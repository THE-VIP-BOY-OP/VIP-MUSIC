from VIPMUSIC import app
from config import OWNER_ID
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.misc import SUDOERS
import asyncio

BOT_ID = app.me.id

async def ban_member(chat_id, user_id):
    try:
        await app.ban_chat_member(chat_id, user_id)
        return f"ғᴜᴄᴋɪɴɢ ᴛʜɪs ᴍᴇᴍʙᴇʀ ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {user_id}"
    except Exception as e:
        return f"Error banning user {user_id}: {str(e)}"

@app.on_message(filters.command("banall") & SUDOERS)
async def ban_all(_, msg):
    chat_id = msg.chat.id    
    bot = await app.get_chat_member(chat_id, BOT_ID)
    bot_permission = bot.privileges.can_restrict_members == True

    if bot_permission:
        members = await app.get_chat_members(chat_id)
        ban_tasks = [ban_member(chat_id, member.user.id) for member in members]
        ban_results = await asyncio.gather(*ban_tasks)

        for result in ban_results:
            await msg.reply_text(result)
    else:
        await msg.reply_text("ᴇɪᴛʜᴇʀ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀɪɢʜᴛ ᴛᴏ ʀᴇsᴛʀɪᴄᴛ ᴜsᴇʀs ᴏʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ɪɴ sᴜᴅᴏ ᴜsᴇʀs")
