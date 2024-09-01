from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, adminlist
from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.misc import SUDOERS, db
from VIPMUSIC.utils import AdminRightsCheck
from VIPMUSIC.utils.database import is_active_chat, is_nonadmin_chat
from VIPMUSIC.utils.decorators.language import languageCB
from VIPMUSIC.utils.inline import close_markup, speed_markup

checker = []


@app.on_message(
    filters.command(["cspeed", "speed", "cslow", "slow", "playback", "cplayback"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def playback(cli, message: Message, _, chat_id):
    playing = db.get(chat_id)
    if not playing:
        return await app.send_message(message.chat.id, text=_["queue_2"])
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await app.send_message(message.chat.id, text=_["speed_1"])
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await app.send_message(message.chat.id, text=_["speed_1"])
    upl = speed_markup(_, chat_id)
    return await app.send_message(
        message.chat.id,
        text=_["speed_2"].format(app.mention),
        reply_markup=upl,
    )


@app.on_callback_query(filters.regex("SpeedUP") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, callback_query, _):
    callback_data = callback_query.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat, speed = callback_request.split("|")
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await callback_query.answer(_["general_5"], show_alert=True)
    is_non_admin = await is_nonadmin_chat(callback_query.message.chat.id)
    if not is_non_admin:
        if callback_query.from_user.id not in SUDOERS:
            admins = adminlist.get(callback_query.message.chat.id)
            if not admins:
                return await callback_query.answer(_["speed_10"], show_alert=True)
            else:
                if callback_query.from_user.id not in admins:
                    return await callback_query.answer(_["speed_11"], show_alert=True)
    playing = db.get(chat_id)
    if not playing:
        return await callback_query.answer(_["queue_2"], show_alert=True)
    duration_seconds = int(playing[0]["seconds"])
    if duration_seconds == 0:
        return await callback_query.answer(_["speed_1"], show_alert=True)
    file_path = playing[0]["file"]
    if "downloads" not in file_path:
        return await callback_query.answer(_["speed_1"], show_alert=True)
    checkspeed = playing[0].get("speed")
    if checkspeed:
        if str(checkspeed) == str(speed):
            if str(speed) == str("1.0"):
                return await callback_query.answer(_["speed_3"], show_alert=True)
    else:
        if str(speed) == str("1.0"):
            return await callback_query.answer(_["speed_3"], show_alert=True)
    if chat_id in checker:
        return await callback_query.answer(_["speed_4"], show_alert=True)
    else:
        checker.append(chat_id)
    try:
        await callback_query.answer(_["speed_5"])
    except:
        pass
    mystic = await app.send_message(
        callback_query.message.chat.id,
        text=_["speed_6"].format(callback_query.from_user.mention),
    )
    try:
        await VIP.speedup_stream(
            chat_id,
            file_path,
            speed,
            playing,
        )
    except:
        if chat_id in checker:
            checker.remove(chat_id)
        return await app.send_message(
            callback_query.message.chat.id,
            text=_["speed_7"],
            reply_markup=close_markup(_),
        )
    if chat_id in checker:
        checker.remove(chat_id)
    await app.send_message(
        callback_query.message.chat.id,
        text=_["speed_8"].format(speed, callback_query.from_user.mention),
        reply_markup=close_markup(_),
    )


__MODULE__ = "Speed"
__HELP__ = """
**Speed Control**

This module allows administrators to control the playback speed of audio files in the group.

Commands:
- /cspeed: Speed up the playback.
- /speed: Speed up the playback.
- /cslow: Slow down the playback.
- /slow: Slow down the playback.
- /playback: Control the playback speed.
- /cplayback: Control the playback speed.

Note:
- Only administrators can use these commands.
"""
