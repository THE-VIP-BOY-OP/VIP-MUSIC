import os

import aiohttp
import requests
import urllib3
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyromod.exceptions import ListenerTimeout

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import delete_app_info

# Import your MongoDB database structure
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


import re


def convert_to_small_caps(text):
    # Mapping for regular letters to small caps
    mapping = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘϙʀꜱᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ",
    )

    # Function to apply the translation, skipping special parts
    def replace(match):
        # Skip text that starts with {, /, is inside `...`, or looks like a URL
        if (
            match.group(0).startswith("{")
            or match.group(0).startswith("/")
            or match.group(0).startswith("`")
        ):
            return match.group(0)
        if re.match(r"https?://", match.group(0)):  # Detect URLs
            return match.group(0)
        return match.group(0).translate(mapping)

    # Regex to match text outside {}, `...`, /commands, and URLs
    pattern = r"\{.*?\}|`[^`]+`|/\w+|https?://\S+|\w+"

    # Apply translation to matches outside the excluded parts
    return re.sub(pattern, replace, text)


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


import aiohttp
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Get Heroku config var (UPSTREAM_REPO)
async def get_heroku_config(app_name):
    url = f"https://api.heroku.com/apps/{app_name}/config-vars"
    headers = {
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3",
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                config_vars = await response.json()
                return config_vars.get(
                    "UPSTREAM_REPO"
                )  # Return the UPSTREAM_REPO value
            else:
                return None  # Handle errors as needed


# Redeploy Heroku app using the specified repo and branch
async def redeploy_heroku_app(app_name, repo_url, branch="master"):
    # Heroku API endpoint to update app's build
    url = f"https://api.heroku.com/apps/{app_name}/builds"
    headers = {
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/vnd.heroku+json; version=3",
    }
    payload = {"source_blob": {"url": f"{repo_url}/tarball/{branch}"}}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            if response.status == 201:
                return True
            else:
                return False


# Fetch branches from a GitHub repository
async def fetch_repo_branches(repo_url):
    owner_repo = repo_url.replace("https://github.com/", "").split("/")
    api_url = f"https://api.github.com/repos/{owner_repo[0]}/{owner_repo[1]}/branches"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                branches_data = await response.json()
                return [branch["name"] for branch in branches_data]
            else:
                return []  # Return empty if fetch fails


# App functions


@app.on_callback_query(filters.regex(r"^app:(.+)") & SUDOERS)
async def app_options(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Manage Dynos"),
                callback_data=f"manage_dynos:{app_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("Restart All Dynos"),
                callback_data=f"restart_dynos:{app_name}",
            ),
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Config Var"),
                callback_data=f"edit_vars:{app_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("View Logs"), callback_data=f"get_logs:{app_name}"
            ),
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Delete Host"),
                callback_data=f"delete_app:{app_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("Re-Deploy"), callback_data=f"redeploy:{app_name}"
            ),
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data="show_apps"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps(
            f"Tap on the given buttons to edit or get logs of {app_name} app from Heroku."
        ),
        reply_markup=reply_markup,
    )


# Callback for "Re-Deploy" button
@app.on_callback_query(filters.regex(r"^redeploy:(.+)") & SUDOERS)
async def redeploy_callback(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    # Show the user options for redeployment
    await callback_query.message.edit(
        text=convert_to_small_caps("From where do you want to deploy?"),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        convert_to_small_caps("Use UPSTREAM_REPO"),
                        callback_data=f"use_upstream_repo:{app_name}",
                    )
                ],
                [
                    InlineKeyboardButton(
                        convert_to_small_caps("Use External Repo"),
                        callback_data=f"use_external_repo:{app_name}",
                    )
                ],
                [
                    InlineKeyboardButton(
                        convert_to_small_caps("Back"), callback_data=f"app:{app_name}"
                    )
                ],
            ]
        ),
    )


# Callback for using UPSTREAM_REPO
@app.on_callback_query(filters.regex(r"^use_upstream_repo:(.+)") & SUDOERS)
async def use_upstream_repo_callback(client, callback_query):
    chat_id = callback_query.message.chat.id
    app_name = callback_query.data.split(":")[1]

    # Continue the process in private chats
    upstream_repo = await get_heroku_config(app_name)

    if upstream_repo:
        branches = await fetch_repo_branches(upstream_repo)
        if branches:
            branch_list = "\n".join(branches)

            # Listen for user's branch name
            response = await app.ask(
                chat_id,
                convert_to_small_caps(
                    f"**Available branches:**\n\n`{branch_list}`\n\nReply with the branch name to deploy."
                ),
                timeout=300,
            )

            # Check if the user is in SUDOERS and the correct chat
            if response.from_user.id not in SUDOERS or response.chat.id != chat_id:
                return await app.send_message(
                    chat_id,
                    convert_to_small_caps("Try Again Please And Give Fast Reply"),
                )

            selected_branch = response.text
            if selected_branch in branches:
                # Ask for confirmation before deploying

                confirmation = await app.ask(
                    chat_id,
                    convert_to_small_caps(
                        f"Do you want to deploy from branch: {selected_branch}?\nType 'yes' or 'no'."
                    ),
                    timeout=300,
                )

                if (
                    confirmation.from_user.id not in SUDOERS
                    or confirmation.chat.id != chat_id
                ):
                    return await app.send_message(
                        chat_id,
                        convert_to_small_caps("Try Again Please And Give Fast Reply"),
                    )

                if confirmation.text.lower() == "yes":
                    success = await redeploy_heroku_app(
                        app_name, upstream_repo, selected_branch
                    )
                    if success:
                        await confirmation.reply_text(
                            convert_to_small_caps(
                                f"App successfully redeployed from branch: {selected_branch}."
                            )
                        )
                    else:
                        await confirmation.reply_text(
                            convert_to_small_caps(
                                f"Failed to redeploy app from branch: {selected_branch}."
                            )
                        )
                else:
                    await confirmation.reply_text(
                        convert_to_small_caps("Deployment canceled.")
                    )
            else:
                await response.reply_text(
                    convert_to_small_caps("Invalid branch name. Please try again.")
                )
        else:
            await callback_query.message.edit(
                convert_to_small_caps("No branches found in the UPSTREAM_REPO.")
            )
    else:
        await callback_query.message.edit(
            convert_to_small_caps("No repo found in UPSTREAM_REPO variable.")
        )


# Callback for using an external repository
@app.on_callback_query(filters.regex(r"^use_external_repo:(.+)") & SUDOERS)
async def use_external_repo_callback(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    try:
        response = await app.ask(
            callback_query.message.chat.id,
            convert_to_small_caps("Please provide the new repo URL."),
            timeout=300,
        )

        if (
            response.from_user.id not in SUDOERS
            or response.chat.id != callback_query.message.chat.id
        ):
            return await app.send_message(
                callback_query.message.chat.id,
                convert_to_small_caps("Try Again Please And Give Fast Reply"),
            )

        if response.from_user.id in SUDOERS:
            new_repo_url = response.text

            # Fetch branches from the provided repo URL
            branches = await fetch_repo_branches(new_repo_url)
            if branches:
                branch_list = "\n".join(branches)

                # Listen for branch selection
                branch_response = await app.ask(
                    response.chat.id,
                    convert_to_small_caps(
                        f"Available branches:\n\n`{branch_list}`\n\nReply with the branch name to deploy."
                    ),
                    timeout=300,
                )

                if (
                    response.from_user.id not in SUDOERS
                    or response.chat.id != response.chat.id
                ):
                    return await app.send_message(
                        response.chat.id,
                        convert_to_small_caps("Try Again Please And Give Fast Reply"),
                    )

                selected_branch = branch_response.text
                if selected_branch in branches:
                    # Ask for confirmation before deploying
                    confirmation = await app.ask(
                        branch_response.chat.id,
                        convert_to_small_caps(
                            f"Do you want to deploy from branch: {selected_branch}?\nType 'yes' or 'no'."
                        ),
                        timeout=300,
                    )

                    if (
                        confirmation.from_user.id not in SUDOERS
                        or response.chat.id != branch_response.chat.id
                    ):
                        return await app.send_message(
                            branch_response.chat.id,
                            convert_to_small_caps(
                                "Try Again Please And Give Fast Reply"
                            ),
                        )

                    if confirmation.text.lower() == "yes":
                        success = await redeploy_heroku_app(
                            app_name, new_repo_url, selected_branch
                        )
                        if success:
                            await confirmation.reply_text(
                                convert_to_small_caps(
                                    f"App successfully redeployed from branch: {selected_branch}."
                                )
                            )
                        else:
                            await confirmation.reply_text(
                                convert_to_small_caps(
                                    f"Failed to redeploy app from branch: {selected_branch}."
                                )
                            )
                    else:
                        await confirmation.reply_text(
                            convert_to_small_caps("Deployment canceled.")
                        )
                else:
                    await branch_response.reply_text(
                        convert_to_small_caps("Invalid branch name. Please try again.")
                    )
            else:
                await response.reply_text(
                    convert_to_small_caps("No branches found or invalid repo URL.")
                )
        else:
            await response.reply_text(
                convert_to_small_caps("You are not authorized to set this value.")
            )
    except ListenerTimeout:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                "**Timeout! No valid input received from SUDOERS. Process canceled.**"
            )
        )
    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")


# Cancel the redeployment process
@app.on_callback_query(filters.regex("cancel_redeploy") & SUDOERS)
async def cancel_redeploy_callback(client, callback_query):
    await callback_query.message.edit_text(
        convert_to_small_caps("Redeployment process canceled.")
    )


@app.on_callback_query(filters.regex("show_apps") & SUDOERS)
async def show_apps(client, callback_query):
    apps = await fetch_apps()

    if not apps:
        await callback_query.message.edit_text(
            convert_to_small_caps("No apps found on Heroku.")
        )
        return

    # Create buttons for each app and a 'Back' button
    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps(app["name"]), callback_data=f"app:{app['name']}"
            )
        ]
        for app in apps
    ]

    # Add the 'Back' button as a new row
    buttons.append(
        [InlineKeyboardButton(convert_to_small_caps("Back"), callback_data="main_menu")]
    )

    # Send the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text(
        convert_to_small_caps("Select your app from given below app list to handle:"),
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^main_menu$") & SUDOERS)
async def main_menu(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Show Deployed Apps"), callback_data="show_apps"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps("Main menu. Choose an option:"), reply_markup=reply_markup
    )


# Handle logs fetching
@app.on_callback_query(filters.regex(r"^get_logs:(.+)") & SUDOERS)
async def get_app_logs(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Fetch logs from Heroku
    status, result = make_heroku_requestb(
        f"apps/{app_name}/log-sessions",
        HEROKU_API_KEY,
        method="post",
        payload={"lines": 100, "source": "app"},
    )

    if status == 201:
        logs_url = result.get("logplex_url")
        logs = requests.get(logs_url).text

        paste_url = await VIPbin(logs)
        await callback_query.answer(
            convert_to_small_caps("Getting Logs..."), show_alert=True
        )
        await callback_query.message.reply_text(
            convert_to_small_caps(
                f"**Here are the latest logs for** {app_name}:\n{paste_url}"
            )
        )
    else:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                f"**Failed to retrieve logs for** {app_name}: {result}"
            )
        )


# Manage Dynos
@app.on_callback_query(filters.regex(r"^manage_dynos:(.+)") & SUDOERS)
async def manage_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Turn On Dynos"),
                callback_data=f"dyno_on:{app_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("Turn Off Dynos"),
                callback_data=f"dyno_off:{app_name}",
            ),
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Dynos Type"),
                callback_data=f"manage_dyno_type:{app_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"app:{app_name}"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps("Choose an action for your dynos:"),
        reply_markup=reply_markup,
    )


# Turn On Dynos
@app.on_callback_query(filters.regex(r"^dyno_on:(.+)") & SUDOERS)
async def turn_on_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = make_heroku_request(
        f"apps/{app_name}/formation/worker",
        HEROKU_API_KEY,
        method="patch",
        payload={"quantity": 1},  # Start with 1 dyno; adjust as needed
    )

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"manage_dynos:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            convert_to_small_caps(
                f"Dynos for app `{app_name}` turned on successfully."
            ),
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            convert_to_small_caps(f"Failed to turn on dynos: {result}"),
            reply_markup=reply_markup,
        )


# Turn Off Dynos
@app.on_callback_query(filters.regex(r"^dyno_off:(.+)") & SUDOERS)
async def turn_off_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = make_heroku_request(
        f"apps/{app_name}/formation/worker",
        HEROKU_API_KEY,
        method="patch",
        payload={"quantity": 0},  # Set to 0 to turn off
    )

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"manage_dynos:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            convert_to_small_caps(
                f"Dynos for app `{app_name}` turned off successfully."
            ),
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            convert_to_small_caps(f"Failed to turn off dynos: {result}"),
            reply_markup=reply_markup,
        )


# 2. Manage Dyno Type: Displaying Basic, Eco, and Professional options
@app.on_callback_query(filters.regex(r"^manage_dyno_type:(.+)") & SUDOERS)
async def manage_dyno_type(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Basic"),
                callback_data=f"set_dyno_basic:{app_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Eco"), callback_data=f"set_dyno_eco:{app_name}"
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Professional"),
                callback_data=f"professional_options:{app_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"app:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps("Choose your Dyno Type:"),
        reply_markup=reply_markup,
    )


# 3. Displaying Professional Options: Standard 1X and Standard 2X
@app.on_callback_query(filters.regex(r"^professional_options:(.+)") & SUDOERS)
async def professional_options(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Standard 1X"),
                callback_data=f"set_dyno_prof_1x:{app_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Standard 2X"),
                callback_data=f"set_dyno_prof_2x:{app_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"),
                callback_data=f"manage_dyno_type:{app_name}",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps("Choose Professional Dyno Type:"),
        reply_markup=reply_markup,
    )


# 4. Setting Dyno Types (Heroku API Call)
def set_dyno_type(app_name, dyno_type):
    endpoint = f"apps/{app_name}/formation/worker"  # Assuming 'web' dyno type, adjust if needed
    payload = {"quantity": 1, "size": dyno_type}

    status, result = make_heroku_request(
        endpoint, HEROKU_API_KEY, method="patch", payload=payload
    )

    return status, result


@app.on_callback_query(filters.regex(r"^set_dyno_basic:(.+)") & SUDOERS)
async def set_dyno_basic(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    status, result = set_dyno_type(app_name, "basic")

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"),
                callback_data=f"manage_dyno_type:{app_name}",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        (
            convert_to_small_caps("Dyno type set to Basic.")
            if status == 200
            else f"Failed: {result}"
        ),
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^set_dyno_eco:(.+)") & SUDOERS)
async def set_dyno_eco(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    status, result = set_dyno_type(app_name, "eco")

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"),
                callback_data=f"manage_dyno_type:{app_name}",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        (
            convert_to_small_caps("Dyno type set to Eco.")
            if status == 200
            else f"Failed: {result}"
        ),
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^set_dyno_prof_1x:(.+)") & SUDOERS)
async def set_dyno_prof_1x(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    status, result = set_dyno_type(app_name, "standard-1X")

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"),
                callback_data=f"manage_dyno_type:{app_name}",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        (
            convert_to_small_caps("Dyno type set to Professional Standard 1X.")
            if status == 200
            else f"Failed: {result}"
        ),
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^set_dyno_prof_2x:(.+)") & SUDOERS)
async def set_dyno_prof_2x(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    status, result = set_dyno_type(app_name, "standard-2X")

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"),
                callback_data=f"manage_dyno_type:{app_name}",
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        (
            convert_to_small_caps("Dyno type set to Professional Standard 2X.")
            if status == 200
            else f"Failed: {result}"
        ),
        reply_markup=reply_markup,
    )


# Restart All Dynos
@app.on_callback_query(filters.regex(r"^restart_dynos:(.+)") & SUDOERS)
async def restart_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = make_heroku_request(
        f"apps/{app_name}/dynos", HEROKU_API_KEY, method="delete"
    )

    if status == 202:
        await callback_query.answer(
            convert_to_small_caps("Restarting All Dynos..."), show_alert=True
        )
        await callback_query.message.reply_text(
            convert_to_small_caps(f"Restarting all dynos for app `{app_name}`...")
        )
    else:
        await callback_query.message.edit_text(
            convert_to_small_caps(f"Failed to restart dynos: {result}")
        )


# Handle Back Button
@app.on_callback_query(filters.regex(r"back_to_apps") & SUDOERS)
async def back_to_apps(client, callback_query):
    await get_deployed_apps(client, callback_query.message)


# Edit Environment Variables
@app.on_callback_query(filters.regex(r"^edit_vars:(.+)") & SUDOERS)
async def edit_vars(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Fetch environment variables from Heroku
    status, response = make_heroku_request(
        f"apps/{app_name}/config-vars", HEROKU_API_KEY
    )

    print(f"Status: {status}, Response: {response}")

    if status == 200 and isinstance(response, dict):
        if response:
            buttons = [
                [
                    InlineKeyboardButton(
                        convert_to_small_caps(var_name),
                        callback_data=f"edit_var:{app_name}:{var_name}",
                    )
                ]
                for var_name in response.keys()
            ]

            # Add "Add New Variable" and Back button
            buttons.append(
                [
                    InlineKeyboardButton(
                        convert_to_small_caps("➕ Add New Variable ➕"),
                        callback_data=f"add_var:{app_name}",
                    )
                ]
            )
            buttons.append(
                [
                    InlineKeyboardButton(
                        convert_to_small_caps("Back"), callback_data=f"app:{app_name}"
                    )
                ]
            )

            reply_markup = InlineKeyboardMarkup(buttons)

            await callback_query.message.edit_text(
                convert_to_small_caps("Select a variable to edit:"),
                reply_markup=reply_markup,
            )
        else:
            await callback_query.message.edit_text(
                convert_to_small_caps("No environment variables found for this app.")
            )
    else:
        await callback_query.message.edit_text(
            convert_to_small_caps(
                f"Failed to fetch environment variables. Status: {status}, Response: {response}"
            )
        )


@app.on_callback_query(filters.regex(r"^edit_var:(.+):(.+)") & SUDOERS)
async def edit_variable_options(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Edit"),
                callback_data=f"edit_var_value:{app_name}:{var_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Delete"),
                callback_data=f"delete_var:{app_name}:{var_name}",
            )
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"edit_vars:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps(f"Choose an option for the variable `{var_name}`:"),
        reply_markup=reply_markup,
    )


# Step 1: Ask for the new value and then confirm with the user
@app.on_callback_query(filters.regex(r"^edit_var_value:(.+):(.+)") & SUDOERS)
async def edit_variable_value(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    try:
        new_value = None
        while new_value is None:
            try:
                response = await app.ask(
                    callback_query.message.chat.id,
                    convert_to_small_caps(
                        f"**Send the new value for** `{var_name}` **within 1 minute (Only SUDOERS allowed)**:"
                    ),
                    timeout=60,
                )

                if response.from_user.id in SUDOERS:
                    new_value = response.text
                else:
                    await app.send_message(
                        callback_query.message.chat.id,
                        convert_to_small_caps(
                            "Only SUDOERS can provide a valid input. Please try again."
                        ),
                    )

            except ListenerTimeout:
                await callback_query.message.reply_text(
                    convert_to_small_caps(
                        "**Timeout! No valid input received from SUDOERS. Process canceled.**"
                    )
                )
                return

    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")
        return

    # Step 2: Ask for confirmation via text
    try:
        confirmation = await app.ask(
            callback_query.message.chat.id,
            convert_to_small_caps(
                f"Do you want to save the new value `{new_value}` for `{var_name}`?\nType 'yes' to confirm or 'no' to cancel."
            ),
            timeout=60,
        )

        if confirmation.from_user.id not in SUDOERS:
            await app.send_message(
                callback_query.message.chat.id,
                convert_to_small_caps(
                    "Only SUDOERS can confirm the input. Please try again."
                ),
            )
            return

        if confirmation.text.lower() == "yes":
            await save_variable_value(
                client, callback_query, app_name, var_name, new_value
            )
        else:
            await callback_query.message.reply_text(
                convert_to_small_caps(f"Edit operation for app `{app_name}` canceled.")
            )
    except ListenerTimeout:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                "**Timeout! No valid confirmation received. Process canceled.**"
            )
        )
    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")


async def save_variable_value(client, callback_query, app_name, var_name, new_value):
    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: new_value},
    )

    if status == 200:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                f"Variable `{var_name}` updated successfully to `{new_value}`."
            )
        )
    else:
        await callback_query.message.reply_text(
            convert_to_small_caps(f"Failed to update variable: {result}")
        )


# Step 1: Confirmation before deleting a variable
@app.on_callback_query(filters.regex(r"^delete_var:(.+):(.+)") & SUDOERS)
async def delete_variable_confirmation(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Yes"),
                callback_data=f"confirm_delete_var:{app_name}:{var_name}",
            ),
            InlineKeyboardButton(
                convert_to_small_caps("No"),
                callback_data=f"cancel_delete_var:{app_name}",
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps(
            f"**Are you sure you want to delete the variable** `{var_name}`?"
        ),
        reply_markup=reply_markup,
    )


# Step 2: If the user clicks Yes, delete the variable
@app.on_callback_query(filters.regex(r"^confirm_delete_var:(.+):(.+)") & SUDOERS)
async def confirm_delete_variable(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: None},
    )

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"edit_vars:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            convert_to_small_caps(
                f"**Variable** `{var_name}` **deleted successfully from** `{app_name}`."
            ),
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            convert_to_small_caps(f"**Failed to delete variable:** {result}"),
            reply_markup=reply_markup,
        )


# Step 3: If the user clicks No, cancel the delete operation
@app.on_callback_query(filters.regex(r"^cancel_delete_var:(.+)") & SUDOERS)
async def cancel_delete_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"edit_vars:{app_name}"
            )
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        convert_to_small_caps(f"**Delete operation for app `{app_name}` canceled.**"),
        reply_markup=reply_markup,
    )


# Add New Variable


# Add New Variable
@app.on_callback_query(filters.regex(r"^add_var:(.+)") & SUDOERS)
async def add_new_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    try:
        # Step 1: Ask for variable name from SUDOERS
        var_name = None
        while var_name is None:
            try:
                response = await app.ask(
                    callback_query.message.chat.id,
                    convert_to_small_caps(
                        "**Please send the new variable name (Only SUDOERS allowed)**:"
                    ),
                    timeout=300,
                )

                if (
                    response.from_user.id in SUDOERS
                    and response.chat.id == callback_query.message.chat.id
                ):
                    var_name = response.text
                else:
                    await app.send_message(
                        callback_query.message.chat.id,
                        convert_to_small_caps(
                            "Only SUDOERS can provide a valid input. Please try again."
                        ),
                    )

            except ListenerTimeout:
                await callback_query.message.reply_text(
                    convert_to_small_caps(
                        "**Timeout! No valid input received from SUDOERS. Process canceled.**"
                    )
                )
                return

        # Step 2: Ask for variable value from SUDOERS
        var_value = None
        while var_value is None:
            try:
                response = await app.ask(
                    callback_query.message.chat.id,
                    convert_to_small_caps(
                        f"**Now send the value for `{var_name}` (Only SUDOERS allowed):**"
                    ),
                    timeout=60,
                )

                if response.from_user.id in SUDOERS:
                    var_value = response.text
                else:
                    await app.send_message(
                        callback_query.message.chat.id,
                        convert_to_small_caps(
                            "Only SUDOERS can provide a valid input. Please try again."
                        ),
                    )

            except ListenerTimeout:
                await callback_query.message.reply_text(
                    convert_to_small_caps(
                        "**Timeout! No valid input received from SUDOERS. Process canceled.**"
                    )
                )
                return

    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")
        return

    # Step 3: Confirmation before saving
    try:
        confirmation = await app.ask(
            callback_query.message.chat.id,
            convert_to_small_caps(
                f"Do you want to save `{var_value}` for `{var_name}`?\nType 'yes' to confirm or 'no' to cancel."
            ),
            timeout=60,
        )

        # Check if the response is from SUDOERS
        if confirmation.from_user.id not in SUDOERS:
            await app.send_message(
                callback_query.message.chat.id,
                convert_to_small_caps(
                    "Only SUDOERS can confirm the input. Please try again."
                ),
            )
            return

        if confirmation.text.lower() == "yes":
            await save_new_variable_value(
                client, callback_query, app_name, var_name, var_value
            )
        else:
            await callback_query.message.reply_text(
                convert_to_small_caps(
                    f"Operation to add a new variable for app `{app_name}` canceled."
                )
            )
    except ListenerTimeout:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                "**Timeout! No valid confirmation received. Process canceled.**"
            )
        )
    except Exception as e:
        await callback_query.message.reply_text(f"An error occurred: {e}")


async def save_new_variable_value(
    client, callback_query, app_name, var_name, var_value
):
    # Step 4: Save the variable to Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: var_value},
    )

    if status == 200:
        await callback_query.message.reply_text(
            convert_to_small_caps(
                f"Variable `{var_name}` with value `{var_value}` saved successfully."
            )
        )
    else:
        await callback_query.message.reply_text(
            convert_to_small_caps(f"Failed to save variable: {result}")
        )


# Handle the callback when an app is selected for deletion
@app.on_callback_query(filters.regex(r"^delete_app:(.+)") & SUDOERS)
async def confirm_app_deletion(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Create confirmation buttons
    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Yes"), callback_data=f"confirm_delete:{app_name}"
            ),
            InlineKeyboardButton(
                convert_to_small_caps("No"), callback_data="cancel_delete"
            ),
        ],
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"show_apps"
            ),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Ask for confirmation
    await callback_query.message.edit_text(
        convert_to_small_caps(
            f"Are you sure you want to delete the app '{app_name}' from Heroku?"
        ),
        reply_markup=reply_markup,
    )


# Handle the confirmation for app deletion
@app.on_callback_query(filters.regex(r"^confirm_delete:(.+)") & SUDOERS)
async def delete_app_from_heroku(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    ok = await delete_app_info(callback_query.from_user.id, app_name)
    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"show_apps"
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Delete the app from Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}", HEROKU_API_KEY, method="delete"
    )

    if status == 200:
        # Delete the app from MongoDB database
        await callback_query.message.edit_text(
            convert_to_small_caps(f"✅ Successfully deleted '{app_name}' from Heroku."),
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.reply_text(
            convert_to_small_caps(f"Failed to delete app: {result}")
        )


# Handle the cancellation of app deletion
@app.on_callback_query(filters.regex(r"cancel_delete") & SUDOERS)
async def cancel_app_deletion(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton(
                convert_to_small_caps("Back"), callback_data=f"show_apps"
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text(
        convert_to_small_caps(f"App deletion canceled."), reply_markup=reply_markup
    )
