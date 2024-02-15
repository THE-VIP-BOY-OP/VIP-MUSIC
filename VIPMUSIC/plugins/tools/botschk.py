import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app

from pyrogram import Client, filters

from pyrogram import Client, filters

# Other imports...

# Assuming BOT_LIST is defined elsewhere
BOT_LIST = ["TG_VC_BOT"]

# Assuming Userbot is defined elsewhere
userbot = Userbot()

@app.on_message(filters.command("botschks") & filters.group)
async def check_bots_command(client, message):
    try:
        # Start the Pyrogram client
        await userbot.one.start()

        for bot_username in BOT_LIST:
            await userbot.one.send_message(bot_username, "/start")
            await asyncio.sleep(1)  # Delay between each bot

        await message.reply_text("Bots checked successfully!")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botschk command: {e}")
    finally:
        # Stop the Pyrogram client after sending messages
        await userbot.one.stop()
