from pyrogram import filters, Client
from VIPMUSIC import app, api, userbot


async def get_advice():
    b = await api.advice()
    c = b["advice"]
    return c


@Client.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)
