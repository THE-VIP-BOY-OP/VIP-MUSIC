from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL
import aiohttp
from io import BytesIO
from VIPMUSIC import app
from pyrogram import filters



async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image

@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    captionss = "**🥀ᴘɪɴɢɪɴɢ ᴏᴜʀ sᴇʀᴠᴇʀ ᴡᴀɪᴛ...**"
    response = await message.reply_photo(PING_IMG_URL, caption=(captionsd))
    start = datetime.now()
    pytgping = await VIP.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    text =  _["ping_2"].format(resp, app.name, UP, RAM, CPU, DISK, pytgping)
    carbon = await make_carbon(text)
    captions = "**🏓 ᴘɪɴɢ...ᴘᴏɴɢ...ᴘɪɴɢ✨\n🎸 ᴅɪɴɢ...ᴅᴏɴɢ...ᴅɪɴɢ💞**"
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
