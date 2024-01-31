import asyncio
import datetime
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.database import get_served_chats
from VIPMUSIC import app 

LOGS = -1001443337704  # Move LOGS definition to the module level

AM = """**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs.💌

🎵 24×7 ᴜᴘᴛɪᴍᴇ\n🎧 ʟᴀɢ ғʀᴇᴇ\n🎧 ᴀᴅᴠᴀɴᴄᴇᴅ & ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs**

<b><u>**sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.

ᴜꜱᴇ /start**"""

ok = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_message(chat_id, AM, reply_markup=ok)
                    await asyncio.sleep(1)  # Sleep for 1 second between sending messages
                except Exception as e:
                    print(f"An error occurred while sending message to chat ID {chat_id}: {e}")
            else:
                print(f"Invalid chat_id type for chat_info {chat_info}: {type(chat_id)}")
    except Exception as e:
        print(f"An error occurred while fetching served chats: {e}")

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(300)  # Sleep for 1 hour (3600 seconds)

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())

# Run the application
app.run()
