from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app
import string
from strings import get_command
from VipX.misc import SUDOERS
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

GALI = [ "**तेरी माँ रंडी मादरचोद**",
         "लंड लेले मेरा भोसड़ी के**" ]


@app.on_message(
    filters.command("gali")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(GALI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✨𝚂𝚄𝙿𝙿𝙾𝚁𝚃✨", url=f"https://t.me/TG_FRIENDSS"),
                    InlineKeyboardButton(
                        "✨𝙾𝙵𝙵𝙸𝙲𝙴✨", url=f"https://t.me/VIP_CREATORS")
                    
                ]
            ]
        ),
    )
