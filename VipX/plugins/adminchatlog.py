from pyrogram import Client, filters
from pyrogram.types import Message
from config import LOG_GROUP_ID
from .. import app
from VipX import app

async def new_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)

@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, message: Message):
    if (await app.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        link = await app.export_chat_invite_link(message.chat.id)
        new = f"**✫** <b><u>#𝐍ᴇᴡ_𝐀ᴅᴍɪɴ_𝐆ʀᴏᴜᴘ</u></b> **✫**\n\n**𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ :** {title}\n\n**𝐂ʜᴀᴛ 𝐋ɪɴᴋ :** [𝐂ʟɪᴄᴋ 𝐇ᴇʀᴇ]({link}) "
        await new_message(LOG_GROUP_ID, new)
