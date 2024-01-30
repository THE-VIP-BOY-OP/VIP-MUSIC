import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import asyncio
import config
from VIPMUSIC import app
from VIPMUSIC.misc import _boot_
from VIPMUSIC.plugins.sudo.sudoers import sudoers_list
from VIPMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from VIPMUSIC.utils.decorators.language import LanguageStart
from VIPMUSIC.utils.formatters import get_readable_time
from VIPMUSIC.utils.inline import first_page, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



YUMI_PICS = [
"https://telegra.ph/file/3ed81ef4e352a691fb0b4.jpg",
"https://telegra.ph/file/3134ed3b57eb051b8c363.jpg",
"https://telegra.ph/file/6ca0813b719b6ade1c250.jpg",
"https://telegra.ph/file/5a2cbb9deb62ba4b122e4.jpg",
"https://telegra.ph/file/cb09d52a9555883eb0f61.jpg"

]


...

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    try:
        await add_served_user(message.from_user.id)
        out = private_panel(_)
        m = await message.reply_text("**๏**")  # Displaying animation
        
        await asyncio.sleep(1)  # Adjust sleep duration if necessary
        
        text_to_edit = ["**๏ s**", "**๏ sᴛ**", "**๏ sᴛᴀ**", "**๏ sᴛᴀʀ**", "**๏ sᴛᴀʀᴛ**",
                        "**๏ sᴛᴀʀᴛɪ**", "**๏ sᴛᴀʀᴛɪɴ**", "**๏ sᴛᴀʀᴛɪɴɢ**", "**๏ sᴛᴀʀᴛɪɴɢ ʙ**",
                        "**๏ sᴛᴀʀᴛɪɴɢ ʙᴏ**", "**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ**", "**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ.**",
                        "**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ...**", "**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ.**"]
        
        for text in text_to_edit:
            await m.edit_text(text)
            await asyncio.sleep(0.1)  # Adjust sleep duration if necessary
        
        await m.delete()  # Delete animation message
        
        await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_2"].format(message.from_user.mention, app.mention),
            reply_markup=InlineKeyboardMarkup(out),
        )
        
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )
    except Exception as e:
        print(f"Error in start_pm: {e}")

...

@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    try:
        await add_served_user(message.from_user.id)
        if len(message.text.split()) > 1:
            name = message.text.split(None, 1)[1]
            if name[0:4] == "help":
                keyboard = first_page(_)
                return await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["help_1"].format(config.SUPPORT_CHAT),
                    reply_markup=keyboard,
                )
            if name[0:3] == "sud":
                await sudoers_list(client=client, message=message, _=_)
                if await is_on_off(2):
                    return await app.send_message(
                        chat_id=config.LOGGER_ID,
                        text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                    )
                return
            if name[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(name)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = _["start_6"].format(
                    title, duration, views, published, channellink, channel, app.mention
                )
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text=_["S_B_8"], url=link),
                            InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                        ],
                    ]
                )
                await m.delete()
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    reply_markup=key,
                )

            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )

