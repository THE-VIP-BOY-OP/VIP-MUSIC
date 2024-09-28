#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def support_group_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_3"],
                    url=SUPPORT_GROUP,
                ),
            ]
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"feature"),
                InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close"),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?start=help"
            )
        ],
    ]
    return buttons


def music_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="✨ᴅ✨", callback_data=f"developer"),
            InlineKeyboardButton(text="⚡ғᴇ⚡", callback_data=f"feature"),
        ],
        [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"home")],
    ]
    return buttons


def about_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="✨ᴅᴇᴠᴇʟᴏᴘᴇʀ✨", callback_data=f"developer"),
            InlineKeyboardButton(text="⚡ғᴇᴀᴛᴜʀᴇ⚡", callback_data=f"feature"),
        ],
        [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data=f"home")],
    ]
    return buttons


def support_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="⚜️ᴜsᴇ ᴍᴇ⚜️", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text="🎭ᴏᴡɴᴇʀ🎭", url=f"tg://openmessage?user_id={config.OWNER_ID}"
            ),
        ],
        [
            InlineKeyboardButton(text="⛅ɢʀᴏᴜᴘ⛅", url=f"{config.SUPPORT_GROUP}"),
            InlineKeyboardButton(text="🎄ᴄʜᴀɴɴᴇʟ🎄", url=f"{config.SUPPORT_CHANNEL}"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data=f"home")],
    ]
    return buttons


def feature_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="🎧 ᴍᴜsɪᴄ 🎧", callback_data=f"music"),
            InlineKeyboardButton(text="♻️ ᴀʟʟ ♻️", callback_data="settings_back_helper"),
        ],
        [InlineKeyboardButton(text="✯ ʜᴏᴍᴇ ✯", callback_data="home")],
    ]
    return buttons


def back_to_music(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"music",
                ),
            ]
        ]
    )
    return upl
