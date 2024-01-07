from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS
import aiohttp
import asyncio
from io import BytesIO
from PIL import Image, ImageEnhance
import requests

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            image = BytesIO(await resp.read())
    return image

async def enhance_image(image):
    # Open the image using Pillow
    img = Image.open(image)
    
    # Increase brightness
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.5)  # Adjust the factor as needed
    
    # Save the image to a BytesIO object
    enhanced_image = BytesIO()
    img.save(enhanced_image, format='PNG', quality=95)  # Adjust the quality as needed
    enhanced_image.seek(0)
    
    return enhanced_image

async def make_carbon(code, quality=100):
    url = "https://carbonara.solopov.dev/api/cook"
    
    # Add quality parameter to the JSON payload
    payload = {"code": code, "quality": quality}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as resp:
            image = BytesIO(await resp.read())
    
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    PING_IMG_URL = "https://telegra.ph/file/7bb907999ea7156227283.jpg"
    
    # Download the image
    image = await download_image(PING_IMG_URL)
    
    # Enhance the image (increase brightness)
    enhanced_image = await enhance_image(image)
    
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ.**"
    response = await message.reply_photo(enhanced_image, caption=(captionss))
    
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    
    # Generate Carbon image with increased quality
    carbon = await make_carbon(text, quality=90)
    
    captions = "**ㅤ  🏓 ᴘɪɴɢ...ᴘᴏɴɢ...ᴘɪɴɢ✨\nㅤ  🎸 ᴅɪɴɢ...ᴅᴏɴɢ...ᴅɪɴɢ💞**"
    await message.reply_photo((carbon), caption=captions,
                              reply_markup=InlineKeyboardMarkup(
                                  [
                                      [
                                          InlineKeyboardButton(
                                              text=_["S_B_5"],
                                              url=f"https://t.me/{app.username}?startgroup=true",
                                          )

                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text="✦ ɢʀᴏᴜᴘ ✦", url=f"https://t.me/TG_FRIENDSS",
                                          ),
                                          InlineKeyboardButton(
                                              text="✧ ᴍᴏʀᴇ ✧", url=f"https://t.me/VIP_CREATORS",
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text="❅ ʜᴇʟᴘ ❅", callback_data="settings_back_helper"
                                          )
                                      ],
                                  ]
                              ),
                              )
    await response.delete()
