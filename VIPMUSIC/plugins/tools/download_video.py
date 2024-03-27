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
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.utils.extraction import extract_user

BANNED_USERS = []

@app.on_callback_query(filters.regex("download_video") & ~filters.user(BANNED_USERS))
async def download_video(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
    user_name = CallbackQuery.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(CallbackQuery.message.chat.id, f"Searching, please wait...")
    if not videoid:
        await pablo.edit(
            "video not found"
        )
        return

    search = YouTube(f"https://youtu.be/{videoid}")
    mi = search.result()
    mio = mi.get("search_result", [])
    if not mio:
        await pablo.edit("Song not found on YouTube.")
        return
    thum = search.title
    duration = search.length
    link = search.link
    fridayz = videoid
    thums = search.channel
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

    file_stark = f"{ytdl_data['videoid']}.mp4"
    capy = f"❄ **Title:** [{thum}]({link})\n💫 **Channel:** {thums}\n🥀 **Requested by:** {chutiya}"
    await client.send_video(
        CallbackQuery.message.chat.id,
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
