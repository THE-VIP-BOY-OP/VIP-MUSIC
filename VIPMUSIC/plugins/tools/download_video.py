import future

import asyncio
import os
import time
from urllib.parse import urlparse
from pyrogram.types import (InlineKeyboardButton, CallbackQuery,
                            InlineKeyboardMarkup, Message)
import wget
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pytube import YouTube
from VIPMUSIC import app
import asyncio
import os
import time
import wget
from urllib.parse import urlparse
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from VIPMUSIC import app
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user



import asyncio
import os
import wget
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos


from VIPMUSIC import app
from VIPMUSIC.utils.extraction import extract_user

BANNED_USERS = []

import asyncio
import os
import wget
from pytube import YouTube
from pyrogram import Client, filters



@app.on_callback_query(filters.regex("download_video") & ~filters.user(BANNED_USERS))
async def download_video(client, callback_query):
    callback_data = callback_query.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(callback_query.message.chat.id, f"Searching, please wait...")
    if not videoid:
        await pablo.edit("Video not found")
        return

    try:
        search = YouTube(f"https://youtu.be/{videoid}")
    except Exception as e:
        await pablo.edit("Error occurred while searching for the video.")
        return

    thum = search.title
    link = search.watch_url
    thums = search.author
    kekme = f"https://img.youtube.com/vi/{videoid}/maxresdefault.jpg"
    await asyncio.sleep(0.6)
    url = link
    sedlyf = wget.download(kekme)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"**Failed to download.** \n**Error:** `{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"❄ **Title:** [{thum}]({link})\n💫 **Channel:** {thums}\n🥀 **Requested by:** {chutiya}"
    await client.send_video(
        callback_query.message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=sedlyf,
        caption=capy,
        supports_streaming=True,
        progress_args=(
            pablo,
            f"Please wait...\n\nUploading `{videoid}` from YouTube servers...💫",
            file_stark,
        ),
    )
    await pablo.delete()
    for files in (sedlyf, file_stark):
        if files and os.path.exists(files):
            os.remove(files)
