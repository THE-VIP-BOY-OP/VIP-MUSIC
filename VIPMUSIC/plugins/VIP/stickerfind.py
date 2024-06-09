from pyrogram import filters

from VIPMUSIC import app


@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("Please provide a sticker ID after /st command.")


__MODULE__ = "Sticker Find"
__HELP__ = """
**Sticker Command**

This command allows users to send stickers by providing a sticker ID.

Features:
- Reply to a command with a sticker ID to send the corresponding sticker.

Commands:
- /st <sticker_id>: Send a sticker by providing its ID.

Example:
- /st <sticker_id>: Sends the sticker corresponding to the provided ID.

Note: Sticker IDs can be obtained from sticker packs or individual stickers.
"""
