from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.utils.errors import capture_err


@app.on_message(
    filters.command("webss", prefixes=["/", "!", "%", ",", "", ".", "@", "#"])
)
@capture_err
async def take_ss(_, message: Message):
    try:
        if len(message.command) != 2:
            return await message.reply_text("**» ɢɪᴠᴇ ᴀ ᴜʀʟ ᴛᴏ ғᴇᴛᴄʜ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        url = message.text.split(None, 1)[1]
        m = await message.reply_text("**» ᴛʀʏɪɴɢ ᴛᴏ ᴛᴀᴋᴇ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        await m.edit("**» ᴜᴩʟᴏᴀᴅɪɴɢ ᴄᴀᴩᴛᴜʀᴇᴅ sᴄʀᴇᴇɴsʜᴏᴛ...**")
        try:
            await message.reply_photo(
                photo=f"https://webshot.amanoteam.com/print?q={url}",
                quote=False,
            )
        except TypeError:
            return await m.edit("**» ɴᴏ sᴜᴄʜ ᴡᴇʙsɪᴛᴇ.**")
        await m.delete()
    except Exception as e:
        await message.reply_text(str(e))


__MODULE__ = "Web Ss"
__HELP__ = """
**Web Screenshot**

This command allows users to take a screenshot of a webpage and send it as a photo.

Features:
- Reply to the command with a URL to take a screenshot of that webpage and send it as a photo.

Commands:
- /webss <url>: Take a screenshot of the provided URL and send it as a photo.

Example:
- /webss <url>: Takes a screenshot of the provided URL and sends it as a photo.

Note: This command uses an external service to take screenshots of webpages.
"""
