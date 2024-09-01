from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP as VIP
from VIPMUSIC.utils.database import is_music_playing, music_on
from VIPMUSIC.utils.decorators import AdminRightsCheck


@app.on_message(filters.command(["resume", "cresume"]) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def resume_com(cli, message: Message, _, chat_id):
    if await is_music_playing(chat_id):
        return await message.reply_text(_["admin_3"])
    await music_on(chat_id)
    await VIP.resume_stream(chat_id)
    buttons_resume = [
        [
            InlineKeyboardButton(text="sᴋɪᴘ", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
        ],
    ]
    await message.reply_text(
        _["admin_4"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons_resume),
    )


__MODULE__ = "Resume"
__HELP__ = """
**Resume**

This module allows administrators to resume playback of the currently paused track.

Commands:
- /resume: Resumes playback of the currently paused track for group.
- /cresume: Resumes playback of the currently paused track for channel.

Note:
- Only administrators can use these commands.
"""
