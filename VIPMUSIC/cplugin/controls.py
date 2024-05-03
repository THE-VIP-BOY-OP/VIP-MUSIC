import logging
from pytgcalls.types import MediaStream, AudioQuality
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from .play import pytgcalls
from .utils import (
    admin_check,
    close_key,
    is_streaming,
    stream_off,
    stream_on,
    is_active_chat,
)
from .utils.active import _clear_
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.thumbnails import gen_thumb
from YukkiMusic.misc import clonedb


@Client.on_message(filters.command(["pause", "resume", "end", "stop"]) & filters.group)
async def pause_str(client, message: Message):
    try:
        await message.delete()
    except:
        pass
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("ʙᴏᴛ ɪsɴ'ᴛ sᴛʀᴇᴀᴍɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.")
    check = await client.get_chat_member(message.chat.id, message.from_user.id)

    if (
        check.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
        or message.from_user.id not in SUDOERS
    ):
        return await message.reply_text(
            "» ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs."
        )

    admin = (
        await client.get_chat_member(message.chat.id, message.from_user.id)
    ).privileges
    if not admin.can_manage_video_chats:
        return await message.reply_text(
            "» ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴍᴀɴᴀɢᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛs, ᴘʟᴇᴀsᴇ sᴛᴀʏ ɪɴ ʏᴏᴜʀ ʟɪᴍɪᴛs."
        )
    if message.text.lower() == "/pause":
        if not await is_streaming(message.chat.id):
            return await message.reply_text(
                "ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ʀᴇsᴜᴍᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?"
            )
        await pytgcalls.pause_stream(message.chat.id)
        await stream_off(message.chat.id)
        return await message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ ᴩᴀᴜsᴇᴅ 🥺\n└ʙʏ : {message.from_user.mention} 🥀",
        )
    elif message.text.lower() == "/resume":

        if await is_streaming(message.chat.id):
            return await message.reply_text(
                "ᴅɪᴅ ʏᴏᴜ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ʏᴏᴜ ᴘᴀᴜsᴇᴅ ᴛʜᴇ sᴛʀᴇᴀᴍ ?"
            )
        await stream_on(message.chat.id)
        await pytgcalls.resume_stream(message.chat.id)
        return await message.reply_text(
            text=f"➻ sᴛʀᴇᴀᴍ ʀᴇsᴜᴍᴇᴅ 💫\n│ \n└ʙʏ : {message.from_user.mention} 🥀",
        )
    elif message.text.lower() == "/end" or message.text.lower() == "/stop":
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
        except:
            pass

        return await message.reply_text(
            text=f"➻ **sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ/sᴛᴏᴩᴩᴇᴅ** ❄\n│ \n└ʙʏ : {message.from_user.mention} 🥀",
        )
