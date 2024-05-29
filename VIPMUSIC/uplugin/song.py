from pyrogram import Client, filters
from VIPMUSIC.misc import SUDOERS


@Client.on_message(filters.text & SUDOERS)
def handle_message(client, message):
    message.reply_text("Hello, world!")
