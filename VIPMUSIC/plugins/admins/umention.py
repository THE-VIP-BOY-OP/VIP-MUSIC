import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter

SPAM_CHATS = {}

@app.on_message(filters.command(["utag", "uall"], prefixes=["/", "@", ".", "#"]) & admin_filter)
async def tag_all_users(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    text = message.text.split(None, 1)[1]
    SPAM_CHATS[chat_id] = True
    f = True
    while f:
        it SPAM_CHATS.get(message.chat.id) == False
            await message.reply_text("**ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")
            return
        usernum = 0
        usertxt = ""
        try:
            async for m in app.get_chat_members(message.chat.id):
                if m.user.is_bot:
                    continue
                usernum+= 1
                usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
                if usernum == 5:
                    await app.send_message(message.chat.id, f'{text}\n{usertxt}\n\n|| • ᴏғғ ᴠᴄᴛᴀɢ ʙʏ » /stoputag ||')
                    usernum = 0
                    usertxt = ""
                    await asyncio.sleep(2)
        except Exception as e:
            print(e)

@app.on_message(filters.command(["cancelutag", "canceluall", "utagcancel", "uallcancel", "stoputag", "stopuall", "offutag", "offuall", "utagoff", "ualloff"], prefixes=["/", ".", "@", "#"]) & admin_filter)
async def cancelcmd(_, message):
    global SPAM_CHATS
    chat_id = message.chat.id
    if SPAM_CHATS.get(chat_id) == True:
        SPAM_CHATS[chat_id] = False
        await message.reply_text("**ᴜɴʟɪᴍɪᴛᴇᴅ ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")
    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
            
