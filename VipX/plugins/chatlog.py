import random
from pyrogram import filters
from pyrogram.types import *
from config import LOG_GROUP_ID
from .. import app
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
        caption=f"{app.first_name} added in new group\n"
                f"chat name : {msg.chat.title}\n"
                f"chat username : @{msg.chat.username}\n"
                f"chat link : {link_text}\n",
        reply_markup=InlineKeyboardMarkup([
            InlineKeyboardButton(f"{msg.from_user.first_name}", url=f"tg://openmessage?user_id={msg.from_user.id}")
        ])
    )


@app.on_message(filters.left_chat_member)
async def on_left_chat_members(_, msg):
    link = await app.export_chat_invite_link(msg.chat.id)
    link_text = link if link else "No link"
        
    await app.send_photo(
        LOG_GROUP_ID, 
        photo=random.choice(photo), 
        caption=f"{app.first_name} left in new group\n"
                f"chat name : {msg.chat.title}\n"
                f"chat username : @{msg.chat.username}\n"
                f"chat link : {link_text}\n",
        reply_markup=InlineKeyboardMarkup([
            InlineKeyboardButton(f"{msg.from_user.first_name}", url=f"tg://openmessage?user_id={msg.from_user.id}")
        ])
    )




