from pyrogram import Client, filters
from pyrogram.types import Message
from VIPMUSIC import app


@app.on_message(filters.command(["dice", "ludo"]))
async def dice(c, m: Message):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
    await dicen.reply_text("results is {0}".format(dicen.dice.value))
