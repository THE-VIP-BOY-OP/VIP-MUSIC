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
from VIPMUSIC import YouTube
from youtubesearchpython import VideosSearch
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


import asyncio
import os
import requests
import wget
from pyrogram import filters
from pyrogram.types import Message
from yt_dlp import YoutubeDL

from VIPMUSIC import app
from VIPMUSIC.utils.extraction import extract_user

BANNED_USERS = []


@app.on_callback_query(filters.regex("downloadvideo") & ~filters.user(BANNED_USERS))
async def downloadvideo(client, callback_query):
    callback_data = callback_query.data.strip()
    video_id = callback_data.split(None, 1)[1]
    user_id = callback_query.from_user.id
    user_name = callback_query.from_user.first_name
    user_link = f"[{user_name}](tg://user?id={user_id})"

    message = await client.send_message(callback_query.message.chat.id, f"Searching, please wait...")
    
    try:
        yt = YouTube(f"https://youtu.be/{video_id}")
        yt_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
        if yt_stream:
            yt_stream.download()
            file_stark = f"{yt.title}.mp4"
            capy = f"❄ **Title:** [{yt.title}]({yt.watch_url})\n💫 **Channel:** {yt.author}\n🥀 **Requested by:** {user_link}"
            await client.send_video(
                callback_query.message.chat.id,
                video=open(file_stark, "rb"),
                duration=int(yt.length),
                file_name=str(yt.title),
                thumb=yt.thumbnail_url,
                caption=capy,
                supports_streaming=True,
                progress_args=(
                    message,
                    f"Please wait...\n\nUploading `{yt.video_id}` from YouTube servers...💫",
                    file_stark,
                ),
            )
            await message.delete()
            os.remove(file_stark)
        else:
            await message.edit("No stream available for the provided video.")
    except Exception as e:
        await message.edit(f"Error: {str(e)}")



@app.on_callback_query(filters.regex("downloadaudio") & ~filters.user(BANNED_USERS))
async def downloadaudio(client, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split()[1]  # Extract video ID from callback data
    m = await client.send_message(CallbackQuery.message.chat.id, f"**🔄 Searching {videoid}... **")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YouTube(f"https://youtube.com/{videoid}")
        link = f"https://youtube.com{videoid}"
        title = results.title
        thumbnail = results.thumbnails
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

        # Add these lines to define views and channel_name
        views = results.views
        channel_name = results.channel

    except Exception as e:
        await m.edit("**⚠️ No results found. Make sure you typed the correct song name.**")
        print(str(e))
        return
    await m.edit("**📥 Downloading...**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        await m.edit("**📤 Uploading...**")

        await client.send_audio(
            CallbackQuery.message.chat.id,
            audio=open(audio_file, "rb"),
            thumb=thumb_name,
            title=title,
            caption=f"{title}\nViews➪ {views}\nChannel➪ {channel_name}",
            duration=dur
        )
        await m.delete()
    except Exception as e:
        await m.edit(" - An error occurred!!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
