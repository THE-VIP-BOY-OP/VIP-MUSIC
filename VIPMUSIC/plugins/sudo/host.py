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

import asyncio
import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Bot Initialization

# Constants
HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")  # Store this in an environment variable
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"

# Global variables to store deployment data
env_vars = {}
user_inputs = {}
current_var = ""
skip_var = False

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
@app.on_message(filters.command("host"))
async def host_app(client: Client, message: Message):
    global env_vars, user_inputs, current_var, skip_var

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

    user_inputs.clear()
    skip_var = False

    # Ask for the app name first (HEROKU_APP_NAME)
    current_var = "HEROKU_APP_NAME"
    await message.reply_text("Please provide a name for the Heroku app:")

# Handling user inputs for environment variables
@app.on_message(filters.text & filters.user(SUDOERS))
async def handle_env_input(client: Client, message: Message):
    global current_var, skip_var, user_inputs, env_vars

    # If we are asking for the app name (HEROKU_APP_NAME)
    if current_var == "HEROKU_APP_NAME":
        app_name = message.text

        # Check if the app name is already taken on Heroku
        if is_app_name_taken(app_name, HEROKU_API_KEY):
            await message.reply_text(f"The app name '{app_name}' is already taken. Please provide another name:")
            return  # Keep asking for a valid app name

        # Store the valid app name in user inputs
        user_inputs[current_var] = app_name

        # Proceed to the next environment variable
        await get_next_variable(client, message)
        return

    # Handle /next command to skip variable
    if message.text == "/next":
        skip_var = True
        await get_next_variable(client, message)
        return

    # Store the input for the current variable
    if not skip_var:
        user_inputs[current_var] = message.text

    # Get the next variable
    await get_next_variable(client, message)

# Function to get the next variable or deploy the app
async def get_next_variable(client: Client, message: Message):
    global current_var, user_inputs, env_vars

    # Get the list of variables
    var_list = list(env_vars.keys())
    
    # Check if we're still asking for environment variables
    if current_var != "HEROKU_APP_NAME" and current_var in var_list:
        current_index = var_list.index(current_var)
    else:
        current_index = -1  # Start with the first variable

    # Check if there are more variables to ask for
    if current_index + 1 < len(var_list):
        current_var = var_list[current_index + 1]
        await message.reply_text(f"Please provide a value for {current_var} (or type /next to skip):")
    else:
        # If all variables are collected, proceed to deploy the app
        await message.reply_text("All variables collected. Deploying the app to Heroku...")

        # Use the app name from user inputs
        app_name = user_inputs.get("HEROKU_APP_NAME")

        # Deploy the app
        status, result = deploy_to_heroku(app_name, user_inputs, HEROKU_API_KEY)
        if status == 201:
            await message.reply_text("App successfully deployed!")
        else:
            await message.reply_text(f"Error deploying app: {result}")
