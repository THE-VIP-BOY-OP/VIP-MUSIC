import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import(InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message)
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat

userbot = Userbot()

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):
    chat = message.chat
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
            msg = (
                f"**📝𝐌ᴜsɪᴄ 𝐁ᴏᴛ 𝐀ᴅᴅᴇᴅ 𝐈ɴ 𝐀 #𝐍ᴇᴡ_𝐆ʀᴏᴜᴘ**\n\n"
                f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {chat.title}\n"
                f"**🍂𝐂ʜᴀᴛ 𝐈ᴅ:** {chat.id}\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ:** @{username}\n"
                f"**📈𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs:** {count}\n"
                f"**🤔𝐀ᴅᴅᴇᴅ 𝐁ʏ:** {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"😍𝐀ᴅᴅᴇᴅ 𝐁ʏ😍", url=f"tg://openmessage?user_id={message.from_user.id}")]
            ]))
            if username:
                await userbot.one.join_chat(f"{username}")
            else:
                invite_link = await app.export_chat_invite_link(chat.id)
                await userbot.one.join_chat(f"{invite_link}")

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    left_chat_member = message.left_chat_member
    if left_chat_member and left_chat_member.id == (await app.get_me()).id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        await delete_served_chat(chat_id)
        await userbot.one.start()
        await userbot.one.leave_chat(chat_id)
        await userbot.one.stop()
