from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            
            InlineKeyboardButton(
                text="✡ sᴇᴛᴛɪɴɢ ✡", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="☢ ɢʀᴏᴜᴘ ☢", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ🥀", url=config.SUPPORT_CHANNEL),
        ],
            
    ]
    return buttons
