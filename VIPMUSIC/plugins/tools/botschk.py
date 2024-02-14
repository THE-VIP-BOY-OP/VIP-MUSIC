import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config

BOT_LIST = ["TG_VC_BOT"]  # List of bots to check

load_dotenv()

# Initialize Pyrogram clients for assistants
assistants = []

class Userbot(Client):
    def __init__(self, name, session_string):
        super().__init__(name, session_string=session_string)

async def check_bots():
    for assistant_id in assistantids:
        try:
            assistant_client = Userbot(f"VIPAss{assistant_id}", session_string=config.STRING_SESSION)
            await assistant_client.start()
            await asyncio.sleep(2)  # Delay to avoid spamming
            for bot_username in BOT_LIST:
                try:
                    await assistant_client.send_message(bot_username, "/start")
                    await asyncio.sleep(1)  # Delay between each bot
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                except Exception as e:
                    print(f"Error sending /start message to bot {bot_username} via assistant {assistant_id}: {e}")
            await assistant_client.stop()
        except Exception as e:
            print(f"Error with assistant {assistant_id}: {e}")

from VIPMUSIC import app

@app.on_message(filters.command("botschk") & filters.private)
async def check_bots_command(client, message):
    await check_bots()
    await message.reply_text("Bots checked successfully!")

if __name__ == "__main__":
    # Add your assistant ids here
    assistantids = [1, 2, 3, 4, 5]

    app.run()
