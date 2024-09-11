import os
import socket

import requests
import urllib3
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app
from VIPMUSIC.utils.database import (
    delete_app_info,
    delete_handler,
    get_all_handlers,
    get_app_info,
    save_handler,
)

# Import your MongoDB database structure
from VIPMUSIC.utils.pastebin import VIPbin

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEROKU_API_URL = "https://api.heroku.com"
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
REPO_URL = "https://github.com/THE-VIP-BOY-OP/VIP-MUSIC"
BUILDPACK_URL = "https://github.com/heroku/heroku-buildpack-python"


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


@app.on_callback_query(filters.regex(r"^show_apps$"))
async def show_deployed_apps(client, callback_query):
    apps = await get_app_info(callback_query.from_user.id)

    if apps:
        buttons = [
            [InlineKeyboardButton(app_name, callback_data=f"app:{app_name}")]
            for app_name in apps
        ]
        # Add a "Back" button to navigate back to a previous menu if needed
        buttons.append([InlineKeyboardButton("Back", callback_data="main_menu")])

        reply_markup = InlineKeyboardMarkup(buttons)
        await callback_query.message.edit_text(
            "**Click the buttons below to check your bots hosted on Heroku.**",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text("**You have not deployed any bots**")


@app.on_callback_query(filters.regex(r"^main_menu$"))
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
@app.on_callback_query(filters.regex(r"^app:(.+)"))
async def app_options(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [
            InlineKeyboardButton(
                "Manage Handlers", callback_data=f"manage_handlers:{app_name}"
            )
        ],
        [InlineKeyboardButton("Edit Variables", callback_data=f"edit_vars:{app_name}")],
        [InlineKeyboardButton("Get Logs", callback_data=f"get_logs:{app_name}")],
        [
            InlineKeyboardButton(
                "Restart All Dynos", callback_data=f"restart_dynos:{app_name}"
            )
        ],
        [
            InlineKeyboardButton(
                "Manage Dynos", callback_data=f"manage_dynos:{app_name}"
            )
        ],
        [InlineKeyboardButton("Back", callback_data="back_to_apps")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Tap on the given buttons to manage or check your app **{app_name}**.",
        reply_markup=reply_markup,
    )


# Manage Dynos
@app.on_callback_query(filters.regex(r"^manage_dynos:(.+)"))
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
@app.on_callback_query(filters.regex(r"^dyno_on:(.+)"))
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
@app.on_callback_query(filters.regex(r"^dyno_off:(.+)"))
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
        await callback_query.message.edit_text(f"Failed to restart dynos: {result}")


# Handle Back Button
@app.on_callback_query(filters.regex(r"back_to_apps"))
async def back_to_apps(client, callback_query):
    await get_deployed_apps(client, callback_query.message)


# Edit Environment Variables


@app.on_callback_query(filters.regex(r"^edit_vars:(.+)"))
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
                        "Add New Variable", callback_data=f"add_var:{app_name}"
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


@app.on_callback_query(filters.regex(r"^edit_var:(.+):(.+)"))
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
@app.on_callback_query(filters.regex(r"^edit_var_value:(.+):(.+)"))
async def edit_variable_value(client, callback_query):
    app_name, var_name = callback_query.data.split(":")[1:3]

    # Ask the user for a new value
    response = await app.ask(
        callback_query.message.chat.id,
        f"Send the new value for `{var_name}`:",
        timeout=60,
    )
    new_value = response.text

    # Step 2: Ask for confirmation
    buttons = [
        [
            InlineKeyboardButton(
                "Yes",
                callback_data=f"confirm_save_var:{app_name}:{var_name}:{new_value}",
            ),
            InlineKeyboardButton("No", callback_data=f"cancel_save_var:{app_name}"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Do you want to save the new value `{new_value}` for `{var_name}`?",
        reply_markup=reply_markup,
    )


# Step 3: If the user clicks Yes, save the new value
@app.on_callback_query(filters.regex(r"^confirm_save_var:(.+):(.+):(.+)"))
async def confirm_save_variable(client, callback_query):
    app_name, var_name, new_value = callback_query.data.split(":")[1:4]

    # Save the variable to Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}/config-vars",
        HEROKU_API_KEY,
        method="patch",
        payload={var_name: new_value},
    )

    # Create a "Back" button that takes the user back to the variable editing options
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    if status == 200:
        await callback_query.message.edit_text(
            f"Variable `{var_name}` updated successfully to `{new_value}`.",
            reply_markup=reply_markup,
        )
    else:
        await callback_query.message.edit_text(
            f"Failed to update variable: {result}", reply_markup=reply_markup
        )


# Step 4: If the user clicks No, cancel the operation
@app.on_callback_query(filters.regex(r"^cancel_save_var:(.+)"))
async def cancel_save_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Create a "Back" button that takes the user back to the variable editing options
    buttons = [
        [InlineKeyboardButton("Back", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Edit operation for app `{app_name}` canceled.", reply_markup=reply_markup
    )


# Manage Handlers Page


@app.on_callback_query(filters.regex(r"^manage_handlers:(.+)"))
async def manage_handlers(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    buttons = [
        [InlineKeyboardButton("Add Handler", callback_data=f"add_handler:{app_name}")],
        [
            InlineKeyboardButton(
                "Check Handlers", callback_data=f"check_handlers:{app_name}"
            )
        ],
        [
            InlineKeyboardButton(
                "Remove Handler", callback_data=f"remove_handler:{app_name}"
            )
        ],
        [InlineKeyboardButton("Back", callback_data=f"app:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.edit_text(
        f"Manage handlers for **{app_name}**.", reply_markup=reply_markup
    )


# Add handler prompt
@app.on_callback_query(filters.regex(r"^add_handler:(.+)"))
async def add_handler_prompt(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Get the list of handlers
    handlers = await get_all_handlers(app_name)

    # Check if there are any handlers
    if not handlers:
        await callback_query.message.reply_text("No handlers found for this app, Adding..")
        

    # Check if the user is the first handler (the host)
    if callback_query.from_user.id != handlers[0]:  # First handler is the host
        await callback_query.message.reply_text("Only the host can add new handlers.")
        return

    try:
        # Prompt the user for the new handler's user ID
        response = await app.ask(
            callback_query.message.chat.id,
            "Send the user ID of the handler to add:",
            timeout=300,
        )
        new_handler_id = int(response.text)

        # Check if the user ID is already in the handlers list
        if new_handler_id in handlers:
            await callback_query.message.reply_text(
                "This user is already in the handler list."
            )
            return

        # Save the new handler
        await save_handler(app_name, new_handler_id)
        await callback_query.message.reply_text(
            f"Handler with user ID {new_handler_id} has been added successfully."
        )

    except ListenerTimeout:
        await callback_query.message.reply_text(
            "Timeout! Please try adding the handler again."
        )


# Check Handlers
@app.on_callback_query(filters.regex(r"^check_handlers:(.+)"))
async def check_handlers(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    handlers = await get_all_handlers(app_name)

    if not handlers:
        await callback_query.message.edit_text("**No handlers found for this app.**")
        return

    handler_list = "\n".join(
        [f"- [{handler}](tg://user?id={handler})" for handler in handlers]
    )

    await callback_query.message.edit_text(
        f"**Handlers for {app_name}:**\n\n{handler_list}", disable_web_page_preview=True
    )


# Remove Handler Prompt
@app.on_callback_query(filters.regex(r"^remove_handler:(.+)"))
async def remove_handler_prompt(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    handlers = await get_all_handlers(app_name)

    if not handlers:
        await callback_query.message.edit_text("**No handlers found for this app.**")
        return

    handler_list = "\n".join([f"- `{handler}`" for handler in handlers])

    await callback_query.message.edit_text(
        f"**Handlers for {app_name}:**\n\n{handler_list}\n\n"
        "**Send the user ID to remove from the handler list:**"
    )

    try:
        response = await app.ask(
            callback_query.message.chat.id,
            "**Enter the user ID of the handler to remove:**",
            timeout=300,
        )
        handler_id_to_remove = int(response.text)
    except ListenerTimeout:
        await callback_query.message.reply_text("**Timeout! Please try again.**")
        return

    # Check if the user is trying to remove the first handler (the host)
    if handler_id_to_remove == handlers[0]:
        await callback_query.message.reply_text("**You cannot remove the app host!**")
        return

    # Check if the handler exists in the list
    if handler_id_to_remove not in handlers:
        await callback_query.message.reply_text(
            "**This user is not in the handler list.**"
        )
    else:
        # Remove the handler
        await delete_handler(app_name, handler_id_to_remove)
        await callback_query.message.reply_text(
            f"**User {handler_id_to_remove} has been removed from the handler list.**"
        )


# Step 1: Confirmation before deleting a variable
@app.on_callback_query(filters.regex(r"^delete_var:(.+):(.+)"))
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

    await callback_query.message.reply_text(
        f"**Are you sure you want to delete the variable** `{var_name}`?",
        reply_markup=reply_markup,
    )


# Step 2: If the user clicks Yes, delete the variable
@app.on_callback_query(filters.regex(r"^confirm_delete_var:(.+):(.+)"))
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
@app.on_callback_query(filters.regex(r"^cancel_delete_var:(.+)"))
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
@app.on_callback_query(filters.regex(r"^add_var:(.+)"))
async def add_new_variable(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Ask for variable name
    response = await app.ask(
        callback_query.message.chat.id,
        "Please send me the new variable name:",
        timeout=60,
    )
    var_name = response.text

    # Ask for variable value
    response = await app.ask(
        callback_query.message.chat.id,
        f"Now send me the value for `{var_name}`:",
        timeout=60,
    )
    var_value = response.text

    # Confirmation before saving
    buttons = [
        [
            InlineKeyboardButton(
                "Yes", callback_data=f"save_var:{app_name}:{var_name}:{var_value}"
            )
        ],
        [InlineKeyboardButton("No", callback_data=f"edit_vars:{app_name}")],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    await callback_query.message.reply_text(
        f"Do you want to save `{var_value}` for `{var_name}`?",
        reply_markup=reply_markup,
    )


# Save Variable
@app.on_callback_query(filters.regex(r"^save_var:(.+):(.+):(.+)"))
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
@app.on_callback_query(filters.regex(r"^delete_app:(.+)"))
async def confirm_app_deletion(client, callback_query):
    app_name = callback_query.data.split(":")[1]

    # Create confirmation buttons
    buttons = [
        [
            InlineKeyboardButton("Yes", callback_data=f"confirm_delete:{app_name}"),
            InlineKeyboardButton("No", callback_data="cancel_delete"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)

    # Ask for confirmation
    await callback_query.message.edit_text(
        f"Are you sure you want to delete the app '{app_name}' from Heroku?",
        reply_markup=reply_markup,
    )


# Handle the confirmation for app deletion
@app.on_callback_query(filters.regex(r"^confirm_delete:(.+)"))
async def delete_app_from_heroku(client, callback_query):
    app_name = callback_query.data.split(":")[1]
    ok = await delete_app_info(callback_query.from_user.id, app_name)

    # Delete the app from Heroku
    status, result = make_heroku_request(
        f"apps/{app_name}", HEROKU_API_KEY, method="delete"
    )

    if status == 200:
        # Delete the app from MongoDB database

        await callback_query.message.edit_text(
            f"Successfully deleted '{app_name}' from Heroku.\nCheck by:- /myhost"
        )
    else:
        await callback_query.message.edit_text(f"Failed to delete app: {result}")


# Handle the cancellation of app deletion
@app.on_callback_query(filters.regex(r"cancel_delete"))
async def cancel_app_deletion(client, callback_query):
    buttons = [
        [
            InlineKeyboardButton("Back", callback_data=f"delete_app"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit_text(f"App deletion canceled.")
