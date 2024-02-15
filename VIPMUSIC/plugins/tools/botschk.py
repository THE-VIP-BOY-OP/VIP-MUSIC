import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app
from datetime import datetime

# Assuming BOT_LIST is defined elsewhere
BOT_LIST = ["TG_VC_BOT"]

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

        for bot_username in BOT_LIST:
            await userbot.one.send_message(bot_username, "/start")
            await asyncio.sleep(1)  # Delay between each bot

        # Update last checked time
        last_checked_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

        await message.reply_text(f"Bots checked successfully! Last checked time: {last_checked_time}")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botschk command: {e}")
    finally:
        # Stop the Pyrogram client after sending messages
        await userbot.one.stop()
