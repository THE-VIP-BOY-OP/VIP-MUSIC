"""import requests
from pyrogram import Client, filters

from VIPMUSIC.misc import SUDOERS


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
    await message.reply_text(result)"""
