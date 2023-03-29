
from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AnonX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHAYRI = [ " ** ✨बहुत अच्छा लगता है तुझे सताना
और फिर प्यार से तुझे मनाना।✨ ** \n\n ** 💞Bahut aacha lagta hai tujhe
satana Aur fir pyar se tujhe
manana.💞 ** ",
           " ** ✨मेरी जिंदगी मेरी जान हो तुम
मेरे सुकून का दुसरा नाम हो तुम।✨ ** \n\n ** 💞Meri zindagi Meri jaan ho
tum Mere sukoon ka Dusra
naam ho tum.💞 ** ",
           " ** ✨तुम मेरी वो खुशी हो जिसके बिना,
मेरी सारी खुशी अधूरी लगती है।✨ ** \n\n ** 💞Tum Meri Wo Khushi Ho Jiske Bina,
Meri Saari Khushi Adhuri Lagti Ha.💞 ** " ]

@app.on_message(
    filters.command("shayri")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHAYRI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )
