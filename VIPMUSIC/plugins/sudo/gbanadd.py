import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils import get_readable_time
from VIPMUSIC.utils.database import (
    add_banned_user,
    get_banned_count,
    get_banned_users,
    get_served_chats,
    is_banned_user,
    remove_banned_user,
)
from VIPMUSIC.utils.decorators.language import language
from config import BANNED_USERS
from datetime import datetime
import os
import random
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User


async def extract_user(m: Message) -> User:
    if m.reply_to_message:
        return m.reply_to_message.from_user
    msg_entities = m.entities[1] if m.text.startswith("/") else m.entities[0]
    return await app.get_users(
        msg_entities.user.id
        if msg_entities.type == MessageEntityType.TEXT_MENTION
        else int(m.command[1])
        if m.command[1].isdecimal()
        else m.command[1]
    )

@app.on_message(filters.command("rgban") & SUDOERS)
async def sgban(client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    msg = await message.reply("ᴜꜱᴇʀ ɪᴅ ᴀᴅᴅɪɴɢ ᴏɴ ɢʙᴀɴ ᴅʙ")
    await global_ban(client, message)

@app.on_message(filters.command("rungban") & SUDOERS)
async def sungban(client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    msg = await message.reply("ᴜꜱᴇʀ ɪᴅ ʀᴇᴍᴏᴠɪɴɢ ᴏɴ ɢʙᴀɴ ᴅʙ")
    await global_unban(client, message)



async def extract_user_info(client, user_id):
    try:
        if user_id.startswith('@'):
            user = await client.get_users(user_id)
            user_id = user.id
            mention = user.mention
            username = user.username if user.username else int(user.id)
        else:
            user = await client.get_users(int(user_id))
            first_name = user.first_name
            user_id = user.id
            username = user.username if user.username else int(user.id)
            mention = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
        return user_id, mention, username
    except ValueError:
        raise ValueError("Invalid user ID or username provided.")
    except Exception as e:
        raise e


async def global_ban(client, message: Message):
    try:
        user_id, reason = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("Please provide a user ID and a reason.")

    try:
        user_id, mention, username = await extract_user_info(client, user_id)
    except ValueError:
        return await message.reply_text("Invalid user ID or username provided.")
    except Exception as e:
        return await message.reply_text(f"An error occurred: {str(e)}")

    if user_id == message.from_user.id:
        return await message.reply_text("You cannot gban yourself.")
    elif user_id == app.id:
        return await message.reply_text("You cannot gban the bot.")
    elif user_id in SUDOERS:
        return await message.reply_text("You cannot gban a sudo user.")

    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return await message.reply_text(f"{mention} is already globally banned from the bot.")

    if user_id not in BANNED_USERS:
        BANNED_USERS.add(user_id)
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    gban_by = message.from_user.id
    await add_banned_user(user_id)
    await message.reply("ᴀᴅᴅᴇᴅ ᴅᴏɴᴇ ✅") 
    
   

async def global_unban(client, message: Message):
    try:
        user_id, reason = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("Please provide a user ID and a reason.")

    try:
        user_id, mention, username = await extract_user_info(client, user_id)
    except ValueError:
        return await message.reply_text("Invalid user ID or username provided.")
    except Exception as e:
        return await message.reply_text(f"An error occurred: {str(e)}")

    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await message.reply_text(f"{mention} is not globally banned from the bot.")

    if user_id in BANNED_USERS:
        BANNED_USERS.remove(user_id)
    await remove_banned_user(user_id)
    await message.reply("Unbanned ᴅᴏɴᴇ ✅") 
