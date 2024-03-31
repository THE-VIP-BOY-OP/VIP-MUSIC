from pyrogram import Client, filters
from youtubesearchpython.__future__ import VideosSearch

from VIPMUSIC import app

# Command handler for /getthumbnail
@app.on_message(filters.command("getthumb", prefixes="/"))
async def get_thumbnail_command(client, message):
    try:
        # Extract video ID from the command
        video_id = message.text.split(maxsplit=1)[1]
        
        # Search for the video using video ID
        query = f"https://www.youtube.com/watch?v={video_id}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail_url = result["thumbnails"][0]["url"].split("?")[0]
        
        # Send the thumbnail as a photo
        await message.reply_photo(thumbnail_url)
    except Exception as e:
        await message.reply(f"An error occurred: {e}")
