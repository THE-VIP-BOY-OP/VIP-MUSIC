from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from unidecode import unidecode

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    get_assistant,
    remove_active_chat,
    remove_active_video_chat,
)


async def generate_join_link(chat_id: int):
    invite_link = await app.export_chat_invite_link(chat_id)
    return invite_link


def ordinal(n):
    suffix = ["th", "st", "nd", "rd", "th"][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    return str(n) + suffix


async def is_userbot_in_call(chat_id):
    """Check if userbot is in the call (audio or video)."""
    try:
        userbot = await get_assistant(chat_id)
        userbot_id = userbot.id
        async for member in userbot.get_call_members(chat_id):
            if member.user.id == userbot_id:  # Userbot found in call
                return True
    except:
        return False
    return False


async def is_userbot_video_on(chat_id):
    """Check if userbot has video on in the call."""
    try:
        userbot = await get_assistant(chat_id)
        userbot_id = userbot.id
        async for member in userbot.get_call_members(chat_id):
            if (
                member.user.id == userbot_id and member.is_video_enabled
            ):  # Check if video is on
                return True
    except:
        return False
    return False


@app.on_message(
    filters.command(
        ["activevc", "activevoice"], prefixes=["/", "!", "%", ",", ".", "@", "#"]
    )
    & SUDOERS
)
async def activevc(_, message: Message):
    mystic = await message.reply_text(
        "» Checking active voice chats where the bot is present..."
    )

    userbot = await get_assistant(message.chat.id)  # Fetch userbot instance
    text = ""  # Initialize text variable
    buttons = []  # Initialize buttons list
    j = 0  # Counter for listing the chats

    async for (
        dialog
    ) in userbot.get_dialogs():  # Loop through all chats where userbot is a member
        chat_id = dialog.chat.id
        if await is_userbot_in_call(chat_id):  # Check if userbot is in a voice chat
            try:
                chat_info = await app.get_chat(chat_id)
                title = chat_info.title
                invite_link = await generate_join_link(chat_id)

                if chat_info.username:
                    user = chat_info.username
                    text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{chat_id}</code>]\n"
                else:
                    text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{chat_id}</code>]\n"

                button_text = f"๏ ᴊᴏɪɴ {ordinal(j + 1)} ɢʀᴏᴜᴘ ๏"
                buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
                j += 1
            except Exception:
                await remove_active_chat(chat_id)
                continue

    if not text:
        await mystic.edit_text(f"» No active voice chats where the bot is present.")
    else:
        await mystic.edit_text(
            f"<b>» List of active voice chats where the bot is present (audio/video):</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )


@app.on_message(
    filters.command(
        ["activev", "activevideo"], prefixes=["/", "!", "%", ",", ".", "@", "#"]
    )
    & SUDOERS
)
async def activevideo(_, message: Message):
    mystic = await message.reply_text(
        "» Checking active video chats where the bot's video is on..."
    )

    userbot = await get_assistant(message.chat.id)  # Fetch userbot instance
    text = ""  # Initialize text variable
    buttons = []  # Initialize buttons list
    j = 0  # Counter for listing the chats

    async for (
        dialog
    ) in userbot.get_dialogs():  # Loop through all chats where userbot is a member
        chat_id = dialog.chat.id
        if await is_userbot_video_on(chat_id):  # Check if userbot video is on
            try:
                chat_info = await app.get_chat(chat_id)
                title = chat_info.title
                invite_link = await generate_join_link(chat_id)

                if chat_info.username:
                    user = chat_info.username
                    text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{chat_id}</code>]\n"
                else:
                    text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{chat_id}</code>]\n"

                button_text = f"๏ ᴊᴏɪɴ {ordinal(j + 1)} ɢʀᴏᴜᴘ ๏"
                buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
                j += 1
            except Exception:
                await remove_active_video_chat(chat_id)
                continue

    if not text:
        await mystic.edit_text(f"» No active video chats where the bot's video is on.")
    else:
        await mystic.edit_text(
            f"<b>» List of active video chats where the bot's video is on:</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
