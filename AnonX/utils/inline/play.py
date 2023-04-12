import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from AnonX import app

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥BRANDED_WORLD💥 "
    elif 3 <= anon < 4:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 4 <= anon < 5:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 6 <= anon < 7:
        bar = " 💥BRANDED_WORLD💥 "
    elif 7 <= anon < 8:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 9 <= anon < 10:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 11 <= anon < 12:
        bar = " 💥BRANDED_WORLD💥 "
    elif 12 <= anon < 13:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 13 < anon < 14:
        bar = " 💥BRANDED_WORLD💥 "
    elif 14 <= anon < 15:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 15 <= anon < 16:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 16 <= anon < 17:
        bar = " 💥BRANDED_WORLD💥 "
    elif 17 <= anon < 18:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 18 <= anon < 19:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 19 <= anon < 20:
        bar = " 💥BRANDED_WORLD💥 "
    elif 20 <= anon < 21:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 21 <= anon < 22:
        bar = " 💥BRANDED_WORLD💥 "
    elif 22 <= anon < 23:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 23 <= anon < 24:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 24 <= anon < 25:
        bar = " 💥BRANDED_WORLD💥 "
    elif 25 <= anon < 26:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 26 <= anon < 27:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 27 <= anon < 28:
        bar = " 💥BRANDED_WORLD💥 "
    elif 28 <= anon < 29:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 29 <= anon < 30:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 30 <= anon < 31:
        bar = " 💥BRANDED_WORLD💥 "
    elif 31 <= anon < 32:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 32 <= anon < 33:
        bar = " 💥BRANDED_WORLD💥 "
    elif 33 <= anon < 34:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 34 <= anon < 35:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 35 <= anon < 36:
        bar = " 💥BRANDED_WORLD💥 "
    elif 36 <= anon < 37:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 37 <= anon < 38:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 38 <= anon < 39:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 39 <= anon < 40:
        bar = " 💥BRANDED_WORLD💥 "
    elif 40 <= anon < 41:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 41 <= anon < 42:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 42 <= anon < 43:
        bar = " 💥BRANDED_WORLD💥 "
    elif 43 <= anon < 44:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 44 < anon < 45:
        bar = " 💥BRANDED_WORLD💥 "
    elif 45 <= anon < 46:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 46 <= anon < 47:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 47 <= anon < 48:
        bar = " 💥BRANDED_WORLD💥 "
    elif 48 <= anon < 49:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 49 <= anon < 50:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 50 <= anon < 51:
        bar = " 💥BRANDED_WORLD💥 "
    elif 51 <= anon < 52:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 52 <= anon < 53:
        bar = " 💥BRANDED_WORLD💥 "
    elif 53 <= anon < 54:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 54 <= anon < 55:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 55 <= anon < 56:
        bar = " 💥BRANDED_WORLD💥 "
    elif 56 <= anon < 57:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 57 <= anon < 58:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 58 <= anon < 59:
        bar = " 💥BRANDED_WORLD💥 "
    elif 59 <= anon < 60:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 61 <= anon < 62:
        bar = " 💥BRANDED_WORLD💥 "
    elif 62 <= anon < 63:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 63 <= anon < 64:
        bar = " 💥BRANDED_WORLD💥 "
    elif 64 <= anon < 65:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 65 <= anon < 66:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 66 <= anon < 67:
        bar = " 💥BRANDED_WORLD💥 "
    elif 67 <= anon < 68:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 68 <= anon < 69:
        bar = " 💥BRANDED_WORLD💥 "
    elif 69 <= anon < 70:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 70 <= anon < 71:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 71 <= anon < 72:
        bar = " 💥BRANDED_WORLD💥 "
    elif 72 <= anon < 73:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 73 <= anon < 74:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 74 <= anon < 75:
        bar = " 💥BRANDED_WORLD💥 "
    elif 75 <= anon < 76:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 76 < anon < 77:
        bar = " 💥BRANDED_WORLD💥 "
    elif 77 <= anon < 78:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 78 <= anon < 79:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 79 <= anon < 80:
        bar = " 💥BRANDED_WORLD💥 "
    elif 80 <= anon < 81:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 81 <= anon < 82:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 82 <= anon < 83:
        bar = " 💥BRANDED_WORLD💥 "
    elif 83 <= anon < 84:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 84 <= anon < 85:
        bar = " 💥BRANDED_WORLD💥 "
    elif 85 <= anon < 86:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 86 <= anon < 87:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 87 <= anon < 88:
        bar = " 💥BRANDED_WORLD💥 "
    elif 88 <= anon < 89:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 89 <= anon < 90:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 90 <= anon < 91:
        bar = " 💥BRANDED_WORLD💥 "
    elif 91 <= anon < 92:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 92 <= anon < 93:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 93 <= anon < 94:
        bar = " 💥BRANDED_WORLD💥 "
    elif 94 <= anon < 95:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 95 <= anon < 96:
        bar = " 💥BRANDED_WORLD💥 "
    elif 96 <= anon < 97:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 97 <= anon < 98:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 98 <= anon < 99:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    else:
        bar = " 🍷ѕσ ¢ιтє ѕσηg🍷 "
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "⚡ѕтαяє∂ ρℓαყเɳɠ⚡"
    elif 2 < anon < 3:
        bar = " 💥BRANDED_WORLD💥 "
    elif 3 <= anon < 4:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 4 <= anon < 5:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 6 <= anon < 7:
        bar = " 💥BRANDED_WORLD💥 "
    elif 7 <= anon < 8:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 9 <= anon < 10:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 11 <= anon < 12:
        bar = " 💥BRANDED_WORLD💥 "
    elif 12 <= anon < 13:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 13 < anon < 14:
        bar = " 💥BRANDED_WORLD💥 "
    elif 14 <= anon < 15:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 15 <= anon < 16:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 16 <= anon < 17:
        bar = " 💥BRANDED_WORLD💥 "
    elif 17 <= anon < 18:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 18 <= anon < 19:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 19 <= anon < 20:
        bar = " 💥BRANDED_WORLD💥 "
    elif 20 <= anon < 21:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 21 <= anon < 22:
        bar = " 💥BRANDED_WORLD💥 "
    elif 22 <= anon < 23:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 23 <= anon < 24:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 24 <= anon < 25:
        bar = " 💥BRANDED_WORLD💥 "
    elif 25 <= anon < 26:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 26 <= anon < 27:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 27 <= anon < 28:
        bar = " 💥BRANDED_WORLD💥 "
    elif 28 <= anon < 29:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 29 <= anon < 30:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 30 <= anon < 31:
        bar = " 💥BRANDED_WORLD💥 "
    elif 31 <= anon < 32:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 32 <= anon < 33:
        bar = " 💥BRANDED_WORLD💥 "
    elif 33 <= anon < 34:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 34 <= anon < 35:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 35 <= anon < 36:
        bar = " 💥BRANDED_WORLD💥 "
    elif 36 <= anon < 37:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 37 <= anon < 38:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 38 <= anon < 39:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 39 <= anon < 40:
        bar = " 💥BRANDED_WORLD💥 "
    elif 40 <= anon < 41:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 41 <= anon < 42:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 42 <= anon < 43:
        bar = " 💥BRANDED_WORLD💥 "
    elif 43 <= anon < 44:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 44 < anon < 45:
        bar = " 💥BRANDED_WORLD💥 "
    elif 45 <= anon < 46:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 46 <= anon < 47:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 47 <= anon < 48:
        bar = " 💥BRANDED_WORLD💥 "
    elif 48 <= anon < 49:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 49 <= anon < 50:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 50 <= anon < 51:
        bar = " 💥BRANDED_WORLD💥 "
    elif 51 <= anon < 52:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 52 <= anon < 53:
        bar = " 💥BRANDED_WORLD💥 "
    elif 53 <= anon < 54:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 54 <= anon < 55:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 55 <= anon < 56:
        bar = " 💥BRANDED_WORLD💥 "
    elif 56 <= anon < 57:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 57 <= anon < 58:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 58 <= anon < 59:
        bar = " 💥BRANDED_WORLD💥 "
    elif 59 <= anon < 60:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 60 <= anon < 61:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 61 <= anon < 62:
        bar = " 💥BRANDED_WORLD💥 "
    elif 62 <= anon < 63:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 63 <= anon < 64:
        bar = " 💥BRANDED_WORLD💥 "
    elif 64 <= anon < 65:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 65 <= anon < 66:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 66 <= anon < 67:
        bar = " 💥BRANDED_WORLD💥 "
    elif 67 <= anon < 68:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 68 <= anon < 69:
        bar = " 💥BRANDED_WORLD💥 "
    elif 69 <= anon < 70:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 70 <= anon < 71:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 71 <= anon < 72:
        bar = " 💥BRANDED_WORLD💥 "
    elif 72 <= anon < 73:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 73 <= anon < 74:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 74 <= anon < 75:
        bar = " 💥BRANDED_WORLD💥 "
    elif 75 <= anon < 76:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 76 < anon < 77:
        bar = " 💥BRANDED_WORLD💥 "
    elif 77 <= anon < 78:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 78 <= anon < 79:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 79 <= anon < 80:
        bar = " 💥BRANDED_WORLD💥 "
    elif 80 <= anon < 81:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 81 <= anon < 82:
        bar = " 🥀@BRANDED_KHUSHI🥀 "
    elif 82 <= anon < 83:
        bar = " 💥BRANDED_WORLD💥 "
    elif 83 <= anon < 84:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 84 <= anon < 85:
        bar = " 💥BRANDED_WORLD💥 "
    elif 85 <= anon < 86:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 86 <= anon < 87:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 87 <= anon < 88:
        bar = " 💥BRANDED_WORLD💥 "
    elif 88 <= anon < 89:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 89 <= anon < 90:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 90 <= anon < 91:
        bar = " 💥BRANDED_WORLD💥 "
    elif 91 <= anon < 92:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 92 <= anon < 93:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 93 <= anon < 94:
        bar = " 💥BRANDED_WORLD💥 "
    elif 94 <= anon < 95:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 95 <= anon < 96:
        bar = " 💥BRANDED_WORLD💥 "
    elif 96 <= anon < 97:
        bar = " 🔥BRANDED_CREATORS🔥 "
    elif 97 <= anon < 98:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    elif 98 <= anon < 99:
        bar = " 🥀BRANDED_KHUSHI🥀 "
    else:
        bar = " 🍷ℓσνєℓу ѕσηg🍷 "

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [  
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons
