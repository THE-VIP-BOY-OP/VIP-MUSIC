import asyncio
import glob
import os
import random
from typing import Union

from pyrogram import filters
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS

TEST_VIDEO_URL = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
auth_token = os.getenv("TOKEN_DATA")


def get_random_cookie():
    folder_path = f"{os.getcwd()}/cookies"
    txt_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    return random.choice(txt_files)


class YouTubeAuthDownloader:
    def __init__(self):
        self.base_url = TEST_VIDEO_URL

    def get_ytdl_options(self, ytdl_opts, auth_token: str) -> Union[str, dict, list]:
        if isinstance(ytdl_opts, list):
            ytdl_opts += ["--username", "oauth2", "--password", auth_token]
        elif isinstance(ytdl_opts, str):
            ytdl_opts += f"--username oauth2 --password {auth_token} "
        elif isinstance(ytdl_opts, dict):
            ytdl_opts.update({"username": "oauth2", "password": auth_token})
        return ytdl_opts

    async def download(self, link: str, auth_token: str, video: bool = True) -> str:
        loop = asyncio.get_running_loop()

        def download_content():
            if not os.path.exists("downloads"):
                os.makedirs("downloads")
            ydl_opts = {
                "format": (
                    "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])"
                    if video
                    else "bestaudio/best"
                ),
                "outtmpl": "downloads/%(id)s.%(ext)s",
                "geo_bypass": True,
                "nocheckcertificate": True,
                "quiet": True,
                "no_warnings": True,
            }
            ydl_opts = self.get_ytdl_options(ydl_opts, auth_token)

            ydl = YoutubeDL(ydl_opts)
            info = ydl.extract_info(link, download=False)
            file_path = os.path.join("downloads", f"{info['id']}.{info['ext']}")
            if not os.path.exists(file_path):
                ydl.download([link])
            return file_path

        file_path = await loop.run_in_executor(None, download_content)
        return file_path


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
    except Exception as e:
        print(f"Error checking cookies: {e}")
        return False


async def check_auth_token():
    auth_token = os.getenv("TOKEN_DATA")
    opts = {
        "format": "bestaudio",
        "quiet": True,
        "username": "oauth2",
        "password": auth_token,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl.extract_info(TEST_VIDEO_URL, download=False)
        return True
    except Exception as e:
        print(f"Error checking auth token: {e}")
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
async def download_videoo():
    os.system(
        f"yt-dlp --username oauth2 --password '' -F https://www.youtube.com/watch?v=LLF3GMfNEYU"
    )


async def list_formats(client, message):
    status_message = "**Status:**\n\n"
    status_message += "Cookies: Checking...\nAuth Token: Checking..."
    status_msg = await message.reply_text(status_message)

    cookie_status = await check_cookies(TEST_VIDEO_URL)
    status_message = "**Status:**\n\n"
    status_message += f"Cookies: {'✅ Alive' if cookie_status else '❌ Dead'}\nAuth Token: Checking..."
    await status_msg.edit_text(status_message)

    use_token = await check_auth_token()
    status_message = "**Status:**\n\n"
    status_message += f"Cookies: {'✅ Alive' if cookie_status else '❌ Dead'}\n"
    status_message += f"Auth Token: {'✅ Alive' if use_token else '❌ Dead'}"
    await status_msg.edit_text(status_message)

    if not use_token:
        status_message += "\n\n**Generating a new Auth token...**"
        await status_msg.edit_text(status_message)
        try:
            await download_videoo()
            await message.reply_text(f"\n**✅ Successfully generated a new token.**")
        except Exception as ex:
            await message.reply_text(
                f"\n**❌ Failed to generate a new token: {str(ex)}**"
            )
