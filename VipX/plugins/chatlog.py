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



@app.on_message(filters.new_chat_members)
async def on_new_chat_members(_, msg):
    link = await app.export_chat_invite_link(msg.chat.id)
    link_text = link if link else "No link"

    await app.send_photo(
        LOG_GROUP_ID,
        photo=random.choice(photo),
        caption=f"{msg.from_user.first_name} added in the new group\n"
                f"Chat name: {msg.chat.title}\n"
                f"Chat username: @{msg.chat.username}\n"
                f"Chat link: {link_text}\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"Go to {msg.from_user.first_name}'s profile", url=f"tg://openmessage?user_id={msg.from_user.id}")]
        ])
    )



@app.on_message(filters.left_chat_member)
async def on_left_chat_members(_, msg):
    link = await app.export_chat_invite_link(msg.chat.id)
    link_text = link if link else "No link"

    await app.send_photo(
        LOG_GROUP_ID,
        photo=random.choice(photo),
        caption=f"{msg.from_user.first_name} left the group\n"
                f"Chat name: {msg.chat.title}\n"
                f"Chat username: @{msg.chat.username}\n"
                f"Chat link: {link_text}\n",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"Go to {msg.from_user.first_name}'s profile", url=f"tg://openmessage?user_id={msg.from_user.id}")]
        ])
    )



