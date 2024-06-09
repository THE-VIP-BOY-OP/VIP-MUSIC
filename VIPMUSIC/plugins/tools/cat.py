import requests
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

from config import BANNED_USERS
from VIPMUSIC import app

close_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="Rᴇғʀᴇsʜ", callback_data="refresh_cat")],
        [InlineKeyboardButton(text="〆 ᴄʟᴏsᴇ 〆", callback_data="close")],
    ]
)


@app.on_message(filters.command("cat") & ~BANNED_USERS)
async def cat(c, m: Message):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await m.reply_animation(
                cat_url, caption="meow", reply_markup=close_keyboard
            )
        else:
            await m.reply_photo(cat_url, caption="meow", reply_markup=close_keyboard)
    else:
        await m.reply_text("Failed to fetch cat picture 🙀")


@app.on_callback_query(filters.regex("refresh_cat") & ~BANNED_USERS)
async def refresh_cat(c, m: CallbackQuery):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await m.edit_caption_animation(
                cat_url, caption="meow", reply_markup=close_keyboard
            )
        else:
            await m.edit_message_media(
                InputMediaPhoto(media=cat_url, caption="meow"),
                reply_markup=close_keyboard,
            )
    else:
        await m.edit_message_text("Failed to refresh cat picture 🙀")


__MODULE__ = "Cat"
__HELP__ = """
## Cat Command

### Command: /cat
**Description:**
Fetches a random cat picture or GIF from The Cat API and sends it in the chat.

**Usage:**
/cat

**Details:**
- Displays a random cat image or GIF.
- Includes buttons for refreshing the cat image or closing the message.

**Examples:**
- /cat: Sends a random cat picture or GIF.

**Notes:**
- Users who are banned will not be able to use this command.

### Buttons:
- **Refresh:** Gets a new cat image or GIF.
- **Close:** Closes the cat image message.
"""
