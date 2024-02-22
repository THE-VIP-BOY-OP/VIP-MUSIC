import os
import requests
from random import randint
from VIPMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, CallbackQuery,
                            InlineKeyboardMarkup, Message)
from VIPMUSIC.utils import close_markup
from config import BANNED_USERS, SERVER_PLAYLIST_LIMIT
from VIPMUSIC import Carbon, app
from VIPMUSIC.utils.decorators.language import language, languageCB
from VIPMUSIC.utils.inline.playlist import (botplaylist_markup,
                                              get_playlist_markup,
                                              warning_markup)
from VIPMUSIC.utils.pastebin import VIPBin
import time
import yt_dlp
from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch
from youtubesearchpython import SearchVideos

from VIPMUSIC.utils.stream.stream import stream
from typing import Dict, List, Union

from VIPMUSIC.core.mongo import mongodb



playlistdb = mongodb.playlist
playlist = []
# Playlist Databse


async def _get_playlists(chat_id: int) -> Dict[str, int]:
    _notes = await playlistdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_playlist_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_playlists(chat_id):
        _notes.append(note)
    return _notes


async def get_playlist(chat_id: int, name: str) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_playlist(chat_id: int, name: str, note: dict):
    name = name
    _notes = await _get_playlists(chat_id)
    _notes[name] = note
    await playlistdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )



async def delete_playlist(chat_id: int, name: str) -> bool:
    notesd = await _get_playlists(chat_id)
    name = name
    if name in notesd:
        del notesd[name]
        await playlistdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"notes": notesd}},
            upsert=True,
        )
        return True
    return False




# Command
ADDPLAYLIST_COMMAND = ("addplaylist")
PLAYLIST_COMMAND = ("playlist")
DELETEPLAYLIST_COMMAND = ("delplaylist")

import json
from pytube import Playlist
from pytube import YouTube

# Combined add_playlist function
@app.on_message(
    filters.command(ADDPLAYLIST_COMMAND)
    & ~BANNED_USERS
)
@language
async def add_playlist(client, message: Message, _):
    if len(message.command) < 2:
        return await message.reply_text("**➻ Please provide a song name or YouTube playlist link after the command**\n\n**➥ Examples:**\n1. `/addplaylist Blue Eyes` (Add a specific song)\n2. `/addplaylist [YouTube Playlist Link]` (Add all songs from a YouTube playlist)")

    query = message.command[1]
    
    # Check if the provided input is a YouTube playlist link
    if "playlist" in query:
        try:
            # Renamed the playlist variable to avoid confusion
            playlist_obj = Playlist(query)
            video_urls = playlist_obj.video_urls
        except Exception as e:
            return await message.reply_text(f"Error: {e}")

        if not video_urls:
            return await message.reply_text("No videos found in the playlist.")

        user_id = message.from_user.id
        for video_url in video_urls:
            video_id = video_url.split("v=")[-1]
            try:
                yt = YouTube(video_url)
                title = yt.title
                duration = yt.length
            except Exception as e:
                # Handling errors gracefully
                print(f"Error fetching video info: {e}")
                continue  # Continue with the next video if an error occurs
            
            plist = {
                "videoid": video_id,
                "title": title,
                "duration": duration,
            }
            await save_playlist(user_id, video_id, plist)

        return await message.reply_text("Playlist added successfully.")
    else:
        # Add a specific song by name (to be implemented)
        query = " ".join(message.command[1:])
        print(query)
        # Add code here to handle adding a specific song by name
        # You can use a similar approach as in the YouTube playlist section
