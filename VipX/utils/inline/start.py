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
YOUR_CHANNEL = getenv("YOUR_CHANNEL", "")


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🕹 𝐀𝐃𝐃 𝐌𝐄 𝐁𝐀𝐁𝐘 🕹",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋𝐅𝐄𝐀𝐓𝐔𝐑𝐄🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="⚙️𝐒𝐄𝐓𝐓𝐈𝐍𝐆⚙️", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚  𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏  ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="♦️𝐆𝐑𝐎𝐔𝐏♦️", url=f"https://t.me/{YOUR_GROUP}",
            ),
            InlineKeyboardButton(
                text="♦️𝐌𝐎𝐑𝐄♦️", url=f"https://t.me/{YOUR_CHANNEL}",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ 𝐇𝐄𝐋𝐏 ⚙️", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
