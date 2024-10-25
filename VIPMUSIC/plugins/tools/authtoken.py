import asyncio
import glob
import os
import random

from pyrogram import filters
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


def get_random_cookie():
    folder_path = f"{os.getcwd()}/cookies"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    return random.choice(txt_files)


async def check_auth_token():
    auth_token = os.getenv("TOKEN_DATA")
    if auth_token:
        opts = {
            "format": "bestaudio",
            "quiet": True,
            "http_headers": {"Authorization": f"Bearer {auth_token}"},
        }

        try:
            with YoutubeDL(opts) as ytdl:
                ytdl.extract_info(
                    "https://www.youtube.com/watch?v=LLF3GMfNEYU", download=False
                )
            return True
        except Exception as e:
            print(f"Token validation failed: {str(e)}")
            return False
    return False


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


@app.on_message(
    filters.command(
        [
            "authstatus",
            "authtoken",
            "cookies",
            "cookie",
            "cookiesstatus",
            "cookiescheck",
        ]
    )
    & SUDOERS
)
async def list_formats(client, message):
    ok = await message.reply_text("**Checking Cookies & auth token...**")

    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"

    auth_token_status = asyncio.run(check_auth_token())
    cookie_status = await check_cookies(video_url)

    status_message = "**Token and Cookie Status:**\n\n"
    if auth_token_status:
        status_message += "✅ Auth token is active.\n"
    else:
        status_message += "❌ Auth token is inactive.\n"

    if cookie_status:
        status_message += "✅ Cookies are active.\n\n"
    else:
        status_message += "❌ Cookies are inactive.\n\n"

    if not auth_token_status:
        status_message += "**Create a new Auth token...**"
        await ok.delete()
        await message.reply_text(status_message)
        try:
            os.system(f"yt-dlp --username oauth2 --password '' -F {video_url}")
            await message.reply_text("✅ Successfully generated a new token.")
        except Exception as ex:
            await message.reply_text(f"**Failed to generate a new token:** {str(ex)}")
    else:
        await ok.delete()
        await message.reply_text(status_message)
