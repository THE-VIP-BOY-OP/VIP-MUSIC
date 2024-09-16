import random
import os
from pyrogram import Client, filters
from pyrogram.types import Message
import yt_dlp
from asyncio import create_subprocess_shell
from VIPMUSIC import app 
# Your predefined YouTube live video URLs
YOUTUBE_LIVE_URLS = [
    "https://www.youtube.com/live/FWZ6qTfTMQ8",  # replace with actual live stream URLs
    "https://www.youtube.com/live/FWZ6qTfTMQ8",
    "https://www.youtube.com/live/FWZ6qTfTMQ8"
]



# Assistant (userbot) import from database
from VIPMUSIC.utils.database import get_assistant

# Function for userbot to join VC and stream audio
async def stream_youtube_audio(userbot, url, chat_id):
    # Download YouTube audio using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'live_audio.mp3'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Ensure userbot joins the voice chat
    vc = await userbot.join_voice_chat(chat_id)
    
    # Stream the downloaded audio using ffmpeg and pipe it to the voice chat
    await vc.stream('live_audio.mp3')

# Command handler for /play
@app.on_message(filters.command("pla"))
async def play_live(client: Client, message: Message):
    userbot = await get_assistant(message.chat.id)
    chat_id = message.chat.id
    # Select a random live stream URL from the list
    selected_url = random.choice(YOUTUBE_LIVE_URLS)
    await message.reply(f"Now playing live stream: {selected_url}")

    # Let userbot stream the YouTube audio
    await stream_youtube_audio(userbot, selected_url, chat_id)
