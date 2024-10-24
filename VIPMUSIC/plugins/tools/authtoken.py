from VIPMUSIC import app
import os

@app.on_message(filters.command("authtoken"))
async def list_formats(client, message):
    try:
        youtube_url = "https://www.youtube.com/watch?v=LLF3GMfNEYU"
        
        await message.reply_text("**Go to Logs and verify to google account then save token data in variable**")
        
        command = f"yt-dlp -F {youtube_url}"
        
        result = os.popen(command).read()
        
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

