import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (get_active_chats, get_authuser_names, get_client,get_served_chats, get_served_users)
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.formatters import alpha_to_int
from config import adminlist
import config
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Global variables
AUTO_BROADCAST_MESSAGE = ""
IS_AUTO_BROADCASTING = False

# Command to start/stop auto-broadcasting
@app.on_message(filters.command(["autobroadcast", "ab"]))
async def toggle_auto_broadcast(_, message: Message):
    global IS_AUTO_BROADCASTING, AUTO_BROADCAST_MESSAGE
    
    if len(message.command) < 2:
        await message.reply_text("Usage: /autobroadcast [on/off] [message]")
        return

    action = message.command[1].lower()

    if action == "on":
        if len(message.command) < 3:
            await message.reply_text("Please provide a message to broadcast.")
            return
        AUTO_BROADCAST_MESSAGE = message.text.split(None, 2)[2]
        IS_AUTO_BROADCASTING = True
        await message.reply_text("Auto-broadcasting started.")
    elif action == "off":
        IS_AUTO_BROADCASTING = False
        await message.reply_text("Auto-broadcasting stopped.")
    else:
        await message.reply_text("Unknown action. Usage: /autobroadcast [on/off] [message]")

# Function to handle auto-broadcasting
async def auto_broadcast():
    global IS_AUTO_BROADCASTING, AUTO_BROADCAST_MESSAGE
    
    while IS_AUTO_BROADCASTING:
        served_chats = []
        schats = await get_served_chats()
        
        for chat in schats:
            served_chats.append(int(chat["chat_id"]))
            
        for chat_id in served_chats:
            try:
                await app.send_message(chat_id, text=AUTO_BROADCAST_MESSAGE)
            except Exception as e:
                print(f"Error broadcasting message to chat {chat_id}: {str(e)}")

            # Wait for a random duration between 1 to 10 seconds before sending the next message
            await asyncio.sleep(random.randint(1, 10))

        await asyncio.sleep(AUTO_BROADCAST_INTERVAL)

async def start_auto_broadcast():
    await app.start()
    await auto_broadcast()

# Run the auto-broadcasting loop within the existing event loop
loop = asyncio.get_event_loop()
loop.create_task(start_auto_broadcast())
