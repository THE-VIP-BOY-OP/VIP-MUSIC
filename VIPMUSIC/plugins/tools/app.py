from pyrogram import filters

# Replace these with your own API ID, API HASH, and Bot Token
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_assistant

# Replace with your destination channel username or ID
destination_channel = ""

# Initialize the Pyrogram Client


@app.on_message(filters.command("forwad"))
def forward_messages(client, message):
    userbot = await get_assistant(message.chat.id)
    # Get the source channel ID from where the command was issued
    source_channel = ""

    # Fetch all messages from the source channel
    messages = client.get_chat_history(
        source_channel, limit=100
    )  # Adjust limit as needed

    # Forward each message to the destination channel
    for msg in messages:
        userbot.forward_messages(destination_channel, source_channel, msg.message_id)

    # Send a confirmation message to the user
    userbot.send_message(
        chat_id=source_channel, text="Messages have been forwarded successfully!"
    )


# Start the bot
