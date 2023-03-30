from pyrogram import Client, filters
from pyrogram.types import Message

from VCRAID import call_py, bot
from config import OWNER
from VCRAID.tgcalls.queues import QUEUE, clear_queue




@Client.on_message(filters.command(["stop"], prefixes=","))
async def stop(client, m: Message):
    await m.delete()
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await bot.send_message(OWNER, "lawda")
        except Expectations as e:
            await bot.send_message(OWNER, f"{e}")
