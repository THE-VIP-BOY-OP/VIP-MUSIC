from pyrogram import Client, filters


@Client.on_message(filters.text & filters.chat("vk_zone"))
def handle_message(client, message):
    message.reply_text("Hello, world!")
