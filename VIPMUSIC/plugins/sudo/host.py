import os
import socket

import requests
import urllib3
from pyrogram import filters
from pyromod.exceptions import ListenerTimeout

# Import your MongoDB database structure
from your_database_file import delete_app_info, get_app_info, save_app_info

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def paste_neko(code: str):
    return await VIPbin(code)


def fetch_app_json(repo_url):
    app_json_url = f"{repo_url}/raw/master/app.json"
    response = requests.get(app_json_url)
    return response.json() if response.status_code == 200 else None


def make_heroku_request(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"
    response = getattr(requests, method)(url, headers=headers, json=payload)
    return response.status_code, response.json() if method != "get" else response


async def collect_env_variables(message, env_vars):
    user_inputs = {}
    await message.reply_text(
        "Provide the values for the required environment variables. Type /cancel at any time to cancel the deployment."
    )
    for var_name in env_vars:
        try:
            response = await app.ask(
                message.chat.id,
                f"Provide a value for `{var_name}` or type /cancel to stop:",
                timeout=60,
            )
            if response.text == "/cancel":
                await message.reply_text("Deployment canceled.")
                return None
            user_inputs[var_name] = response.text
        except ListenerTimeout:
            await message.reply_text(
                "Timeout! You must provide the variables within 60 seconds. Restart the process to deploy"
            )
            return None
    return user_inputs


@app.on_message(filters.command("host") & filters.private & SUDOERS)
async def host_app(client, message):
    try:
        response = await app.ask(
            message.chat.id, "Provide a Heroku app name:", timeout=60
        )
        app_name = response.text
    except ListenerTimeout:
        await message.reply_text("Timeout! Restart the process again to deploy ")
        return await host_app(client, message)

    if make_heroku_request(f"apps/{app_name}", HEROKU_API_KEY)[0] == 200:
        await message.reply_text("App name is taken. Try another.")
        return

    app_json = fetch_app_json(REPO_URL)
    if not app_json:
        await message.reply_text("Could not fetch app.json.")
        return

    env_vars = app_json.get("env", {})
    user_inputs = await collect_env_variables(message, env_vars)
    if user_inputs is None:
        return

    status, result = make_heroku_request(
        "apps",
        HEROKU_API_KEY,
        method="post",
        payload={"name": app_name, "region": "us", "stack": "heroku-24"},
    )

    if status == 201:
        await message.reply_text("App deployed! Setting environment variables...")
        make_heroku_request(
            f"apps/{app_name}/config-vars",
            HEROKU_API_KEY,
            method="patch",
            payload=user_inputs,
        )
        status, result = make_heroku_request(
            f"apps/{app_name}/builds",
            HEROKU_API_KEY,
            method="post",
            payload={"source_blob": {"url": f"{REPO_URL}/tarball/master"}},
        )
        if status == 201:
            await message.reply_text("Build triggered successfully!")

            # Save app info to the database
            await save_app_info(message.from_user.id, app_name)
            await message.reply_text(f"App {app_name} saved to the database!")
        else:
            await message.reply_text(f"Error triggering build: {result}")
    else:
        await message.reply_text(f"Error deploying app: {result}")


@app.on_message(filters.command("get_apps") & filters.private & SUDOERS)
async def get_deployed_apps(client, message):
    apps = await get_app_info(message.from_user.id)
    if apps:
        app_list = "\n".join(apps)
        await message.reply_text(f"Your deployed apps:\n{app_list}")
    else:
        await message.reply_text("You have no deployed apps.")


@app.on_message(filters.command("delete_app") & filters.private & SUDOERS)
async def delete_deployed_app(client, message):
    try:
        response = await app.ask(
            message.chat.id, "Provide the app name to delete:", timeout=60
        )
        app_name = response.text
    except ListenerTimeout:
        await message.reply_text("Timeout! Please restart the process.")
        return

    # Delete from Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}", HEROKU_API_KEY, method="delete"
    )
    if status == 200:
        await delete_app_info(message.from_user.id, app_name)
        await message.reply_text(f"App {app_name} deleted successfully.")
    else:
        await message.reply_text(f"Failed to delete app: {result}")
