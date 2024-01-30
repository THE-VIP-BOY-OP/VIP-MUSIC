from pyrogram import filters
from pyrogram.types import Message
from strings import get_string, helpers
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import add_sudo, remove_sudo
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.extraction import extract_user
from VIPMUSIC.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@app.on_message(filters.command(["addsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(_["sudo_1"].format(user.mention))
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & filters.user(OWNER_ID))
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(_["sudo_3"].format(user.mention))
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention))
    else:
        await message.reply_text(_["sudo_8"])



photo_url = "https://telegra.ph/file/20b4a9fd06ea4a9457a61.jpg"

@app.on_message(filters.command(["sudolist", "listsudo", "sudoers"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, _):
    keyboard = []

    user = await app.get_users(OWNER_ID)
    user_mention = user.mention if user else f"🌹 Oᴡɴᴇʀ ɪᴅ ➥ `{OWNER_ID}`"
    caption = f"**๏ ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs ๏ **\n\n**🌹 ᴏᴡɴᴇʀ** ➥ {user_mention}\n\n"

    keyboard.append([InlineKeyboardButton("๏ ᴠɪᴇᴡ ᴏᴡɴᴇʀ ๏", url=f"tg://openmessage?user_id={OWNER_ID}")])

    count = 1
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user_mention = user.mention if user else f"**🎁 Sᴜᴅᴏ {count} ɪᴅ:** {user_id}"
                caption += f"**🎁 Sᴜᴅᴏ** {count}: {user_mention}\n"
                button_text = f"๏ ᴠɪᴇᴡ sᴜᴅᴏ {count} ๏ "
                keyboard.append([InlineKeyboardButton(button_text, url=f"tg://openmessage?user_id={user_id}")])
                count += 1
            except:
                continue

    if keyboard:
        reply_markup = InlineKeyboardMarkup(keyboard)
        await message.reply_photo(photo=photo_url, caption=caption, reply_markup=reply_markup)
    else:
        await message.reply_text(_["sudo_7"])

