from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_GROUP_ID
from .. import app

async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, message: Message):
    if (await app.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        chat_id = message.chat.id
        new = f"**✫** <b><u>ɴᴇᴡ ɢʀᴏᴜᴘ</u></b> **:**\n\n**ᴄʜᴀᴛ ɪᴅ :** {chat_id}\n**ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :** {username}\n**ᴄʜᴀᴛ ᴛɪᴛʟᴇ :** {title}\n\n**ᴀᴅᴅᴇᴅ ʙʏ :** {added_by}"
        await new_message(LOG_GROUP_ID, new)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        chat_id = message.chat.id
        left = f"**✫** <b><u>ʟᴇғᴛ ɢʀᴏᴜᴘ</u></b> **:**\n\n**ᴄʜᴀᴛ ɪᴅ :** {chat_id}\n**ᴄʜᴀᴛ ᴛɪᴛʟᴇ :** {title}\n\n**ʀᴇᴍᴏᴠᴇᴅ ʙʏ :** {remove_by}"
        await new_message(LOG_GROUP_ID, left)