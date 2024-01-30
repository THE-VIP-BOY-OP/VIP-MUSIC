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



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    out = private_panel(_)
    m = await message.reply_text("**๏**")  # Displaying animation
    await asyncio.sleep(0.1)
    await m.edit_text("**๏ s**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙᴏ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ.**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ...**")
                await asyncio.sleep(0.1)
                await m.edit_text("**๏ sᴛᴀʀᴛɪɴɢ ʙᴏᴛ.**")
                await asyncio.sleep(0.1)
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


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
