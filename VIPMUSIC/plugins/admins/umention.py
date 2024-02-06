import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter


SPAM_CHATS = []


@app.on_message(filters.command(["mentionall", "all", "djj"], prefixes=["/", "@", "#"]) & admin_filter)
async def tag_all_users(_,message): 

        text = message.text.split(None, 1)[1]
        
        SPAM_CHATS.append(message.chat.id)
        usernum= 0
        usertxt = ""
        async for m in app.get_chat_members(message.chat.id):       
            if message.chat.id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"\n⊚ [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 5:
                await app.send_message(message.chat.id,f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""


async def continuous_tag_all_users():
    while True:
        await tag_all_users()

        # Wait for 2 seconds before next Tag
        await asyncio.sleep(2)

# Start the continuous tagall loop if chat_id in spam_chat

if True:  
    asyncio.create_task(continuous_tag_all_users())
    
@app.on_message(filters.command(["stopdj", "stopall", "cancelmention", "offmention", "mentionoff", "alloff", "cancelall", "allcancel" ], prefixes=["/", "@", "#"]))
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass   
        return await message.reply_text("**ᴛᴀɢ ᴀʟʟ sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")     
                                     
    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")  
        return       
