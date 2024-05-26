import requests
from pyrogram import filters
from pyrogram.types import CallbackQuery, InputMediaPhoto
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from pyrogram.types import Message
from VIPMUSIC import app
from config import BANNED_USERS

close_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="৻ꪆ Rᴇғʀᴇsʜ ৻ꪆ", callback_data="refresh_cat")],
        [InlineKeyboardButton(text="৻ꪆ ᴄʟᴏsᴇ ৻ꪆ", callback_data="close")],
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
                cat_url, caption="𝐌𝐄𝐎𝐖....😽💐", reply_markup=close_keyboard
            )
        else:
            await m.reply_photo(cat_url, caption="𝐌𝐄𝐎𝐖....😽💐", reply_markup=close_keyboard)
    else:
        await m.reply_text("Failed to fetch cat picture 🙀")


@app.on_callback_query(filters.regex("refresh_cat") & ~BANNED_USERS)
async def refresh_cat(c, m: CallbackQuery):
    r = requests.get("https://api.thecatapi.com/v1/images/search")
    if r.status_code == 200:
        data = r.json()
        cat_url = data[0]["url"]
        if cat_url.endswith(".gif"):
            await m.edit_message_animation(
                cat_url, caption="𝐌𝐄𝐎𝐖....😽💐", reply_markup=close_keyboard
            )
        else:
            await m.edit_message_media(
                InputMediaPhoto(media=cat_url, caption="𝐌𝐄𝐎𝐖....😽💐"),
                reply_markup=close_keyboard,
            )
    else:
        await m.edit_message_text("Failed to refresh cat picture 🙀")
