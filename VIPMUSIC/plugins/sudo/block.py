from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import add_gban_user, remove_gban_user
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.extraction import extract_user
from config import BANNED_USERS


from time import time

# Define the list of specific commands to track for spamming
SPAM_COMMANDS = ["/play", "/start", "/stop"]  # Example commands

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}

# Modify the existing code
@app.on_message(filters.command(SPAM_COMMANDS) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in BANNED_USERS:
        return await message.reply_text(_["block_1"].format(user.mention))
    await add_gban_user(user.id)
    BANNED_USERS.add(user.id)
    await message.reply_text(_["block_2"].format(user.mention))

    # Additional code to track spamming
    user_id = message.from_user.id
    current_time = time()

    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 60:
        # If less than 60 seconds have passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > 5:
            # Block the user if they exceed the threshold
            await add_gban_user(user_id)
            BANNED_USERS.add(user_id)
            await client.send_message(user_id, "You have been blocked for spamming.")
    else:
        # If more than 60 seconds have passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

@app.on_message(filters.command(["unblock"]) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in BANNED_USERS:
        return await message.reply_text(_["block_3"].format(user.mention))
    await remove_gban_user(user.id)
    BANNED_USERS.remove(user.id)
    await message.reply_text(_["block_4"].format(user.mention))


@app.on_message(filters.command(["blocked", "blockedusers", "blusers"]) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = user.first_name if not user.mention else user.mention
            count += 1
        except:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)
