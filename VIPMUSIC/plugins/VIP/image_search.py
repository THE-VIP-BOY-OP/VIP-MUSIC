from pyrogram import filters
from pyrogram.types import InputMediaPhoto
from requests import get

from VIPMUSIC import app


@app.on_message(
    filters.command(["image"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
async def pinterest(_, message):
    chat_id = message.chat.id

    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply("**ɢɪᴠᴇ ɪᴍᴀɢᴇ ɴᴀᴍᴇ ғᴏʀ sᴇᴀʀᴄʜ 🔍**")

    images = get(f"https://pinterest-api-one.vercel.app/?q={query}").json()

    media_group = []
    count = 0

    msg = await message.reply(f"sᴄʀᴀᴘɪɴɢ ɪᴍᴀɢᴇs ғʀᴏᴍ ᴘɪɴᴛᴇʀᴇᴛs...")
    for url in images["images"][:6]:

        media_group.append(InputMediaPhoto(media=url))
        count += 1
        await msg.edit(f"=> ᴏᴡᴏ sᴄʀᴀᴘᴇᴅ ɪᴍᴀɢᴇs {count}")

    try:

        await app.send_media_group(
            chat_id=chat_id, media=media_group, reply_to_message_id=message.id
        )
        return await msg.delete()

    except Exception as e:
        await msg.delete()
        return await message.reply(f"ᴇʀʀᴏʀ : {e}")


__MODULE__ = "Image Search"
__HELP__ = """
**Pinterest Image Search**

This command allows users to search for images on Pinterest and sends a collection of up to 6 images.

Features:
- Reply to the command with a query to search for images related to that query on Pinterest.
- Sends up to 6 images found on Pinterest related to the query.

Commands:
- /image <query>: Search for images related to the provided query on Pinterest.

Example:
- /image <query>: Searches for images related to the provided query on Pinterest and sends up to 6 images.

Note: This command uses an external Pinterest API to fetch images.
"""
