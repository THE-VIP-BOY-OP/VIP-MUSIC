import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC.utils.database import get_served_chats
from VIPMUSIC import app 
import datetime


AM = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ+ᴄʜᴀɴɴᴇʟ ᴠᴄ.💌

🎵 24×7 ᴜᴘᴛɪᴍᴇ + 🎧 ᴠᴘs ʜᴏsᴛᴇᴅ\n🎙 ᴘʟᴀʏ+ᴠᴘʟᴀʏ+ᴄᴘʟᴀʏ+ᴄᴠᴘʟᴀᴜ sʏsᴛᴇᴍ...**

<b><u>**sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ, ʟᴇғᴛ ᴍᴇᴍʙᴇʀ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ...**

ᴜꜱᴇ [/start](https://t.me/{app.username}?start=help)**

**➲ ʙᴏᴛ :** @{app.username}"""

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
                    await app.send_message(chat_id, AM, reply_markup=ok, disable_web_page_preview=True)
                    await asyncio.sleep(1)  # Sleep for 1 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(300)  # Sleep for 5 minutes (300 seconds)

# Start the continuous broadcast loop
asyncio.create_task(continuous_broadcast())
