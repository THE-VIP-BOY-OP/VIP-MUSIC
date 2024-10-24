import os
from pyrogram import filters
from VIPMUSIC import app


@app.on_message(filters.command("authtoken"))
async def list_formats(client, message):
    try:
        youtube_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"

        await message.reply_text(
            "**Go to Logs and verify to google account then save token data in variable**\n\n**If you dont want to generate new token data then just restart bot otherwise bot will stay offline**"
        )

        command = f"yt-dlp -F {youtube_url}"

        result = os.popen(command).read()

    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")
