import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from datetime import datetime


import asyncio
from pyrogram import Client, filters
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = {}

async def mention_all(chat_id, message, userlist):
    usernum = 0
    usertxt = ""
    async for m in app.iter_chat_members(chat_id):
        if m.user.id in userlist:
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(chat_id, f"{message}\n{usertxt}")
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""

async def mention_all_users(message, userlist):
    replied = message.reply_to_message
    text = message.text.split(None, 1)[1] if len(message.command) > 1 else None

    if not replied and not text:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ**")
        return

    while SPAM_CHATS.get(message.chat.id, False):
        if replied:
            await mention_all(message.chat.id, replied.text, userlist)
        else:
            await mention_all(message.chat.id, text, userlist)
        await asyncio.sleep(2)

@app.on_message(filters.command(["okstart", "aljl", "menition"], prefixes=["/", "@", "#"]) & admin_filter)
async def tag_all_users(_, message):
    replied = message.reply_to_message

    if replied:
        userlist = []
        async for m in app.iter_chat_members(message.chat.id):
            userlist.append(m.user.id)
        SPAM_CHATS[message.chat.id] = True
        await mention_all_users(message, userlist)

    else:
        await message.reply_text("**Reply to a message to mention all members.**")

@app.on_message(filters.command(["okruko", "stopaljl", "cancelmuention", "offmentjion", "mentionojff", "alljoff", "canceljall", "allcanucel"], prefixes=["/", "@", "#"]))
async def cancelcmd(_, message):
    chat_id = message.chat.id

    if chat_id in SPAM_CHATS:
        del SPAM_CHATS[chat_id]
        await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        
