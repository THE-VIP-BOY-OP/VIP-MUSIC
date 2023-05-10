from typing import Union
import re
import os
from os import getenv

from dotenv import load_dotenv

from pyrogram import filters


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
load_dotenv()
YOUR_GROUP = getenv("YOUR_GROUP", "")

def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 𝐀𝐃𝐃 𝐌𝐄 𝐅𝐀𝐒𝐓 𝐁𝐀𝐁𝐘 🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 𝐇𝐄𝐋𝐏 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️ 𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 ⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 𝐀𝐃𝐃 𝐌𝐄 𝐅𝐀𝐒𝐓 𝐁𝐀𝐁𝐘 🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🎭 𝐎𝐖𝐍𝐄𝐑 🎭", url=f"https://t.me/TG_X_BRO",
            ),
            InlineKeyboardButton(
                text="🔰 𝐇𝐄𝐋𝐏 🔰", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎄𝐒𝐔𝐏𝐏𝐎𝐑𝐓🎄", url=f"https://t.me.{YOUR_GROUP}",
            ),
            InlineKeyboardButton(
                text="🥀𝐔𝐏𝐃𝐀𝐓𝐄𝐒🥀", url=f"https://t.me/VIP_CREATORS",
            )
        ],
        [
            InlineKeyboardButton(
                text="🌱ѕσʋяcɛ🌱",
                url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC",
            )
        ],
     ]
    return buttons
