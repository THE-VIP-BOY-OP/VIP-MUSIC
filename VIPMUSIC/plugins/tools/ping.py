from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import requests

# ... (previous imports)

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    
    # Prepare the code to be sent to Carbon
    code = f"""Response Time: {resp} ms
UP: {UP} | RAM: {RAM} | CPU: {CPU} | DISK: {DISK}
Pyrogram Ping: {pytgping}"""

    # Carbon API endpoint
    carbon_api_url = "https://carbonara.solopov.dev/api/cook"

    # Request payload
    payload = {
        "code": code,
        "backgroundColor": "white",
        "theme": "seti",
        "dropShadow": True,
        "fontSize": 18,
        "lineNumbers": False,
        "watermark": False,
    }

    # Make the request to Carbon API
    response = requests.post(carbon_api_url, json=payload)

    # Save the image locally
    with open("carbon_ping_result.png", "wb") as f:
        f.write(response.content)

    # Send the image
    await message.reply_photo(photo="carbon_ping_result.png", caption="Ping results drawn on Carbon with colorful text")
