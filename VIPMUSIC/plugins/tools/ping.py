import requests
from pyrogram import filters
from pyrogram.types import Message
from datetime import datetime
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL

CARBON_API_URL = "https://carbonara.solopov.dev/api/cook"

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000

    # Prepare the code to be sent to Carbon
    code = f"""
from pyrogram import filters
from pyrogram.types import Message
from datetime import datetime
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await message.reply_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
"""

    # Carbon API Request payload
    payload = {
        "code": code,
        "backgroundColor": "white",
    }

    try:
        # Make the request to Carbon API
        response = requests.post(CARBON_API_URL, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Get the image URL from the response
        image_url = response.json().get("url")

        # Send the image URL as a reply
        await message.reply_text(f"Generated Carbon Image: {image_url}")

    except requests.exceptions.RequestException as e:
        print(f"Error making request to Carbon API: {e}")
        await message.reply_text("An error occurred while processing the image. Please try again.")
