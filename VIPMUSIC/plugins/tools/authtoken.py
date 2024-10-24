import os
import time
from pyrogram import filters
from yt_dlp import YoutubeDL
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


@app.on_message(filters.command("authtoken") & SUDOERS)
async def list_formats(client, message):
    video_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"  # Replace with actual video URL
    auth_token = os.getenv("TOKEN_DATA")  # Replace with the actual OAuth token you have

    # Options for yt-dlp, using OAuth token for authentication
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "%(id)s.mp4",
        "quiet": True,
        "http_headers": {
            "Authorization": f"Bearer {auth_token}"
        }
    }

    try:
        await message.reply_text("Attempting to download the video with OAuth token...")

        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(video_url, download=True)
            file_path = f"{ytdl_data['id']}.mp4"

        await message.reply_video(
            video=open(file_path, "rb"),
            caption="✅ Successfully downloaded using OAuth token."
        )

        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)

    except Exception as e:
        await message.reply_text(f"Download failed: {str(e)}. Attempting to regenerate token...")

        try:
            os.system(f"yt-dlp --username oauth2 --password '' -F {video_url}")
            await message.reply_text("✅ Successfully generated a new token. Check logs for details.")
        except Exception as ex:
            await message.reply_text(f"Failed to generate a new token: {str(ex)}")
