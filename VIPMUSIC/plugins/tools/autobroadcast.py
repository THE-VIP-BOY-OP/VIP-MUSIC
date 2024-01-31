import asyncio
from pyrogram import filters
from pyrogram.types import Message
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import get_served_chats

# Global variables
AUTO_BROADCAST_INTERVAL = 300  # Interval in seconds (adjust as needed)
AUTO_BROADCAST_MESSAGE = ""
IS_AUTO_BROADCASTING = False

# Command to start/stop auto-broadcasting
@app.on_message(filters.command(["autobroadcast", "ab"]) & SUDOERS)
async def toggle_auto_broadcast(_, message: Message):
    global IS_AUTO_BROADCASTING
    global AUTO_BROADCAST_MESSAGE

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
async def auto_broadcast(is_auto_broadcasting):
    while is_auto_broadcasting:
        served_chats = await get_served_chats()
        for chat in served_chats:
            chat_id = chat["chat_id"]
            try:
                await app.send_message(chat_id, text=AUTO_BROADCAST_MESSAGE)
            except Exception as e:
                print(f"Error broadcasting message to chat {chat_id}: {str(e)}")

        await asyncio.sleep(AUTO_BROADCAST_INTERVAL)

# Start auto-broadcasting loop
asyncio.create_task(auto_broadcast(IS_AUTO_BROADCASTING))
