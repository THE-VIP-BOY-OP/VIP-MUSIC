import os
import socket

import requests
import urllib3
from pyrogram import filters
from pyromod import listen  # Importing pyromod.listen

from VIPMUSIC import app
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def paste_neko(code: str):
    return await VIPbin(code)


# Constants
HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv(
    "HEROKU_API_KEY"
)  # Make sure to set this as an environment variable
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"

# Global variables
env_vars = {}
user_inputs = {}
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


# Deploy the app to Heroku
def deploy_to_heroku(app_name, env_vars, api_key):
    url = f"{HEROKU_API_URL}/apps"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",  # Correct header for versioning
        "Content-Type": "application/json",
    }
    payload = {
        "name": app_name,
        "region": "us",  # Set appropriate region
        "stack": "heroku-24",  # Updated to the supported stack (heroku-22 or heroku-20)
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 201:
        return 201, {"logs": "App deployed successfully"}  # Success
    else:
        return response.status_code, response.json()  # Error


# Function to set environment variables in the Heroku app
def set_heroku_config_vars(app_name, env_vars, api_key):
    url = f"{HEROKU_API_URL}/apps/{app_name}/config-vars"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    payload = env_vars  # Setting the environment variables
    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 200:
        return True
    else:
        return False, response.json()


# Trigger Heroku Build
def trigger_heroku_build(app_name, api_key):
    build_url = f"{HEROKU_API_URL}/apps/{app_name}/builds"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
        "Content-Type": "application/json",
    }
    payload = {
        "source_blob": {
            "url": f"{REPO_URL}/tarball/master"  # URL for tarball of your repo
        },
        "buildpacks": [
            {"url": "heroku/python"},
            {"url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git"}
        ],
        "formation": {
            "worker": {
                "quantity": 1,
                "size": "basic"
            }
        }
    }
    response = requests.post(build_url, headers=headers, json=payload)
    if response.status_code == 201:
        return True
    else:
        return False, response.json()


# Function to collect environment variables
async def collect_env_variables(client, message):
    global env_vars, user_inputs

    for var_name in env_vars.keys():
        await message.reply_text(
            f"Please provide a value for `{var_name}` (or type /next to skip):"
        )
        response = await client.listen(message.chat.id)  # Listen for the input

        if response.from_user.id != message.from_user.id:  # Ensure it's the same user
            continue  # Ignore input from other users

        if response.text == "/next":
            continue  # Skip this variable
        else:
            user_inputs[var_name] = response.text  # Store the variable value

    await message.reply_text("All variables collected. Deploying the app to Heroku...")


# Start hosting process
@app.on_message(filters.command("host") & filters.private)  # Only allow in private messages
async def host_app(client, message):
    global app_name

    # Ask for app name using pyromod
    await message.reply_text("Please provide a name for the Heroku app:")
    response = await client.listen(message.chat.id)  # Listen for app name input

    if response.from_user.id != message.from_user.id:  # Ensure it's the same user
        return  # Ignore messages from other users

    app_name = response.text

    # Check if the app name already exists on Heroku
    if check_app_exists(app_name, HEROKU_API_KEY):
        await message.reply_text(
            "The app name is already taken. Please provide another app name:"
        )
        return  # Exit if app name is taken

    await message.reply_text(
        f"App name `{app_name}` is available. Proceeding to set environment variables..."
    )

    # Fetch app.json from the repo
    app_json_data = fetch_app_json(REPO_URL)
    if not app_json_data:
        await message.reply_text("Could not fetch app.json from the repository.")
        return

    # Extract environment variables
    global env_vars
    env_vars = app_json_data.get("env", {})
    if not env_vars:
        await message.reply_text("No environment variables found in app.json.")
        return

    # Proceed to collect environment variables
    await collect_env_variables(client, message)

    # Deploy the app
    status, result = deploy_to_heroku(app_name, user_inputs, HEROKU_API_KEY)
    if status == 201:
        await message.reply_text("App successfully deployed!")

        # Set environment variables in Heroku
        set_status = set_heroku_config_vars(app_name, user_inputs, HEROKU_API_KEY)
        if set_status is True:
            await message.reply_text("Environment variables set successfully.")

            # Trigger Heroku build with dynos auto-scaled
            build_status = trigger_heroku_build(app_name, HEROKU_API_KEY)
            if build_status is True:
                await message.reply_text(
                    "Build triggered successfully, and dynos are configured to start automatically!"
                )
            else:
                await message.reply_text(f"Error triggering build: {build_status[1]}")
        else:
            await message.reply_text(
                f"Error setting environment variables: {set_status[1]}"
            )
    else:
        await message.reply_text(f"Error deploying app: {result}")
