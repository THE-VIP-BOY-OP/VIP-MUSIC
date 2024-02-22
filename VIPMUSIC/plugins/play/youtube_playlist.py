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
    if "youtube.com/playlist" in query:
        try:
            playlist = Playlist(query)
            video_urls = playlist.video_urls
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
                return await message.reply_text(f"Error fetching video info: {e}")
            
            plist = {
                "videoid": video_id,
                "title": title,
                "duration": duration,
            }
            await save_playlist(user_id, video_id, plist)

        return await message.reply_text("Playlist added successfully.")
    else:
        # Add a specific song by name
        query = " ".join(message.command[1:])
        print(query)

        # Code for adding a specific song by name (similar to your previous implementation)...
      
