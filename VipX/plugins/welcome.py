import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VipX import app

@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):
    chat = message.chat
    
    for member in message.new_chat_members:
        count = await app.get_chat_members_count(chat.id)

        msg = (
            f"🌷{message.from_user.mention} Welcome in a New Group🥳\n\n"
            f"📌Chat Name: {message.chat.title}\n"
            f"🔐Chat Username: @{message.chat.username}\n"
            f"💖Your ID: {message.from_user.id}\n"
            f"✍️Your Username: @{message.from_user.username}\n"
            f"👥Completed {count} Members🎉"
        )
      
        # Send the group's profile photo
        group_photo = await app.get_chat(chat.id).photo.big_file_id
        
        await app.send_photo(
            message.chat.id,
            photo=group_photo,
            caption=msg,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"Invite Me", url=f"https://t.me/{app.username}?startgroup=true")]
            ])
        )
