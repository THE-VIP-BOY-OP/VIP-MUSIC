import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VipX import app  

photo = [
    "https://telegra.ph/file/1b819cfbcb2a2d3c738f6.jpg",
    "https://telegra.ph/file/3021c823c7f006658682f.jpg",
    "https://telegra.ph/file/05561f0fbf323e057ab87.jpg",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/b3de9e03e5c8737ca897f.jpg",
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷{message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ ᴀ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳\n\n"
                f"**📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝐊ɪᴅɴᴀᴘ 𝐌ᴇ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
