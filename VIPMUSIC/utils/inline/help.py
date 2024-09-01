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
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"], callback_data=f"settings_back_helper"
                ),
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
