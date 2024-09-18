import asyncio
import math

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from strings import get_string
from VIPMUSIC.misc import db
from VIPMUSIC.utils.database import get_active_chats, get_lang, is_music_playing
from VIPMUSIC.utils.formatters import seconds_to_min, time_to_seconds

from ..admins.callback import wrong

checker = {}

# ==========================================================================#


def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 60:
        bar = "——◉——————————"
    elif 60 <= umm < 65:
        bar = "—————◉———————"
    elif 65 <= umm < 70:
        bar = "——————◉——————"
    elif 70 <= umm < 75:
        bar = "———————◉—————"
    elif 75 <= umm < 80:
        bar = "————————◉————"
    elif 80 <= umm < 85:
        bar = "—————————◉———"
    elif 85 <= umm < 90:
        bar = "——————————◉——"
    elif 90 <= umm < 95:
        bar = "———————————◉—"
    elif 95 <= umm < 100:
        bar = "————————————◉"
    else:
        bar = "——◉——————————————"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="II ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),
            InlineKeyboardButton(text="▢ sᴛᴏᴘ", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(
                text="sᴋɪᴘ ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷ ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ ↺", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ғᴇᴀᴛᴜʀᴇs ๏",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 60:
        bar = "——◉——————————"
    elif 60 <= umm < 65:
        bar = "—————◉———————"
    elif 65 <= umm < 70:
        bar = "——————◉——————"
    elif 70 <= umm < 75:
        bar = "———————◉—————"
    elif 75 <= umm < 80:
        bar = "————————◉————"
    elif 80 <= umm < 85:
        bar = "—————————◉———"
    elif 85 <= umm < 90:
        bar = "——————————◉——"
    elif 90 <= umm < 95:
        bar = "———————————◉—"
    elif 95 <= umm < 100:
        bar = "————————————◉"
    else:
        bar = "——◉——————————————"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text=_["CLOSEMENU_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


# ==========================================================================#


async def timer():
    while not await asyncio.sleep(1):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            if not await is_music_playing(chat_id):
                continue
            playing = db.get(chat_id)
            if not playing:
                continue
            file_path = playing[0]["file"]
            if "index_" in file_path or "live_" in file_path:
                continue
            duration = int(playing[0]["seconds"])
            if duration == 0:
                continue
            db[chat_id][0]["played"] += 1


asyncio.create_task(timer())


async def markup_timer():
    while not await asyncio.sleep(120):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                if not await is_music_playing(chat_id):
                    continue
                playing = db.get(chat_id)
                if not playing:
                    continue
                duration_seconds = int(playing[0]["seconds"])
                if duration_seconds == 0:
                    continue
                try:
                    mystic = playing[0]["mystic"]
                    markup = playing[0]["markup"]
                except:
                    continue
                try:
                    check = wrong[chat_id][mystic.message_id]
                    if check is False:
                        continue
                except:
                    pass
                try:
                    language = await get_lang(chat_id)
                    _ = get_string(language)
                except:
                    _ = get_string("en")
                try:
                    buttons = (
                        stream_markup_timer(
                            _,
                            playing[0]["vidid"],
                            chat_id,
                            seconds_to_min(playing[0]["played"]),
                            playing[0]["dur"],
                        )
                        if markup == "stream"
                        else telegram_markup_timer(
                            _,
                            chat_id,
                            seconds_to_min(playing[0]["played"]),
                            playing[0]["dur"],
                        )
                    )
                    await mystic.edit_reply_markup(
                        reply_markup=InlineKeyboardMarkup(buttons)
                    )
                except:
                    continue
            except:
                continue


asyncio.create_task(markup_timer())
