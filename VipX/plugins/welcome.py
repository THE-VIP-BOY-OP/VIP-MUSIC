import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VipX import app
from pyrogram.types import ChatPermissions


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)
        
        
            msg = (
                f"🌷{message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ ᴀ 𝐍ᴇw 𝐆ʀᴏᴜᴘ🥳\n\n"
                f"📌𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {message.chat.title}\n"
                f"🔐𝐂ʜᴀᴛ 𝐔.𝐍: @{message.chat.username}\n"
                f"💖𝐔ʀ 𝐈d: {message.from_user.id}\n"
                f"✍️𝐔ʀ 𝐔.𝐍aмe: @{message.from_user.username}\n"
                f"👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀs🎉"
            )
            await app.send_photo(message.chat.id, photo={await app.get_chat(message.chat.id).photo.big_file_id}, caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"𝐊ɪᴅɴᴀᴘ 𝐌ᴇ", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))


@app.on_message(filters.chat_created, group=3)
async def set_default_permissions(_, message):
    
    chat = message.chat
    permissions = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_stickers=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_pin_messages=True,
        can_change_info=True,
        can_delete_messages=True,
        can_edit_messages=True,
        can_promote_members=True,
        can_restrict_members=True,
        can_ban_users=True,
        can_unban_users=True,
    )
    await chat.set_permissions(permissions)
