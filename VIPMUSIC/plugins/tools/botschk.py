import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app
from datetime import datetime

# Assuming Userbot is defined elsewhere
userbot = Userbot()

last_checked_time = None

@app.on_message(filters.command("botschk") & filters.group)
async def check_bots_command(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        await userbot.one.start()

        # Get current time before sending messages
        start_time = datetime.now()

        # Extract bot username from command
        command_parts = message.command
        if len(command_parts) == 2:
            bot_username = command_parts[1]
            await userbot.one.send_message(bot_username, "/start")
            await asyncio.sleep(1)  # Delay between each bot

            # Check if bot responded to /start message
            response = await client.get_chat_member(message.chat.id, bot_username)
            if response and response.status not in ("kicked", "left"):
                status_message = "And bot is active."
            else:
                status_message = "And bot is not responding or is inactive."

            # Update last checked time
            last_checked_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

            await message.reply_text(f"Bots checked successfully! {status_message} Last checked time: {last_checked_time}")
        else:
            await message.reply_text("Invalid command format. Please use /botschk <bot_username>")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botschk command: {e}")
    finally:
        # Stop the Pyrogram client after sending messages
        await userbot.one.stop()
