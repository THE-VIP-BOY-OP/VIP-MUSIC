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



@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    
    # Create a blank image
    image = Image.new("RGB", (600, 400), color="white")
    draw = ImageDraw.Draw(image)
    
    # Load a font (adjust the path accordingly)
    font = ImageFont.load_default()

    # Draw ping results on the image with colorful text
    draw.text((10, 10), f"Response Time: {resp} ms", fill=(255, 0, 0), font=font)  # Red text
    draw.text((10, 30), f"UP: {UP} | RAM: {RAM} | CPU: {CPU} | DISK: {DISK}", fill=(0, 255, 0), font=font)  # Green text
    draw.text((10, 50), f"Pyrogram Ping: {pytgping}", fill=(0, 0, 255), font=font)  # Blue text

    # Save the image
    image.save("ping_result_colorful.png")

    # Send the image
    await message.reply_photo(photo="ping_result_colorful.png", caption="Colorful Ping results drawn on Carbon")
