import random

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.misc import db
from VIPMUSIC.utils.decorators import AdminRightsCheck
from VIPMUSIC.utils.inline import close_markup


@app.on_message(
    filters.command(["shuffle", "cshuffle"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


__MODULE__ = "Shuffle"
__HELP__ = """
**Shuffle Queue**

This module allows administrators to shuffle the music queue in the group.

Commands:
- /shuffle: Shuffle the music queue for group.
- /cshuffle: Shuffle the music queue for channel.

Note:
- Only administrators can use these commands.
"""
