import random
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import LOG_GROUP_ID
from VipX import app  



photo = [
    "https://telegra.ph/file/1b819cfbcb2a2d3c738f6.jpg",
    "https://telegra.ph/file/3021c823c7f006658682f.jpg",
    "https://telegra.ph/file/05561f0fbf323e057ab87.jpg",
    "https://telegra.ph/file/7a6b51ee0077724254ca7.jpg",
    "https://telegra.ph/file/b3de9e03e5c8737ca897f.jpg",
]



@app.on_message(filters.new_chat_members, group=2)
async def on_new_chat_members(_, msg):
    link = await app.export_chat_invite_link(msg.chat.id)
    link_text = link if link else "ɴᴏ ʟɪɴᴋ"
    
    await app.send_photo(
        LOG_GROUP_ID,
        photo=random.choice(photo),
        caption=f"ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"ᴄʜᴀᴛ ɴᴀᴍᴇ: {msg.chat.title}\n"
                f"ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat_username}\n"
                f"ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link_text})\n",
                
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"{msg.from_user.first_name}'", url=f"tg://openmessage?user_id={msg.from_user.id}")]
        ])
    )

