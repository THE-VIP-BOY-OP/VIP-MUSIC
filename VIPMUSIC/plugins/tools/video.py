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

def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

import os

from pyrogram.types import Message
from youtube_search import YoutubeSearch

@app.on_message(filters.command(["video", "yt"]))
async def download_video(client, message: Message):
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        await message.reply("Please provide a valid URL or song name.")
        return

    command, query = text
    url = None
    if command == "/video":
        url = query
    else:
        results = YoutubeSearch(query, max_results=1).to_dict()
        if results:
            url = f"https://www.youtube.com{results[0]['url_suffix']}"
        else:
            await message.reply("No video found for the given song name.")
            return

    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, "Downloading, please wait...")

    try:
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
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"Failed to download.\nError: `{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Title:** {ytdl_data['title']}\n**URL:** {url}\n**Requested by:** {chutiya}"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        caption=capy,
        supports_streaming=True,
    )

    await pablo.delete()
    if os.path.exists(file_stark):
        os.remove(file_stark)


@app.on_message(filters.command(["shorts"]))
async def download_shorts(client, message: Message):
    url = get_text(message)
    if not url:
        await message.reply("Please provide a valid URL.")
        return

    await message.delete()
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"

    pablo = await client.send_message(message.chat.id, "Downloading, please wait...")

    try:
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
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)

    except Exception as e:
        await pablo.edit(f"Failed to download.\nError: `{str(e)}`")
        return

    file_stark = f"{ytdl_data['id']}.mp4"
    capy = f"**Title:** {ytdl_data['title']}\n**URL:** {url}\n**Requested by:** {chutiya}"
    await client.send_video(
        message.chat.id,
        video=open(file_stark, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        caption=capy,
        supports_streaming=True,
    )

    await pablo.delete()
    if os.path.exists(file_stark):
        os.remove(file_stark)

__mod_name__ = "Video and Shorts Downloader"
__help__ = """
/video or /yt [URL] - Download video from the provided URL.
/shorts [URL] - Download shorts video from the provided URL.
"""
