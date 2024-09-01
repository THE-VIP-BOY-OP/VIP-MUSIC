import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from TeamSuperBan import app
from TeamSuperBan.utils import get_readable_time
from TeamSuperBan.utils.database import get_served_chats

from config import GBAN_USERS


@app.on_message(filters.command(["rstats", "allstats"]) & filters.user(GBAN_USERS))
async def all_stats(client, message: Message):
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = get_readable_time(len(served_chats))
    SKY = await message.reply_text(
        "Getting all real stats of {0}\n\nTime to take: {1}".format(
            app.mention, time_expected
        )
    )
    admin_chats = 0
    admin_not = 0
    chat_not = 0
    for chat_id in served_chats:
        try:
            member = await app.get_chat_member(chat_id, app.me.id)
            if member.status == ChatMemberStatus.ADMINISTRATOR:
                admin_chats += 1
            else:
                admin_not += 1
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except Exception as e:
            chat_not += 1
            continue

    await SKY.edit(
        "Real stats of {0}\n\nAdmin in chats: {1}\nNot admin in chats: {2}\nChats not accessible: {3}".format(
            app.mention, admin_chats, admin_not, chat_not
        )
    )
