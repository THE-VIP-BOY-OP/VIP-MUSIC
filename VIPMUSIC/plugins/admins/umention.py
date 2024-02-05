import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from datetime import datetime


SPAM_CHATS = []



# A set to keep track of users who are mentioned
mentioned_users = set()

# Function to send mention message to all users in a chat
async def send_mention_message(chat_id, message_text):
    async for member in app.iter_chat_members(chat_id):
        if member.user.is_bot:
            continue
        try:
            await app.send_message(chat_id, f"@{member.user.username} {message_text}")
            await asyncio.sleep(1)  # Delay to avoid flooding
        except Exception as e:
            print(f"Error sending message to user {member.user.id}: {str(e)}")

# Function to start unlimited mentioning
async def start_unlimited_mention(chat_id, message_text):
    global mentioned_users
    mentioned_users = set()
    while True:
        if mentioned_users:
            await send_mention_message(chat_id, message_text)
        await asyncio.sleep(1)  # Check every second if new users have been added to the set

# Command to start unlimited mentioning
@app.on_message(filters.command(["unlimitedmention"], prefixes="/") & filters.me)
async def start_unlimited_mention_command(_, message):
    global mentioned_users
    chat_id = message.chat.id
    if len(message.command) > 1:
        message_text = " ".join(message.command[1:])
    else:
        message_text = "You've been mentioned!"
    await message.reply_text("Unlimited mentioning started!")
    mentioned_users = set()
    asyncio.create_task(start_unlimited_mention(chat_id, message_text))

# Command to stop unlimited mentioning

@app.on_message(filters.command(["stopunlimitedmention"], prefixes="/") & filters.me)
async def stop_unlimited_mention_command(_, message):
    global mentioned_users
    await message.reply_text("Unlimited mentioning stopped!")
    mentioned_users = set()

app.run()
