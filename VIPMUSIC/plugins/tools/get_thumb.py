from pyrogram import filters
from VIPMUSIC import app

@app.on_message(filters.command("gethumb", prefixes="/"))
async def get_thumbnail_command(client, message):
    try:
        if len(message.text.split(" ")) < 2:
            await message.reply("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴠᴀʟɪᴅ ʏᴏᴜᴛᴜʙᴇ ᴜʀʟ.")
            return
        
        url = message.text.split(" ")[1]
        video_id = url.split("v=")[-1] 
        if "&" in video_id:
            video_id = video_id.split("&")[0]
        query = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        await message.reply_photo(query)
    except Exception as e:
        await message.reply(f"An error occurred: {e}")
