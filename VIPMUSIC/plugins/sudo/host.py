import os
import socket
import time

import requests
import urllib3
from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def paste_neko(code: str):
    return await VIPbin(code)


import os
import time

import requests
from pyrogram import (  # dp: Required for handling bot commands and messages
    Client,
    filters,
)
from pyrogram.types import Message  # dp: Required for message handling

# Constants
HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv(
    "HEROKU_API_KEY"
)  # Make sure to set this as an environment variable
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"

# Global variables to store deployment data
env_vars = {}
user_inputs = {}
current_var = ""
skip_var = False
app_name = ""


# Function to fetch app.json from the repo
def fetch_app_json(repo_url):
    app_json_url = f"{repo_url}/raw/master/app.json"
    response = requests.get(app_json_url)
    if response.status_code == 200:
        return response.json()  # Returns parsed JSON
    else:
        return None


# Function to check if the app name already exists on Heroku
def check_app_exists(app_name, api_key):
    url = f"{HEROKU_API_URL}/apps/{app_name}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200  # Returns True if the app exists


# Function to fetch build logs after deployment
def fetch_build_logs(app_id, api_key):
    url = f"{HEROKU_API_URL}/apps/{app_id}/logs"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return "Unable to fetch logs."


# Function to deploy the app to Heroku
def deploy_to_heroku(app_name, env_vars, api_key):
    app_create_url = f"{HEROKU_API_URL}/apps"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    payload = {"name": app_name}
    response = requests.post(app_create_url, json=payload, headers=headers)

    if response.status_code != 201:
        return response.status_code, response.json()

    app_id = response.json().get("id")

    # Step 2: Set environment variables
    config_vars_url = f"{HEROKU_API_URL}/apps/{app_id}/config-vars"
    config_response = requests.patch(config_vars_url, json=env_vars, headers=headers)
    if config_response.status_code != 200:
        return config_response.status_code, config_response.json()

    # Step 3: Set the buildpack (if needed)
    buildpack_url = f"{HEROKU_API_URL}/apps/{app_id}/buildpack-installations"
    buildpack_payload = {"updates": [{"buildpack": BUILDPACK_URL}]}
    buildpack_response = requests.put(
        buildpack_url, json=buildpack_payload, headers=headers
    )

    if buildpack_response.status_code != 200:
        return buildpack_response.status_code, buildpack_response.json()

    # Step 4: Trigger the build
    build_url = f"{HEROKU_API_URL}/apps/{app_id}/builds"
    build_payload = {"source_blob": {"url": f"{REPO_URL}/tarball/master"}}
    build_response = requests.post(build_url, json=build_payload, headers=headers)

    # Fetch build logs after the deployment
    if build_response.status_code == 201:
        # Successful build trigger
        time.sleep(5)  # Wait for the build to start
        logs = fetch_build_logs(app_id, api_key)
        return build_response.status_code, {"logs": logs}
    else:
        return build_response.status_code, build_response.json()


# Command to start hosting process
@app.on_message(filters.command("host"))
async def host_app(client: Client, message: Message):
    global env_vars, user_inputs, current_var, skip_var, app_name

    # Ask for app name first
    await message.reply_text("Please provide a name for the Heroku app:")
    app_name = ""  # Reset the app name to ensure it's set in the next step


# Handling the app name input
@app.on_message(filters.text)
async def handle_app_name(client: Client, message: Message):
    global app_name

    if not app_name:  # If we haven't received the app name yet
        app_name = message.text

        # Check if the app name already exists on Heroku
        if check_app_exists(app_name, HEROKU_API_KEY):
            await message.reply_text(
                "The app name is already taken. Please provide another app name:"
            )
            app_name = ""  # Reset the app name so the user can input a new one
        else:
            await message.reply_text(
                f"App name `{app_name}` is available. Proceeding to set environment variables..."
            )

            # Fetch app.json from the repo
            app_json_data = fetch_app_json(REPO_URL)
            if not app_json_data:
                await message.reply_text(
                    "Could not fetch app.json from the repository."
                )
                return

            # Extract environment variables
            env_vars = app_json_data.get("env", {})
            if not env_vars:
                await message.reply_text("No environment variables found in app.json.")
                return

            # Proceed to ask for environment variables
            await ask_for_next_variable(client, message)


# Function to ask for the next environment variable
async def ask_for_next_variable(client: Client, message: Message):
    global current_var, user_inputs, env_vars

    var_list = list(env_vars.keys())
    if not current_var:  # Start with the first variable
        current_var = var_list[0]

    await message.reply_text(
        f"Please provide a value for `{current_var}` (or type /next to skip):"
    )


# Handling user inputs for environment variables
@app.on_message(filters.text)
async def handle_env_input(client: Client, message: Message):
    global current_var, skip_var, user_inputs, env_vars

    if message.text == "/next":  # Skip the current variable
        skip_var = True
    else:
        user_inputs[current_var] = (
            message.text
        )  # Store the input for the current variable

    # Get the next variable or deploy the app if done
    await get_next_variable(client, message)


# Function to get the next variable or deploy the app
async def get_next_variable(client: Client, message: Message):
    global current_var, user_inputs, env_vars

    var_list = list(env_vars.keys())
    current_index = var_list.index(current_var)

    if current_index + 1 < len(var_list):
        current_var = var_list[current_index + 1]
        await message.reply_text(
            f"Please provide a value for `{current_var}` (or type /next to skip):"
        )
    else:
        await message.reply_text(
            "All variables collected. Deploying the app to Heroku..."
        )
        status, result = deploy_to_heroku(app_name, user_inputs, HEROKU_API_KEY)
        if status == 201:
            await message.reply_text("App successfully deployed!")
            await message.reply_text(f"Build logs:\n{result['logs']}")
        else:
            await message.reply_text(f"Error deploying app: {result}")
