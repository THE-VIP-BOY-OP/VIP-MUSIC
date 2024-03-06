from VIPMUSIC.utils.vip_ban import admin_filter
import os
import csv
from pyrogram import Client, filters
from VIPMUSIC import app
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

@app.on_message(filters.command("user") & admin_filter)
async def user_command(client, message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    chat_members = await app.get_chat_members(message.chat.id)

    members_list = []
    for member in chat_members:
        members_list.append({
            "username": member.user.username,
            "userid": member.user.id
        })

    with open("members.txt", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["username", "userid"])
        writer.writeheader()
        for member in members_list:
            writer.writerow(member)

    # Send the text file as a reply to the message
    await app.send_document(message.chat.id, "members.txt")
