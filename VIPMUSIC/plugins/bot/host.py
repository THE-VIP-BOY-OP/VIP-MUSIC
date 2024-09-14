import asyncio
import os
import socket

import requests
import urllib3
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import save_app_info
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")  # Pre-defined variable
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"  # Pre-defined variable
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"
UPSTREAM_REPO = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"  # Pre-defined variable
UPSTREAM_BRANCH = "master"  # Pre-defined variable
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


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

    # Return parsed JSON for `get` method as well
    if method == "get":
        return response.status_code, response.json()
    else:
        return response.status_code, (
            response.json() if response.status_code == 200 else response.text
        )


def make_heroku_request(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"
    response = getattr(requests, method)(url, headers=headers, json=payload)
    return response.status_code, (
        response.json() if response.status_code == 200 else None
    )


def make_heroku_requesta(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"
    response = getattr(requests, method)(url, headers=headers, json=payload)

    # Return parsed JSON for `get` method as well
    if method == "get":
        return response.status_code, response.json()
    else:
        return response.status_code, (
            response.json() if response.status_code == 200 else response.text
        )


def make_heroku_requestb(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"
    response = getattr(requests, method)(url, headers=headers, json=payload)
    return response.status_code, response.json() if method != "get" else response


def make_heroku_requestc(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"
    response = getattr(requests, method)(url, headers=headers, json=payload)
    return response.status_code, (
        response.json() if response.status_code == 200 else None
    )


async def fetch_apps():
    status, apps = make_heroku_requestc("apps", HEROKU_API_KEY)
    return apps if status == 200 else None


async def get_owner_id(app_name):
    status, config_vars = make_heroku_request(
        f"apps/{app_name}/config-vars", HEROKU_API_KEY
    )
    if status == 200 and config_vars:
        return config_vars.get("OWNER_ID")
    return None


async def collect_env_variables(message, env_vars):
    user_inputs = {}
    await message.reply_text(
        "Provide the values for the required environment variables. Type /cancel at any time to cancel the deployment."
    )

    for var_name, var_info in env_vars.items():
        if var_name in [
            "HEROKU_APP_NAME",
            "HEROKU_API_KEY",
            "UPSTREAM_REPO",
            "UPSTREAM_BRANCH",
            "API_ID",
            "API_HASH",
        ]:
            continue  # Skip hardcoded variables

        # Get description from the JSON file
        description = var_info.get("description", "No description provided.")

        try:
            # Ask the user for input with the variable's description
            response = await app.ask(
                message.chat.id,
                f"Provide a value for **{var_name}**\n\n**About:** {description}\n\nType /cancel to stop hosting.",
                timeout=300,
            )
            if response.text == "/cancel":
                await message.reply_text("**Deployment canceled.**")
                return None
            user_inputs[var_name] = response.text
        except ListenerTimeout:
            await message.reply_text(
                "Timeout! You must provide the variables within 5 Minutes. Restart the process to deploy."
            )
            return None

    # Add hardcoded variables
    user_inputs["HEROKU_APP_NAME"] = app_name
    user_inputs["HEROKU_API_KEY"] = HEROKU_API_KEY
    user_inputs["UPSTREAM_REPO"] = UPSTREAM_REPO
    user_inputs["UPSTREAM_BRANCH"] = UPSTREAM_BRANCH
    user_inputs["API_ID"] = API_ID
    user_inputs["API_HASH"] = API_HASH

    return user_inputs

    if status == 200:
        await callback_query.message.edit_text(
            f"Dynos for app `{app_name}` turned on successfully.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            f"Failed to turn on dynos: {result}", reply_markup=reply_markup
        )


async def check_app_name_availability(app_name):
    # Try to create a temporary app with the provided name
    status, result = make_heroku_request(
        "apps",
        HEROKU_API_KEY,
        method="post",
        payload={"name": app_name, "region": "us", "stack": "container"},
    )
    if status == 201:
        # App created successfully, now delete it
        delete_status, delete_result = make_heroku_request(
            f"apps/{app_name}",
            HEROKU_API_KEY,
            method="delete",
        )
        if delete_status == 200:
            return True  # App name is available
    else:
        return False  # App name is not available


@app.on_message(filters.command("host") & filters.private & SUDOERS)
async def host_app(client, message):
    global app_name  # Declare global to use it everywhere

    while True:
        try:
            # Ask the user for the app name
            response = await app.ask(
                message.chat.id,
                "Provide a Heroku app name (small letters):",
                timeout=300,
            )
            app_name = response.text  # Set the app name variable here
        except ListenerTimeout:
            await message.reply_text("Timeout! Restart the process again to deploy.")
            return await host_app(client, message)

        # Check if the app name is available by trying to create and then delete it
        if await check_app_name_availability(app_name):
            await message.reply_text(
                f"App name `{app_name}` is available. Proceeding..."
            )
            break  # Exit the loop if the app name is valid
        else:
            # Inform the user and ask for a new app name
            await message.reply_text("This app name is not available. Try another one.")

    # Proceed with the deployment process if the app name is available
    app_json = fetch_app_json(REPO_URL)
    if not app_json:
        await message.reply_text("Could not fetch app.json.")
        return

    env_vars = app_json.get("env", {})
    user_inputs = await collect_env_variables(message, env_vars)
    if user_inputs is None:
        return

    # Now create the actual app with the selected name
    status, result = make_heroku_request(
        "apps",
        HEROKU_API_KEY,
        method="post",
        payload={"name": app_name, "region": "us", "stack": "container"},
    )
    if status == 201:
        await message.reply_text("✅ Done! Your app has been created.")

        # Set environment variables
        make_heroku_request(
            f"apps/{app_name}/config-vars",
            HEROKU_API_KEY,
            method="patch",
            payload=user_inputs,
        )

        # Trigger build
        status, result = make_heroku_request(
            f"apps/{app_name}/builds",
            HEROKU_API_KEY,
            method="post",
            payload={"source_blob": {"url": f"{REPO_URL}/tarball/master"}},
        )

        buttons = [
            [InlineKeyboardButton("Turn On Dynos", callback_data=f"dyno_on:{app_name}")]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        if status == 201:
            ok = await message.reply_text("⌛ Deploying Please wait a moment...")
            await save_app_info(message.from_user.id, app_name)
            await asyncio.sleep(200)
            await ok.delete()
            # Edit message to show dynos button after deployment
            await message.reply_text(
                "✅ Deployed Successfully...✨\n\n🥀 Please turn on dynos 👇",
                reply_markup=reply_markup,
            )
        else:
            await message.reply_text(f"Error triggering build: {result}")

    else:
        await message.reply_text(f"Error deploying app: {result}")


# ============================CHECK APP==================================#


@app.on_message(
    filters.command(["heroku", "hosts", "hosted", "mybots", "myhost"]) & SUDOERS
)
async def get_deployed_apps(client, message):
    apps = await fetch_apps()

    if not apps:
        await message.reply_text("No apps found on Heroku.")
        return

    buttons = [
        [InlineKeyboardButton(app["name"], callback_data=f"app:{app['name']}")]
        for app in apps
    ]

    buttons.append([InlineKeyboardButton("Back", callback_data="main_menu")])

    # Send the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_text("Select an app:", reply_markup=reply_markup)


# ============================DELETE APP==================================#


@app.on_message(filters.command("deletehost") & filters.private & SUDOERS)
async def delete_deployed_app(client, message):
    # Fetch the list of deployed apps for the user
    user_apps = await fetch_apps()

    # Check if the user has any deployed apps
    if not user_apps:
        await message.reply_text("You have no deployed bots")
        return

    # Create buttons for each deployed app
    buttons = [
        [InlineKeyboardButton(app_name, callback_data=f"delete_app:{app_name}")]
        for app_name in user_apps
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Send a message to select the app for deletion
    await message.reply_text(
        "Please select the app you want to delete:", reply_markup=reply_markup
    )


# ===============================AUTO DYNOS RESTART===================================


import asyncio

import aiohttp

# Your Heroku API key


# Heroku API endpoint

HEADERS = {
    "Authorization": f"Bearer {HEROKU_API_KEY}",
    "Accept": "application/vnd.heroku+json; version=3",
}


async def make_heroku_requestc(endpoint, api_key):
    """Make asynchronous requests to Heroku API."""
    url = f"{HEROKU_API_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            status = response.status
            apps = await response.json() if status == 200 else None
            return status, apps


async def check_app_status(app_name):
    """Check the dyno status of a given Heroku app."""
    dynos_url = f"{HEROKU_API_URL}/apps/{app_name}/dynos"
    async with aiohttp.ClientSession() as session:
        async with session.get(dynos_url, headers=HEADERS) as response:
            if response.status == 200:
                dynos = await response.json()
                for dyno in dynos:
                    if dyno["state"] in ["crashed", "down"]:
                        print(
                            f"Dyno '{dyno['name']}' in app '{app_name}' is {dyno['state']}."
                        )
                        return True  # Return True if any dyno is crashed or down
                print(f"All dynos in '{app_name}' are running normally.")
                return False
            else:
                print(f"Failed to fetch dyno status for {app_name}.")
                return False


async def restart_dynos(app_name):
    """Restart all dynos of a given Heroku app."""
    dynos_url = f"{HEROKU_API_URL}/apps/{app_name}/dynos"
    async with aiohttp.ClientSession() as session:
        async with session.delete(dynos_url, headers=HEADERS) as response:
            if response.status == 202:
                print(f"Restarted all dynos for {app_name}.")
            else:
                print(f"Failed to restart dynos for {app_name}.")


async def check_and_restart_apps():
    """Check dyno statuses for all apps and restart dynos if any are crashed or down."""
    apps = await fetch_apps()
    if apps:
        for app in apps:
            app_name = app["name"]
            if await check_app_status(app_name):
                await restart_dynos(app_name)
    else:
        print("Failed to fetch apps.")


async def main():
    """Main loop to check every 10 minutes asynchronously."""
    while True:
        await check_and_restart_apps()
        await asyncio.sleep(30)  # Wait for 10 minutes before next check


# Run the asynchronous loop
asyncio.run(main())
