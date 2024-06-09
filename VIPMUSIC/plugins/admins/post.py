from pyrogram import filters

from config import OWNER_ID
from VIPMUSIC import app


async def post_message(message, destination_group_id):
    if message.reply_to_message:
        await message.reply_to_message.copy(destination_group_id)
        await message.reply_text(f"Messages copied to group ID: {destination_group_id}")
    else:
        await message.reply_text("Please reply to a message to post it.")


@app.on_message(filters.command(["post"], prefixes=["/", "."]) & filters.user(OWNER_ID))
async def handle_post_command(_, message):

    if len(message.command) == 1:
        await message.reply_text("Please provide the channel ID after the command.")
        return

    destination_group_id = message.command[1]
    try:
        destination_group_id = int(destination_group_id)
        await post_message(message, destination_group_id)
    except ValueError:
        await message.reply_text(
            "Invalid channel ID. Please provide a valid numeric ID."
        )


__MODULE__ = "Post"
__HELP__ = """
**Post Messages**

This module allows the owner to copy messages from one chat to another.

Commands:
- /post: Replies to a message to copy it to a predefined destination group.

Note:
- Only the owner of the bot can use this command.
- Replace the `destination_group_id` variable with the desired destination group ID.
"""
