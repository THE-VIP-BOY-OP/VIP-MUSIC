import asyncio
from VIPMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from VIPMUSIC import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

id = -1001443337704

async def update_served_chats_count():
    while True:
        global served_chats
        served_chats = len(await get_served_chats())
        await asyncio.sleep(5)

async def send_broadcast():
    while True:
        global sent
        global pin
        global chats

        ok = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
                ]
            ]
        )

        message_text = f"๏ ᴛʜɪs ɪs {app.mention}\n\n➻ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs.💌\n\n🎵 24×7 ᴜᴘᴛɪᴍᴇ\n🎧 ʟᴀɢ ғʀᴇᴇ\n🎧 ᴀᴅᴠᴀɴᴄᴇᴅ & ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs\n\n<b><u>sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n\nᴜꜱᴇ /start\n\nʙᴏᴛ ᴜꜱᴇɴᴀᴍᴇ : @{app.username}"

        for chat_id in chats:
            try:
                await app.send_message(chat_id, message_text, reply_markup=ok)
                sent += 1
            except Exception as e:
                error_message = f"Failed to send message to chat_id {chat_id}: {e}"
                await app.send_message(id, error_message)

        await asyncio.sleep(5)

# Initialize global variables
served_chats = 0
sent = 0
pin = 0
chats = []

# Run the tasks
loop = asyncio.get_event_loop()
loop.create_task(update_served_chats_count())
loop.create_task(send_broadcast())
loop.run_forever()
