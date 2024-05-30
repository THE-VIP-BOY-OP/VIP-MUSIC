import logging
from inspect import getfullargspec

from pyrogram import Client, filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    approve_pmpermit,
    disapprove_pmpermit,
    is_on_off,
    is_pmpermit_approved,
)

 
import requests
from pyrogram import Client, filters


@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~SUDOERS
)
async def awaiting_message(client, message):
    text = message.text
    API_URL = f"https://chatgpt.apinepdev.workers.dev/?question={text}&state=girlfriend"
    response = requests.get(API_URL)
    re = response.json()
    result = re["answer"]
    await message.reply_text(result)
