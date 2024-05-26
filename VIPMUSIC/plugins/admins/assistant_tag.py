import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.enums import ParseMode
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.database import get_assistant

SPAM_CHATS = []


@app.on_message(
    filters.command(["aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"])
    & admin_filter
)
async def tag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text("Give some text to tag all, like: @aall Hi Friends")
        return

    if replied:
        chat_id = message.chat.id
        text = replied.text if replied.text else replied.caption
        user_mentions = ""
        async for member in app.iter_chat_members(chat_id):
            user_mentions += f'<a href="tg://user?id={member.user.id}">{member.user.first_name}</a>\n'
        await userbot.send_message(
            chat_id, f"{text}\n{user_mentions}", parse_mode="HTML"
        )
    else:
        text = message.text.split(None, 1)[1]
        chat_id = message.chat.id
        user_mentions = ""
        async for member in app.get_chat_members(chat_id):
            user_mentions += f'<a href="tg://user?id={member.user.id}">{member.user.first_name}</a>\n'
        await userbot.send_message(
            chat_id, f"{text}\n{user_mentions}", parse_mode="HTML"
        )


@app.on_message(
    filters.command(
        [
            "astopmention",
            "aoffall",
            "acancel",
            "aallstop",
            "astopall",
            "acancelmention",
            "aoffmention",
            "amentionoff",
            "aalloff",
            "acancelall",
            "aallcancel",
        ],
        prefixes=["/", "@", "#"],
    )
    & admin_filter
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return
