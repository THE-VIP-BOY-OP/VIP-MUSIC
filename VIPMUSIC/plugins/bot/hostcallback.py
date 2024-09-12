import asyncio
import os

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


from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@app.on_callback_query(filters.regex("show_apps") & SUDOERS)
async def show_apps(client, callback_query):
    apps = await fetch_apps()

    if not apps:
        await callback_query.message.edit_text("No apps found on Heroku.")
        return

    # Create buttons for each app and a 'Back' button
    buttons = [
        [InlineKeyboardButton(app["name"], callback_data=f"app:{app['name']}")]
        for app in apps
    ]

    # Add the 'Back' button as a new row
    buttons.append([InlineKeyboardButton("Back", callback_data="main_menu")])

    # Send the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text(
        "Select your app from given below app list to handle:",
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^main_menu$") & SUDOERS)
async def main_menu(client, callback_query):
    buttons = [
        [InlineKeyboardButton("Show Deployed Apps", callback_data="show_apps")],
        # Add other menu options here
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        "Main menu. Choose an option:", reply_markup=reply_markup
    )


# Handle app-specific options (Edit / Logs / Restart Dynos)
# Handle app-specific options (Edit / Logs / Restart Dynos / Manage Dynos)
@app.on_callback_query(filters.regex(r"^app:(.+)") & SUDOERS)
async def app_options(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                "Edit Variables", callback_data=f"edit_vars:{app_name}"
            ),
            InlineKeyboardButton("Get Logs", callback_data=f"get_logs:{app_name}"),
        ],
        [
            InlineKeyboardButton(
                "Restart All Dynos", callback_data=f"restart_dynos:{app_name}"
            ),
            InlineKeyboardButton(
                "Manage Dynos", callback_data=f"manage_dynos:{app_name}"
            ),
        ],
        [
            InlineKeyboardButton("Back", callback_data="show_apps"),
            InlineKeyboardButton("Delete Host", callback_data=f"delete_app:{app_name}"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Tap on the given buttons to edit or get logs of {app_name} app from Heroku.",
        reply_markup=reply_markup,
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
        await callback_query.answer("Getting Logs...", show_alert=True)
        await callback_query.message.reply_text(
            f"**Here are the latest logs for** {app_name}:\n{paste_url}"
        )
    else:
        await callback_query.message.reply_text(
            f"**Failed to retrieve logs for** {app_name}: {result}"
        )


# Manage Dynos
@app.on_callback_query(filters.regex(r"^manage_dynos:(.+)") & SUDOERS)
async def manage_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [InlineKeyboardButton("Turn On Dynos", callback_data=f"dyno_on:{app_name}")],
        [InlineKeyboardButton("Turn Off Dynos", callback_data=f"dyno_off:{app_name}")],
        [InlineKeyboardButton("Back", callback_data=f"app:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        "Choose an action for your dynos:", reply_markup=reply_markup
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
        [InlineKeyboardButton("Back", callback_data=f"manage_dynos:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            f"Dynos for app `{app_name}` turned on successfully.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            f"Failed to turn on dynos: {result}", reply_markup=reply_markup
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
        [InlineKeyboardButton("Back", callback_data=f"manage_dynos:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            f"Dynos for app `{app_name}` turned off successfully.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            f"Failed to turn off dynos: {result}", reply_markup=reply_markup
        )


# Restart All Dynos
@app.on_callback_query(filters.regex(r"^restart_dynos:(.+)") & SUDOERS)
async def restart_dynos(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    status, result = make_heroku_request(
        f"apps/{app_name}/dynos", HEROKU_API_KEY, method="delete"
    )

    if status == 202:
        await callback_query.answer("Restarting All Dynos...", show_alert=True)
        await callback_query.message.reply_text(
            f"Restarting all dynos for app `{app_name}`..."
        )
    else:
        await callback_query.message.edit_text(f"Failed to restart dynos: {result}")


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

    # Debugging output
    print(f"Status: {status}, Response: {response}")

    # Check if the response is successful and contains environment variables
    if status == 200 and isinstance(response, dict):
        if response:
            # Create buttons for each environment variable
            buttons = [
                [
                    InlineKeyboardButton(
                        var_name, callback_data=f"edit_var:{app_name}:{var_name}"
                    )
                ]
                for var_name in response.keys()
            ]

            # Add an option to add new variables and a back button
            buttons.append(
                [
                    InlineKeyboardButton(
                        "➕ Add New Variable ➕", callback_data=f"add_var:{app_name}"
                    )
                ]
            )
            buttons.append(
                [InlineKeyboardButton("Back", callback_data=f"app:{app_name}")]
            )

            reply_markup = InlineKeyboardMarkup(buttons)

            # Send the buttons to the user
            await callback_query.message.edit_text(
                "Select a variable to edit:", reply_markup=reply_markup
            )
        else:
            await callback_query.message.edit_text(
                "No environment variables found for this app."
            )
    else:
        await callback_query.message.edit_text(
            f"Failed to fetch environment variables. Status: {status}, Response: {response}"
        )


@app.on_callback_query(filters.regex(r"^edit_var:(.+):(.+)") & SUDOERS)
async def edit_variable_options(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    buttons = [
        [
            InlineKeyboardButton(
                "Edit", callback_data=f"edit_var_value:{app_name}:{var_name}"
            )
        ],
        [
            InlineKeyboardButton(
                "Delete", callback_data=f"delete_var:{app_name}:{var_name}"
            )
        ],
        [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Choose an option for the variable `{var_name}`:", reply_markup=reply_markup
    )


# Step 1: Ask for the new value and then confirm with the user
temporary_var_storage = {}


@app.on_callback_query(filters.regex(r"^edit_var_value:(.+):(.+)") & SUDOERS)
async def edit_variable_value(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]
    try:
        new_value = None

        async def check_sudo_responses():
            nonlocal new_value
            while True:
                try:
                    buttons = [
                        [
                            InlineKeyboardButton(
                                "Cancel", callback_data=f"cancel_save_var:{app_name}"
                            ),
                        ]
                    ]

                    reply_markup = InlineKeyboardMarkup(buttons)
                    response = await app.ask(
                        callback_query.message.chat.id,
                        f"**Send the new value for** `{var_name}` **within 1 min:**",
                        reply_markup=reply_markup,
                        timeout=60,
                    )

                    if response.from_user.id in SUDOERS:
                        new_value = response.text
                        break
                except ListenerTimeout:
                    return await callback_query.message.reply_text(
                        "**Timeout! No valid response received.**",
                        reply_markup=reply_markup,
                    )

        await asyncio.wait_for(check_sudo_responses(), timeout=60)

        if not new_value:
            return await callback_query.message.reply_text(
                "**No valid SUDOER response received.**", reply_markup=reply_markup
            )

        # Generate a unique ID for this transaction
        transaction_id = f"{app_name}:{var_name}"

        # Store the new value in the temporary storage
        temporary_var_storage[transaction_id] = new_value

    except ListenerTimeout:
        return await callback_query.message.reply_text(
            "**Timeout! Restart the process again.**", reply_markup=reply_markup
        )

    # Ask for confirmation
    buttons = [
        [
            InlineKeyboardButton(
                "Yes", callback_data=f"confirm_save_var:{transaction_id}"
            ),
            InlineKeyboardButton(
                "No", callback_data=f"cancel_save_var:{transaction_id}"
            ),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.reply_text(
        f"**Do you want to save the new value** `{new_value}` **for** `{var_name}`?",
        reply_markup=reply_markup,
    )


@app.on_callback_query(filters.regex(r"^confirm_save_var:(.+)") & SUDOERS)
async def confirm_save_variable(client, callback_query):
    transaction_id = callback_query.data.split(":")[1]

    try:
        # Validate and unpack transaction_id
        app_name, var_name = transaction_id.split(":")

        # Retrieve the stored value
        if transaction_id in temporary_var_storage:
            new_value = temporary_var_storage[transaction_id]

            # Logic to save the variable in Heroku
            status, result = make_heroku_request(
                f"apps/{app_name}/config-vars",
                HEROKU_API_KEY,
                method="patch",
                payload={var_name: new_value},
            )

            # Clean up the temporary storage
            del temporary_var_storage[transaction_id]

            await callback_query.message.reply_text(
                f"**Successfully saved the new value** `{new_value}`."
            )
        else:
            await callback_query.message.reply_text(
                "**Error: The new value could not be found.**"
            )
    except ValueError as e:
        await callback_query.message.reply_text(
            f"**Error: Invalid transaction ID format.** {str(e)}"
        )
    except Exception as e:
        await callback_query.message.reply_text(
            f"**Unexpected error occurred.** {str(e)}"
        )


@app.on_callback_query(filters.regex(r"^cancel_save_var:(.+)") & SUDOERS)
async def cancel_save_variable(client, callback_query):
    transaction_id = callback_query.data.split(":")[1]

    try:
        # Validate and unpack transaction_id
        app_name, var_name = transaction_id.split(":")

        # Remove the new value from the temporary storage if present
        if transaction_id in temporary_var_storage:
            del temporary_var_storage[transaction_id]

        # "Back" button to return to the variable editing options
        buttons = [
            [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        await callback_query.message.edit_text(
            f"Edit operation for `{var_name}` in app `{app_name}` canceled.",
            reply_markup=reply_markup,
        )
    except ValueError as e:
        await callback_query.message.reply_text(
            f"**Error: Invalid transaction ID format.** {str(e)}"
        )
    except Exception as e:
        await callback_query.message.reply_text(
            f"**Unexpected error occurred.** {str(e)}"
        )


# Step 1: Confirmation before deleting a variable
@app.on_callback_query(filters.regex(r"^delete_var:(.+):(.+)") & SUDOERS)
async def delete_variable_confirmation(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    # Ask for confirmation to delete
    buttons = [
        [
            InlineKeyboardButton(
                "Yes", callback_data=f"confirm_delete_var:{app_name}:{var_name}"
            ),
            InlineKeyboardButton("No", callback_data=f"cancel_delete_var:{app_name}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"**Are you sure you want to delete the variable** `{var_name}`?",
        reply_markup=reply_markup,
    )


# Step 2: If the user clicks Yes, delete the variable
@app.on_callback_query(filters.regex(r"^confirm_delete_var:(.+):(.+)") & SUDOERS)
async def confirm_delete_variable(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    # Delete the variable from Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: None},  # Setting to None removes the variable
    )

    # Create a "Back" button to return to the variable list
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            f"**Variable** `{var_name}` **deleted successfully from** `{app_name}`.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            f"**Failed to delete variable:** {result}", reply_markup=reply_markup
        )


# Step 3: If the user clicks No, cancel the delete operation
@app.on_callback_query(filters.regex(r"^cancel_delete_var:(.+)") & SUDOERS)
async def cancel_delete_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Create a "Back" button to return to the variable list
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"**Delete operation for app `{app_name}` canceled.**",
        reply_markup=reply_markup,
    )


# Add New Variable
@app.on_callback_query(filters.regex(r"^add_var:(.+)") & SUDOERS)
async def add_new_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    try:
        # Ask for variable name
        response = await app.ask(
            callback_query.message.chat.id,
            "Please send me the new variable name:",
            timeout=60,
        )

        # Ensure that only SUDOERS can respond
        if response.from_user.id not in SUDOERS:
            return await callback_query.message.reply_text(
                "**You are not authorized to perform this action.**"
            )

        var_name = response.text

        # Ask for variable value
        response = await app.ask(
            callback_query.message.chat.id,
            f"Now send me the value for `{var_name}`:",
            timeout=60,
        )

        # Ensure that only SUDOERS can respond
        if response.from_user.id not in SUDOERS:
            return await callback_query.message.reply_text(
                "**You are not authorized to perform this action.**"
            )

        var_value = response.text
    except ListenerTimeout:
        return await callback_query.message.reply_text(
            "**Timeout! Restart the process again.**"
        )

    # Ask for confirmation
    buttons = [
        [
            InlineKeyboardButton(
                "Yes",
                callback_data=f"confirm_add_var:{app_name}:{var_name}:{var_value}",
            ),
            InlineKeyboardButton("No", callback_data=f"cancel_add_var:{app_name}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.reply_text(
        f"**Do you want to add the new variable** `{var_name}` **with value** `{var_value}`?",
        reply_markup=reply_markup,
    )


# Save Variable
@app.on_callback_query(filters.regex(r"^save_var:(.+):(.+):(.+)") & SUDOERS)
async def save_new_variable(client, callback_query):
    app_name, var_name, var_value = callback_query.data.split(":")[1:4]

    # Save the variable to Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: var_value},
    )

    if status == 200:
        await callback_query.message.edit_text(
            f"Variable `{var_name}` with value `{var_value}` saved successfully."
        )
    else:
        await callback_query.message.edit_text(f"Failed to save variable: {result}")


# Handle the callback when an app is selected for deletion
@app.on_callback_query(filters.regex(r"^delete_app:(.+)") & SUDOERS)
async def confirm_app_deletion(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Create confirmation buttons
    buttons = [
        [
            InlineKeyboardButton("Yes", callback_data=f"confirm_delete:{app_name}"),
            InlineKeyboardButton("No", callback_data="cancel_delete"),
        ],
        [
            InlineKeyboardButton("Back", callback_data=f"app"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Ask for confirmation
    await callback_query.message.edit_text(
        f"Are you sure you want to delete the app '{app_name}' from Heroku?",
        reply_markup=reply_markup,
    )


# Handle the confirmation for app deletion
@app.on_callback_query(filters.regex(r"^confirm_delete:(.+)") & SUDOERS)
async def delete_app_from_heroku(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    ok = await delete_app_info(callback_query.from_user.id, app_name)
    buttons = [
        [
            InlineKeyboardButton("Back", callback_data=f"show_apps"),
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
            f"✅ Successfully deleted '{app_name}' from Heroku.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.reply_text(f"Failed to delete app: {result}")


# Handle the cancellation of app deletion
@app.on_callback_query(filters.regex(r"cancel_delete") & SUDOERS)
async def cancel_app_deletion(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("Back", callback_data=f"delete_app"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text(
        f"App deletion canceled.", reply_markup=reply_markup
    )
