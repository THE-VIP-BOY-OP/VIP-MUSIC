import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = []

@app.on_message(filters.command(["mentionall", "all", "djj"], prefixes=["/", "@", "#"]) & admin_filter)
async def tag_all_users(_, message):
    global SPAM_CHATS
    SPAM_CHATS.append(message.chat.id)
    text = message.text.split(None, 1)[1]
    while message.chat.id in SPAM_CHATS:
        usernum = 0
        usertxt = ""
        async for m in app.iter_chat_members(message.chat.id):
            if message.chat.id not in SPAM_CHATS:
                break
            if m.user.is_bot:
                continue
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(message.chat.id, f'{text}\n{usertxt}')
                usernum = 0
                usertxt = ""
                await asyncio.sleep(2)

@app.on_message(filters.command(["stopdj", "stopall", "cancelmention", "offmention", "mentionoff", "alloff", "cancelall", "allcancel"], prefixes=["/", "@", "#"]))
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        SPAM_CHATS.remove(chat_id)
        await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")
    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
            
