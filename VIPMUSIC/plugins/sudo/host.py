# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#
import os
import socket

import requests
import urllib3
from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


async def paste_neko(code: str):
    return await VIPbin(code)


import os

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen  # Import pyromod for better user input handling

# Constants
HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")  # Store this in an environment variable
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"


# Function to fetch app.json from the repo
def fetch_app_json(repo_url):
    app_json_url = f"{repo_url}/raw/master/app.json"
    response = requests.get(app_json_url)
    if response.status_code == 200:
        return response.json()  # Returns parsed JSON
    else:
        return None


# Function to check if the app name is already taken on Heroku
def is_app_name_taken(app_name, api_key):
    url = f"{HEROKU_API_URL}/apps/{app_name}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    response = requests.get(url, headers=headers)
    return response.status_code == 200  # Returns True if app exists, False otherwise


# Function to deploy the app to Heroku
def deploy_to_heroku(app_name, env_vars, api_key):
    url = f"{HEROKU_API_URL}/apps"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    payload = {"name": app_name, "env": env_vars}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code, response.json()


# Command to start hosting process
@app.on_message(filters.command("host") & filters.private & filters.user(SUDOERS))
async def host_app(client: Client, message: Message):
    # Fetch app.json from the repo
    app_json_data = fetch_app_json(REPO_URL)
    if not app_json_data:
        await message.reply_text("Could not fetch app.json from the repository.")
        return

    # Extract environment variables
    env_vars = app_json_data.get("env", {})
    if not env_vars:
        await message.reply_text("No environment variables found in app.json.")
        return

    # Ask for the app name first (HEROKU_APP_NAME)
    await message.reply_text("Please provide a name for the Heroku app:")
    app_name = await client.listen(message.chat.id)

    # Check if the app name is already taken on Heroku
    while is_app_name_taken(app_name.text, HEROKU_API_KEY):
        await message.reply_text(
            f"The app name '{app_name.text}' is already taken. Please provide another name:"
        )
        app_name = await client.listen(message.chat.id)

    # Store the valid app name in user inputs
    user_inputs = {"HEROKU_APP_NAME": app_name.text}

    # Ask for the remaining environment variables
    for var_name in env_vars:
        await message.reply_text(
            f"Please provide a value for {var_name} (or type /next to skip):"
        )
        user_input = await client.listen(message.chat.id)

        if user_input.text.lower() != "/next":
            user_inputs[var_name] = user_input.text

    # Deploy the app to Heroku
    await message.reply_text("All variables collected. Deploying the app to Heroku...")
    status, result = deploy_to_heroku(
        user_inputs["HEROKU_APP_NAME"], user_inputs, HEROKU_API_KEY
    )

    if status == 201:
        await message.reply_text("App successfully deployed!")
    else:
        await message.reply_text(f"Error deploying app: {result}")
