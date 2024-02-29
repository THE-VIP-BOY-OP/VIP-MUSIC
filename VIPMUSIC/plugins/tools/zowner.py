from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app
from VIPMUSIC.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.database import get_assistant
import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from VIPMUSIC.utils.database import get_assistant, is_active_chat

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    userbot = await get_assistant(chat_id)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

# --------------------------------------------------------------------------------- #

@app.on_message(filters.command(["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"] ,prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.group)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)


# --------------------------------------------------------------------------------- #




from pyrogram import filters
import time

@app.on_message(filters.command(["addbots", f"addbots@{app.username}"]) & SUDOERS)
async def add_all(client, message):
    command_parts = message.text.split(" ")
    if len(command_parts) != 2:
        await message.reply("Invalid command format. Please use: /addbots @bot_username")
        return
    
    bot_username = command_parts[1]
    try:
        userbot = await get_assistant(message.chat.id)
        app_id = (await app.get_users(bot_username)).id
        done = 0
        failed = 0
        lol = await message.reply("🔄 **Adding bot in all chats!**")
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == -1001733534088:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                await lol.edit(
                    f"**Adding {bot_username} in chats.\n\n**✅ Added in: {done} chats**\n**❌ Failed in {failed} chats.**\n\n**⏲️ Time taken:** {time.time()}"
                )
            except Exception as e:
                failed += 1
                await lol.edit(
                    f"**Adding {bot_username} in chats.\n\n**✅ Added in: {done} chats**\n**❌ Failed in {failed} chats.**\n\n**⏲️ Time taken:** {time.time()}"
                )
            await asyncio.sleep(2)  # Adjust sleep time based on rate limits
        
        await lol.edit(
            f"**🎉 {bot_username} Bot Added Successfully.**\n\n**✅ Added in {done} chats.**\n**❌ Failed in {failed} chats.**\n\n**⏲️ Time taken:** {time.time()}"
        )
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
