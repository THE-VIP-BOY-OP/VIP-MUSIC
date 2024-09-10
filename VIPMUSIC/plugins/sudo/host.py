import os

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from pyromod import listen  # Import pyromod to handle user inputs interactively

from VIPMUSIC import app

# Constants
HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"

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


# Function to deploy the app to Heroku using the build endpoint
def deploy_to_heroku(app_name, env_vars, api_key):
    # Step 1: Create the Heroku app
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
    return build_response.status_code, build_response.json()


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

    # Ask for the first environment variable
    current_var = list(env_vars.keys())[0]
    await message.reply_text(
        f"Please provide a value for {current_var} (or type /next to skip):"
    )


# Handling user inputs for environment variables
@app.on_message(filters.text)
async def handle_env_input(client: Client, message: Message):
    global current_var, skip_var, user_inputs, env_vars

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
    current_index = var_list.index(current_var)

    # Check if there are more variables to ask for
    if current_index + 1 < len(var_list):
        current_var = var_list[current_index + 1]
        await message.reply_text(
            f"Please provide a value for {current_var} (or type /next to skip):"
        )
    else:
        # If all variables are collected, proceed to deploy the app
        await message.reply_text(
            "All variables collected. Deploying the app to Heroku..."
        )
        app_name = (
            f"{REPO_URL.split('/')[-1].replace('-', '').lower()}app"  # Example app name
        )
        status, result = deploy_to_heroku(app_name, user_inputs, HEROKU_API_KEY)
        if status == 201:
            await message.reply_text("App successfully deployed!")
        else:
            await message.reply_text(f"Error deploying app: {result}")
