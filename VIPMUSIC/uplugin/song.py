from pyrogram import Client, filters
@Client.on_message(filters.text)
def handle_message(client, message):
    message.reply_text("Hello, world!")