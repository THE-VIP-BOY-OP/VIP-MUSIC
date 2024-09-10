import asyncio
import math
import os
import shutil
import socket
from datetime import datetime

import dotenv
import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters
from pyromod import listen  # Import pyromod to handle user inputs interactively

import config
from strings import get_command
from VIPMUSIC import app
from VIPMUSIC.misc import HAPP, SUDOERS, XCB
from VIPMUSIC.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")  # Ensure HEROKU_API_KEY is set in the environment variables
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"

env_vars = {}
user_inputs = {}

# Function to fetch app.json from the repo
def fetch_app_json(repo_url):
    app_json_url = f"{repo_url}/raw/master/app.json"
    response = requests.get(app_json_url)
    if response.status_code == 200:
        return response.json()  # Returns parsed JSON
    else:
        return None

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
@app.on_message(filters.command("host") & SUDOERS)
async def host_app(client, message):
    global env_vars, user_inputs

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

    # Prompt for each environment variable using pyromod
    for var in env_vars:
        try:
            response = await client.ask(
                message.chat.id,
                f"Please provide a value for {var} (or type /skip to skip):",
                filters=filters.text,
                timeout=300,
            )
            if response.text.lower() == "/skip":
                continue
            user_inputs[var] = response.text
        except asyncio.TimeoutError:
            await message.reply_text("You took too long to respond. Please try again.")
            return

    # Proceed to deploy the app
    await message.reply_text("All variables collected. Deploying the app to Heroku...")
    app_name = f"{REPO_URL.split('/')[-1].replace('-', '').lower()}app"  # Example app name
    status, result = deploy_to_heroku(app_name, user_inputs, HEROKU_API_KEY)
    if status == 201:
        await message.reply_text("App successfully deployed!")
    else:
        await message.reply_text(f"Error deploying app: {result}")
