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
    if 10 < umm <= 20:
        bar = "——◉——————————"
    elif 20 <= umm < 35:
        bar = "—————◉———————"
    elif 35 <= umm < 50:
        bar = "——————◉——————"
    elif 50 <= umm < 75:
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
        bar = "◉——————————————"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴘʟᴀʏʟɪsᴛ", callback_data=f"vip_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="ᴄᴏɴᴛʀᴏʟs ♻",
                callback_data=f"Pages Back|3|{videoid}|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ", callback_data=f"downloadvideo {videoid}"
            ),
            InlineKeyboardButton(
                text="📥 ᴀᴜᴅɪᴏ", callback_data=f"downloadaudio {videoid}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ๏",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
        ],
    ]

    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 10 < umm <= 20:
        bar = "——◉——————————"
    elif 20 <= umm < 35:
        bar = "—————◉———————"
    elif 35 <= umm < 50:
        bar = "——————◉——————"
    elif 50 <= umm < 75:
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
        bar = "◉——————————————"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} •{bar}• {dur}",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴘʟᴀʏʟɪsᴛ", callback_data=f"vip_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="ᴄᴏɴᴛʀᴏʟs ♻",
                callback_data=f"Pages Back|3|{videoid}|{chat_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ", callback_data=f"downloadvideo {videoid}"
            ),
            InlineKeyboardButton(
                text="📥 ᴀᴜᴅɪᴏ", callback_data=f"downloadaudio {videoid}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs ๏",
                callback_data=f"Pages Forw|0|{videoid}|{chat_id}",
            ),
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
    while not await asyncio.sleep(3):
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
