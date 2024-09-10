import os
import socket
import aiohttp  # Changed from requests to aiohttp for async requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import delete_app_info, get_app_info, save_app_info
from VIPMUSIC.utils.pastebin import VIPbin

HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
REPO_URL = os.getenv("REPO_URL", "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")  # Moved to env variable
BUILDPACK_URL = os.getenv("BUILDPACK_URL", "https://github.com/heroku/heroku-buildpack-python")


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def paste_neko(code: str):
    return await VIPbin(code)


async def fetch_app_json(repo_url):
    app_json_url = f"{repo_url}/raw/master/app.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(app_json_url) as response:
            if response.status == 200:
                return await response.json()
            return None


async def make_heroku_request(endpoint, api_key, method="get", payload=None):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    url = f"{HEROKU_API_URL}/{endpoint}"

    async with aiohttp.ClientSession() as session:
        async with session.request(method, url, headers=headers, json=payload) as response:
            if response.status == 200:
                return response.status, await response.json()
            return response.status, await response.text()


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
                "Timeout! You must provide the variables within 60 seconds. Restart the process to deploy."
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
        await message.reply_text("Timeout! Restart the process again to deploy.")
        return await host_app(client, message)

    status, result = await make_heroku_request(f"apps/{app_name}", HEROKU_API_KEY)

    if status == 200:
        await message.reply_text("App name is taken. Try another.")
        return

    app_json = await fetch_app_json(REPO_URL)
    if not app_json:
        await message.reply_text("Could not fetch app.json.")
        return

    env_vars = app_json.get("env", {})
    user_inputs = await collect_env_variables(message, env_vars)
    if user_inputs is None:
        return

    status, result = await make_heroku_request(
        "apps",
        HEROKU_API_KEY,
        method="post",
        payload={"name": app_name, "region": "us", "stack": "heroku-24"},
    )

    if status == 201:
        await message.reply_text("App deployed! Setting environment variables...")
        await make_heroku_request(
            f"apps/{app_name}/config-vars",
            HEROKU_API_KEY,
            method="patch",
            payload=user_inputs,
        )
        status, result = await make_heroku_request(
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
    elif status == 403:
        await message.reply_text("Permission denied. Please check your API key.")
    else:
        await message.reply_text(f"Error deploying app: {result}")


@app.on_message(filters.command("myhost") & filters.private & SUDOERS)
async def get_deployed_apps(client, message):
    apps = await get_app_info(message.from_user.id)
    if apps:
        buttons = [
            [InlineKeyboardButton(app_name, callback_data=f"app:{app_name}")]
            for app_name in apps
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            "Click the below app buttons to check your bots hosted on Heroku.",
            reply_markup=reply_markup,
        )
    else:
        await message.reply_text("You have no deployed apps.")


@app.on_callback_query(filters.regex(r"^app:(.+)"))
async def app_options(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [InlineKeyboardButton("Edit Variables", callback_data=f"edit_vars:{app_name}")],
        [InlineKeyboardButton("Get Logs", callback_data=f"get_logs:{app_name}")],
        [InlineKeyboardButton("Restart All Dynos", callback_data=f"restart_dynos:{app_name}")],
        [InlineKeyboardButton("Back", callback_data="back_to_apps")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.reply_text(
        f"Tap on the given buttons to edit or get logs of {app_name} app from Heroku.",
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^save_var:(.+):(.+):(.+)"))
async def save_new_variable(client, callback_query):
    app_name, var_name, var_value = callback_query.data.split(":")[1:4]

    status, result = await make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: var_value},
    )

    if status == 200:
        await callback_query.message.reply_text(
            f"Variable `{var_name}` with value `{var_value}` saved successfully."
        )
    else:
        await callback_query.message.reply_text(f"Failed to save variable: {result}")


@app.on_callback_query(filters.regex(r"^restart_dynos:(.+)"))
async def restart_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = await make_heroku_request(
        f"apps/{app_name}/dynos", HEROKU_API_KEY, method="delete"
    )

    if status == 202:
        await callback_query.message.reply_text(
            f"Restarting all dynos for app `{app_name}`..."
        )
    else:
        await callback_query.message.reply_text(f"Failed to restart dynos: {result}")


@app.on_callback_query(filters.regex(r"back_to_apps"))
async def back_to_apps(client, callback_query):
    await get_deployed_apps(client, callback_query.message)


@app.on_callback_query(filters.regex(r"^get_logs:(.+)"))
async def get_app_logs(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = await make_heroku_request(
        f"apps/{app_name}/log-sessions",
        HEROKU_API_KEY,
        method="post",
        payload={"lines": 100, "source": "app"},
    )

    if status == 201:
        logs_url = result.get("logplex_url")
        async with aiohttp.ClientSession() as session:
            async with session.get(logs_url) as logs_response:
                logs = await logs_response.text()

        paste_url = await VIPbin(logs)
        await callback_query.message.reply_text(
            f"Here are the latest logs for {app_name}:\n{paste_url}"
        )
    else:
        await callback_query.message.reply_text(
            f"Failed to retrieve logs for {app_name}: {result}"
        )


@app.on_callback_query(filters.regex(r"^edit_vars:(.+)"))
async def edit_vars(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Fetch environment variables from Heroku
    status, response = make_heroku_request(f"apps/{app_name}/config-vars", HEROKU_API_KEY)

    if status == 200 and isinstance(response, dict):
        if response:
            # Create buttons for each environment variable
            buttons = [
                [InlineKeyboardButton(var_name, callback_data=f"edit_var:{app_name}:{var_name}")]
                for var_name in response.keys()
            ]
            # Add an option to add new variables and a back button
            buttons.append([InlineKeyboardButton("Add New Variable", callback_data=f"add_var:{app_name}")])
            buttons.append([InlineKeyboardButton("Back", callback_data=f"app:{app_name}")])

            reply_markup = InlineKeyboardMarkup(buttons)
            await callback_query.message.reply_text(
                f"Tap on the buttons below to edit or add environment variables for {app_name}.",
                reply_markup=reply_markup,
            )
        else:
            await callback_query.message.reply_text("No variables found for this app.")
    else:
        await callback_query.message.reply_text(f"Failed to retrieve variables: {response}")


@app.on_callback_query(filters.regex(r"^edit_var:(.+):(.+)"))
async def edit_var(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    try:
        response = await app.ask(
            callback_query.message.chat.id,
            f"Enter a new value for `{var_name}` or type /cancel to stop:",
            timeout=60,
        )
        if response.text == "/cancel":
            await callback_query.message.reply_text("Action canceled.")
            return
        new_value = response.text

        status, result = make_heroku_request(
            f"apps/{app_name}/config-vars",
            HEROKU_API_KEY,
            method="patch",
            payload={var_name: new_value},
        )

        if status == 200:
            await callback_query.message.reply_text(
                f"Variable `{var_name}` updated successfully to `{new_value}`."
            )
        else:
            await callback_query.message.reply_text(f"Failed to update variable: {result}")
    except ListenerTimeout:
        await callback_query.message.reply_text(
            "Timeout! You must provide the new variable value within 60 seconds. Restart the process to edit."
        )


@app.on_callback_query(filters.regex(r"^add_var:(.+)"))
async def add_var(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    try:
        response_var_name = await app.ask(
            callback_query.message.chat.id,
            "Enter the name of the new environment variable:",
            timeout=60,
        )
        if response_var_name.text == "/cancel":
            await callback_query.message.reply_text("Action canceled.")
            return

        response_var_value = await app.ask(
            callback_query.message.chat.id,
            f"Enter the value for `{response_var_name.text}` or type /cancel to stop:",
            timeout=60,
        )
        if response_var_value.text == "/cancel":
            await callback_query.message.reply_text("Action canceled.")
            return

        var_name = response_var_name.text
        var_value = response_var_value.text

        status, result = make_heroku_request(
            f"apps/{app_name}/config-vars",
            HEROKU_API_KEY,
            method="patch",
            payload={var_name: var_value},
        )

        if status == 200:
            await callback_query.message.reply_text(
                f"New variable `{var_name}` with value `{var_value}` added successfully."
            )
        else:
            await callback_query.message.reply_text(f"Failed to add new variable: {result}")
    except ListenerTimeout:
        await callback_query.message.reply_text(
            "Timeout! You must provide the variable name and value within 60 seconds. Restart the process to add."
        )


@app.on_message(filters.command("delhost") & filters.private & SUDOERS)
async def delete_hosted_app(client, message):
    apps = await get_app_info(message.from_user.id)

    if apps:
        buttons = [
            [InlineKeyboardButton(app_name, callback_data=f"del_app:{app_name}")]
            for app_name in apps
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            "Select an app to delete:",
            reply_markup=reply_markup,
        )
    else:
        await message.reply_text("You have no deployed apps to delete.")


@app.on_callback_query(filters.regex(r"^del_app:(.+)"))
async def confirm_delete_app(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    try:
        response = await app.ask(
            callback_query.message.chat.id,
            f"Are you sure you want to delete the app `{app_name}`? Type 'yes' to confirm or /cancel to stop:",
            timeout=60,
        )
        if response.text.lower() == "yes":
            status, result = make_heroku_request(
                f"apps/{app_name}",
                HEROKU_API_KEY,
                method="delete",
            )

            if status == 200:
                await delete_app_info(callback_query.from_user.id, app_name)
                await callback_query.message.reply_text(
                    f"App `{app_name}` has been deleted successfully."
                )
            else:
                await callback_query.message.reply_text(f"Failed to delete app: {result}")
        else:
            await callback_query.message.reply_text("Action canceled.")
    except ListenerTimeout:
        await callback_query.message.reply_text("Timeout! Please restart the delete process.")


# Restart All Dynos
@app.on_callback_query(filters.regex(r"^restart_dynos:(.+)"))
async def restart_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = make_heroku_request(
        f"apps/{app_name}/dynos", HEROKU_API_KEY, method="delete"
    )

    if status == 202:
        await callback_query.message.reply_text(
            f"Restarting all dynos for app `{app_name}`..."
        )
    else:
        await callback_query.message.reply_text(f"Failed to restart dynos: {result}")


# Handle logs fetching
@app.on_callback_query(filters.regex(r"^get_logs:(.+)"))
async def get_app_logs(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Fetch logs from Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}/log-sessions",
        HEROKU_API_KEY,
        method="post",
        payload={"lines": 100, "source": "app"},
    )

    if status == 201:
        logs_url = result.get("logplex_url")
        logs = requests.get(logs_url).text

        paste_url = await VIPbin(logs)
        await callback_query.message.reply_text(
            f"Here are the latest logs for {app_name}:\n{paste_url}"
        )
    else:
        await callback_query.message.reply_text(
            f"Failed to retrieve logs for {app_name}: {result}"
        )


# Back to App Options
@app.on_callback_query(filters.regex(r"back_to_apps"))
async def back_to_apps(client, callback_query):
    await get_deployed_apps(client, callback_query.message)
