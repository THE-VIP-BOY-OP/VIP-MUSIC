import os

from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


@app.on_message(filters.command("authtoken") & SUDOERS)
async def list_formats(client, message):
    try:
        await message.reply_text(
            "**connect with youtube by given below process**\n\n**Otherwise restart bot from server.**"
        )

        os.system(
            f"yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=LLF3GMfNEYU"
        )
        await message.reply_text(
            "**Successfully generated new token check your logger group**"
        )

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
