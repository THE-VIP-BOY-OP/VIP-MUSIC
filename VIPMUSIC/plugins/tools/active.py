from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from unidecode import unidecode

from VIPMUSIC import app
from VIPMUSIC.core.call import _st_ as clean
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    get_active_chats,
    get_active_video_chats,
    get_assistant,
    is_active_chat,
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


@app.on_message(
    filters.command(
        ["activevc", "activevoice"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    )
    & SUDOERS
)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    buttons = []

    # Loop through each active chat and check if the userbot is in the voice chat
    for x in served_chats:
        try:
            userbot = await get_assistant(x)
            call_participants_id = [
                member.chat.id async for member in userbot.get_call_members(x)
            ]

            if await is_active_chat(x) and userbot.id in call_participants_id:
                chat_info = await app.get_chat(x)
                title = chat_info.title
                invite_link = await generate_join_link(x)

                if chat_info.username:
                    user = chat_info.username
                    text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
                else:
                    text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"

                button_text = f"๏ ᴊᴏɪɴ {ordinal(j + 1)} ɢʀᴏᴜᴘ ๏"
                buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
                j += 1
            else:
                await remove_active_chat(x)
        except:
            await remove_active_chat(x)
            continue

    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs :</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )


@app.on_message(
    filters.command(
        ["activev", "activevideo"], prefixes=["/", "!", "%", ",", "", ".", "@", "#"]
    )
    & SUDOERS
)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ɢᴇᴛᴛɪɴɢ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʟɪsᴛ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    buttons = []

    # Loop through each active video chat and check if the userbot is in the video chat
    for x in served_chats:
        try:
            userbot = await get_assistant(x)
            call_participants_id = [
                member.chat.id async for member in userbot.get_call_members(x)
            ]

            if await is_active_chat(x) and userbot.id in call_participants_id:
                chat_info = await app.get_chat(x)
                title = chat_info.title
                invite_link = await generate_join_link(x)

                if chat_info.username:
                    user = chat_info.username
                    text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
                else:
                    text += f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"

                button_text = f"๏ ᴊᴏɪɴ {ordinal(j + 1)} ɢʀᴏᴜᴘ ๏"
                buttons.append([InlineKeyboardButton(button_text, url=invite_link)])
                j += 1
            else:
                await remove_active_video_chat(x)
        except:
            await remove_active_video_chat(x)
            continue

    if not text:
        await mystic.edit_text(f"» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ᴏɴ {app.mention}.")
    else:
        await mystic.edit_text(
            f"<b>» ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs :</b>\n\n{text}",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    active_chats = await get_active_chats()
    active_video_chats = await get_active_video_chats()
    ok = await message.reply_text("**ғᴇᴛᴄʜɪɴɢ....**")

    valid_audio_chats = []
    valid_video_chats = []

    for chat_id in active_chats:
        userbot = await get_assistant(chat_id)
        call_participants_id = [
            member.chat.id async for member in userbot.get_call_members(chat_id)
        ]

        if await is_active_chat(chat_id) and userbot.id in call_participants_id:
            valid_audio_chats.append(chat_id)
        else:
            await clean(chat_id)

    for chat_id in active_video_chats:
        userbot = await get_assistant(chat_id)
        call_participants_id = [
            member.chat.id async for member in userbot.get_call_members(chat_id)
        ]

        if await is_active_chat(chat_id) and userbot.id in call_participants_id:
            valid_video_chats.append(chat_id)
        else:
            await clean(chat_id)

    ac_audio = str(len(valid_audio_chats))
    ac_video = str(len(valid_video_chats))

    await ok.delete()
    await message.reply_text(
        f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data=f"close")]]
        ),
    )


__MODULE__ = "Aᴄᴛɪᴠᴇ"
__HELP__ = """
## Aᴄᴛɪᴠᴇ Vᴏɪᴄᴇ/Vɪᴅᴇᴏ Cʜᴀᴛs Cᴏᴍᴍᴀɴᴅs

/activevc ᴏʀ /activevoice - Lɪsᴛs ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ɪɴ ᴀ sᴇʀᴠᴇᴅ ɢʀᴏᴜᴘs.

/activev ᴏʀ /activevideo - Lɪsᴛs ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ɪɴ ᴀ sᴇʀᴠᴇᴅ ɢʀᴏᴜᴘs.

/ac - Dɪsᴘᴀʏs ᴛʜᴇ ᴄᴏᴜɴᴛ ᴏғ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs.

**Nᴏᴛᴇs:**
- Oɴʏ SUDOERS ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
- Aᴜᴛᴏᴍᴀᴛɪᴄᴀʏ ɢᴇɴᴇʀᴀᴛᴇs ᴊᴏɪɴ ɪɴᴋs ғᴏʀ ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs.
"""
