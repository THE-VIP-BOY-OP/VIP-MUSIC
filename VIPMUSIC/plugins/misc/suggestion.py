import asyncio
from VIPMUSIC.utils.database import get_served_chats, get_served_users, get_sudoers
from VIPMUSIC import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def send_broadcast():
    while True:
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())

        ok = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
                ]
            ]
        )

        await app.send_message(message.chat.id, f"๏ ᴛʜɪs ɪs {app.mention}\n\n➻ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛs.💌\n\n🎵 24×7 ᴜᴘᴛɪᴍᴇ\n🎧 ʟᴀɢ ғʀᴇᴇ\n🎧 ᴀᴅᴠᴀɴᴄᴇᴅ & ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs\n\n<b><u>sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.\n\nᴜꜱᴇ /start\n\nʙᴏᴛ ᴜꜱᴇɴᴀᴍᴇ : @{app.username}", reply_markup=ok)
        
        await asyncio.sleep(30)

# Run the broadcast task
loop = asyncio.get_event_loop()
loop.create_task(send_broadcast())
loop.run_forever()
