import random

import yt_dlp
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import AudioPiped
from VIPMUSIC.core.call import VIP
from VIPMUSIC import app
from VIPMUSIC.platforms.Youtube import cookie_txt_file
from VIPMUSIC.utils.database import get_assistant

# Your predefined YouTube live video URLs
YOUTUBE_LIVE_URLS = [
    "https://www.youtube.com/live/FWZ6qTfTMQ8",  # Replace with actual live stream URLs
    "https://www.youtube.com/live/FWZ6qTfTMQ8",
    "https://www.youtube.com/live/FWZ6qTfTMQ8",
]

# Initialize PyTgCalls for handling group calls



# Function for userbot to join VC and stream audio
async def stream_youtube_audio(userbot, url, chat_id):
    # Download YouTube audio using yt-dlp
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
                "cookiefile": cookie_txt_file(),
            }
        ],
        "outtmpl": "live_audio.mp3",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Ensure userbot joins the group voice chat and streams the audio
    await VIP.join_call(
        chat_id, AudioPiped("live_audio.mp3")  # Use AudioPiped to stream the file
    )


# Command handler for /play
@app.on_message(filters.command("py"))
async def play_live(client: Client, message: Message):
    userbot = await get_assistant(message.chat.id)
    chat_id = message.chat.id

    # Select a random live stream URL from the list
    selected_url = random.choice(YOUTUBE_LIVE_URLS)
    await message.reply(f"Now playing live stream: {selected_url}")

    # Let userbot stream the YouTube audio
    await stream_youtube_audio(userbot, selected_url, chat_id)


# Start both the bot and PyTgCalls client
