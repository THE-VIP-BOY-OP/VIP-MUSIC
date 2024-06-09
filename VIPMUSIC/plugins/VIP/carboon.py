from io import BytesIO

import aiohttp
from pyrogram import filters

from VIPMUSIC import app


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("**ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ.**")
    text = await message.reply("Processing...")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit("**ᴜᴘʟᴏᴀᴅɪɴɢ...**")
    await message.reply_photo(carbon)
    await text.delete()
    carbon.close()


__MODULE__ = "Carbon"
__HELP__ = """
**Carbon Command**

This command allows users to create a Carbon image from a text message. Carbon is a tool for creating beautiful images of source code.

Features:
- Reply to a text message to generate a Carbon image from the message content.
- Supports both plain text and captioned messages.
- Displays a processing message while generating the Carbon image.
- Uploads the generated Carbon image as a reply to the original message.

Commands:
- /carbon: Reply to a text message to generate a Carbon image from the message content.

Note: Make sure to reply to a text message to generate the Carbon image successfully.
"""
