from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils.database import set_loop
from VIPMUSIC.utils.decorators import AdminRightsCheck
from VIPMUSIC.utils.inline import close_markup


@app.on_message(
    filters.command(
        ["end", "stop", "cend", "cstop"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await VIP.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )


__MODULE__ = "Stop Music"
__HELP__ = """
**Stop Music**

This module allows administrators to stop the music playback in the group.

Commands:
- /end: Stop the music playback.
- /stop: Stop the music playback.
- /cend: Stop the music playback.
- /cstop: Stop the music playback.

Note:
- Only administrators can use these commands.
"""
