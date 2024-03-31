import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app
from datetime import datetime
from VIPMUSIC.utils.database import get_assistant
from telegraph import Telegraph  # Import Telegraph library
import os

last_checked_time = None

@app.on_message(filters.command("botchat") & filters.group)
async def check_bots_command(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        userbot = await get_assistant(message.chat.id)

        # Get current time before sending messages
        start_time = datetime.now()

        # Extract bot username and limit from command
        command_parts = message.command
        if len(command_parts) >= 2:
            bot_username = command_parts[1]
            limit = int(command_parts[2]) if len(command_parts) >= 3 else 10
            response = ""  # Define response variable
            try:
                bot = await userbot.get_users(bot_username)
                bot_id = bot.id
                await asyncio.sleep(0.5)
                
                # Get chat history with specified limit
                async for bot_message in userbot.get_chat_history(bot_id, limit=limit):
                    if bot_message.from_user.id == bot_id:
                        response += f"{bot_message.text}\n"
                    else:
                        line = f"{bot_message.from_user.first_name}: {bot_message.text}\n"
                        if bot_message.photo or bot_message.video:
                            # Create a Telegraph link for photo or video
                            media_link = await create_telegraph_media_link(bot_message)
                            if media_link:
                                line += f"Media: {media_link}\n"
                        response += line
            except Exception:
                response += f"Unable to fetch chat history for {bot_username}."
            # Update last checked time
            last_checked_time = start_time.strftime("%Y-%m-%d")
            # Save conversation to a text file
            filename = f"{bot_username}_chat.txt"
            with open(filename, "w") as file:
                file.write(response)
            await message.reply_text(f"Conversation saved to {filename}\nLast checked: {last_checked_time}")
            # Send the text file
            await message.reply_document(document=filename)
            os.remove(filename)  # Delete the file after sending
        else:
            await message.reply_text("Invalid command format.\n\nPlease use /botchat Bot_Username [limit]\n\nExample: `/botchat @example_bot 10`")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botchat command: {e}")

async def create_telegraph_media_link(message: Message) -> str:
    """
    Create a Telegraph link for photo or video message.
    """
    file_path = None
    if message.photo:
        file_path = message.photo.file_id
    elif message.video:
        file_path = message.video.file_id
    
    if file_path:
        media_url = await app.download_media(file_path)
        telegraph = Telegraph()
        telegraph.create_account(short_name='pyrogram')
        response = telegraph.upload_file(media_url)
        return response["url"]
    return ""
