import os

from pyrogram import filters
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


async def check_cookies(video_url):
    cookie_file = get_random_cookie()
    opts = {
        "format": "bestaudio",
        "quiet": True,
        "cookiefile": cookie_file,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl.extract_info(video_url, download=False)
        return True
    except:
        return False


async def check_auth_token():
    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
    auth_token = os.getenv("TOKEN_DATA")
    opts = {
        "format": "bestaudio",
        "quiet": True,
        "username": "oauth2",
        "password": auth_token,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl.extract_info(video_url, download=False)
        return True
    except:
        return False


@app.on_message(filters.command("cookies") & SUDOERS)
async def cookies_status(client, message):
    status_message = "**Cookie Status:**\nChecking..."
    status_msg = await message.reply_text(status_message)

    cookie_status = await check_cookies("https://www.youtube.com/watch?v=LLF3GMfNEYU")
    status_message = "**Cookie Status:**\n"
    status_message += "✅ Alive" if cookie_status else "❌ Dead"
    await status_msg.edit_text(status_message)


@app.on_message(filters.command("authtoken") & SUDOERS)
async def auth_token_status(client, message):
    status_message = "**Auth Token Status:**\nChecking..."
    status_msg = await message.reply_text(status_message)

    use_token = await check_auth_token()
    status_message = "**Auth Token Status:**\n"
    status_message += "✅ Alive" if use_token else "❌ Dead"
    await status_msg.edit_text(status_message)

    if not use_token:
        status_message += "\n\n**Generating a new Auth token...**"
        await status_msg.edit_text(status_message)
        try:
            os.system(
                f"yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=LLF3GMfNEYU"
            )
            await message.reply_text("**✅ Successfully generated a new token.**")
        except Exception as ex:
            await message.reply_text(
                f"**❌ Failed to generate a new token: {str(ex)}**"
            )
