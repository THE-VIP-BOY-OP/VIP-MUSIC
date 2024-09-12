from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import BANNED_USERS, OWNER_ID
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import add_sudo, remove_sudo
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.extraction import extract_user


@app.on_message(
    filters.command(["addsudo"], prefixes=["/", "!", "%", ",", ".", "@", "#"])
    & filters.user(OWNER_ID)
)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id in SUDOERS:
        return await message.reply_text(
            _["sudo_1"].format(user.mention or user.first_name)
        )
    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(_["sudo_2"].format(user.mention or user.first_name))
    else:
        await message.reply_text(_["sudo_8"])


@app.on_message(
    filters.command(["delsudo", "rmsudo"], prefixes=["/", "!", "%", ",", ".", "@", "#"])
    & filters.user(OWNER_ID)
)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
    user = await extract_user(message)
    if user.id not in SUDOERS:
        return await message.reply_text(
            _["sudo_3"].format(user.mention or user.first_name)
        )
    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(_["sudo_4"].format(user.mention or user.first_name))
    else:
        await message.reply_text(_["sudo_8"])


photo_url = "https://telegra.ph/file/20b4a9fd06ea4a9457a61.jpg"


@app.on_message(
    filters.command(
        ["sudolist", "listsudo", "sudoers"],
        prefixes=["/", "!", "%", ",", ".", "@", "#"],
    )
    & ~BANNED_USERS
)
async def sudoers_list(client, message: Message):
    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]
    ]
    reply_markups = InlineKeyboardMarkup(keyboard)
    await message.reply_photo(
        photo=photo_url,
        caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ",
        reply_markup=reply_markups,
    )


@app.on_callback_query(filters.regex("^check_sudo_list$"))
async def check_sudo_list(client, callback_query: CallbackQuery):
    keyboard = []
    if callback_query.from_user.id not in SUDOERS:
        return await callback_query.answer(
            "You are not authorized to view the sudo list.", show_alert=True
        )
    else:
        user = await app.get_users(OWNER_ID)
        user_mention = user.mention or user.first_name
        caption = f"**˹ʟɪsᴛ ᴏғ ʙᴏᴛ ᴍᴏᴅᴇʀᴀᴛᴏʀs˼**\n\n**🌹Oᴡɴᴇʀ** ➥ {user_mention}\n\n"

        keyboard.append(
            [
                InlineKeyboardButton(
                    "๏ ᴠɪᴇᴡ ᴏᴡɴᴇʀ ๏", url=f"tg://openmessage?user_id={OWNER_ID}"
                )
            ]
        )

        count = 1
        for user_id in SUDOERS:
            if user_id != OWNER_ID:
                try:
                    user = await app.get_users(user_id)
                    user_mention = user.mention or f"**🎁 Sᴜᴅᴏ {count} ɪᴅ:** {user_id}"
                    caption += f"**🎁 Sᴜᴅᴏ** {count} **»** {user_mention}\n"
                    button_text = f"๏ ᴠɪᴇᴡ sᴜᴅᴏ {count} ๏ "
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                button_text, url=f"tg://openmessage?user_id={user_id}"
                            )
                        ]
                    )
                    count += 1
                except:
                    continue

        # Add a "Back" button at the end
        keyboard.append(
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="back_to_main_menu")]
        )

        if keyboard:
            reply_markup = InlineKeyboardMarkup(keyboard)
            await callback_query.message.edit_caption(
                caption=caption, reply_markup=reply_markup
            )


@app.on_callback_query(filters.regex("^back_to_main_menu$"))
async def back_to_main_menu(client, callback_query: CallbackQuery):
    keyboard = [
        [InlineKeyboardButton("๏ ᴠɪᴇᴡ sᴜᴅᴏʟɪsᴛ ๏", callback_data="check_sudo_list")]
    ]
    reply_markups = InlineKeyboardMarkup(keyboard)
    await callback_query.message.edit_caption(
        caption="**» ᴄʜᴇᴄᴋ sᴜᴅᴏ ʟɪsᴛ ʙʏ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ.**\n\n**» ɴᴏᴛᴇ:**  ᴏɴʟʏ sᴜᴅᴏ ᴜsᴇʀs ᴄᴀɴ ᴠɪᴇᴡ. ",
        reply_markup=reply_markups,
    )


__MODULE__ = "Sudolist"
__HELP__ = """
- `/addsudo`: Add a user as sudoer.
- `/delsudo`: Remove a user from sudoers.
- `/sudolist`: View the list of sudoers.

# Commands for SUDOERS:
"""
