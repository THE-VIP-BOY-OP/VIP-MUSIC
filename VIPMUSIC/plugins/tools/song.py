import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtubesearchpython import VideosSearch
import yt_dlp

from ... import app

DOWNLOAD_PATH = "downloads"

@app.on_message(filters.command(["song", "audio"], ["/", "!", "."]))
async def audio_command(client: app, message: Message):
    await download_media(message, audio=True)

@app.on_message(filters.command(["video"], ["/", "!", "."]))
async def video_command(client: app, message: Message):
    await download_media(message, audio=False)

async def download_media(message: Message, audio: bool = True):
    command_name = "audio" if audio else "video"
    aux = await message.reply_text(f"**🔄 𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐚𝐧𝐝 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 {command_name}...**")

    if len(message.command) < 2:
        return await aux.edit(f"**Usage:** `/song` or `/audio` for audio, `/video` for video")

    try:
        media_name = message.text.split(None, 1)[1]
        vid = VideosSearch(media_name, limit=1)
        media_title = vid.result()["result"][0]["title"]
        media_link = vid.result()["result"][0]["link"]

        # Provide video quality options
        quality_options = [
            {"itag": "18", "label": "360p"},
            {"itag": "22", "label": "720p"},
            {"itag": "137", "label": "1080p"},
            # Add more quality options as needed
        ]

        quality_buttons = [
            InlineKeyboardButton(option["label"], callback_data=f'{option["itag"]}_{media_link}_{media_title}_{audio}')
            for option in quality_options
        ]

        markup = InlineKeyboardMarkup([quality_buttons])
        await aux.edit(f"**Choose the preferred {command_name} quality:**", reply_markup=markup)

    except Exception as e:
        await aux.edit(f"**Error:** {e}")

async def download_video_with_quality(quality_itag, media_link, media_title, audio, aux):
    ydl_opts = {
        "format": f"bestvideo[height<=?1080][itag={quality_itag}]+bestaudio/best" if quality_itag.isnumeric() else "bestaudio/best",
        "verbose": True,
        "geo-bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4"
            }
        ] if quality_itag.isnumeric() else [],
        "outtmpl": f"{DOWNLOAD_PATH}/{media_title}.mp3" if audio else f"{DOWNLOAD_PATH}/{media_title}.mp4",
    }

    await aux.edit(f"**𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐯𝐢𝐝𝐞𝐨...**")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        await asyncio.to_thread(ydl.download, [media_link])

    await aux.edit(f"**𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠 𝐯𝐢𝐝𝐞𝐨...**")

    return ydl_opts

@app.on_callback_query(filters.regex(r'^\d+_.+_.+_(True|False)$'))
async def process_callback_query(client, query):
    try:
        quality_itag, media_link, media_title, audio_str = query.data.split('_', 3)
        audio = audio_str.lower() == 'true'
        aux = await query.message.reply_text(f"**𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐯𝐢𝐝𝐞𝐨...**")
        ydl_opts = await download_video_with_quality(quality_itag, media_link, media_title, audio, aux)

        if audio:
            await query.message.reply_audio(f"{DOWNLOAD_PATH}/{media_title}.mp3")
        else:
            await query.message.reply_video(f"{DOWNLOAD_PATH}/{media_title}.mp4")

        try:
            os.remove(f"{DOWNLOAD_PATH}/{media_title}.mp3") if audio else os.remove(f"{DOWNLOAD_PATH}/{media_title}.mp4")
        except:
            pass

        await aux.delete()

    except Exception as e:
        print(e)
