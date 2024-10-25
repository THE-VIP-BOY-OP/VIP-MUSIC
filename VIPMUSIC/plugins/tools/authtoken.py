import os

from pyrogram import filters
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


@app.on_message(filters.command("authtoken") & SUDOERS)
async def list_formats(client, message):
    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
    auth_token = os.getenv("TOKEN_DATA")

    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "%(id)s.mp4",
        "quiet": True,
        "http_headers": {"Authorization": f"Bearer {auth_token}"},
    }

    try:
        ok = await message.reply_text("**Checking old token...")

        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(video_url, download=True)
            file_path = f"{ytdl_data['id']}.mp4"

        await ok.delete()
        await message.reply_text(
            "**✅ Successfully working old token.**",
        )

        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:

        try:
            os.system(f"yt-dlp --username oauth2 --password '' -F {video_url}")

        except Exception as ex:
            await message.reply_text(f"**Failed to generate a new token:** {str(ex)}")
