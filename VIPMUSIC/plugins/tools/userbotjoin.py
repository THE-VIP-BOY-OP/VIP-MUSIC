import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from VIPMUSIC.utils.database import get_assistant
links = {}


@app.on_message(filters.group & filters.command(["userbotjoin", f"userbotjoin@{app.username}"]) & ~filters.private)
async def join_group(client, message):
    chat_id = message.chat.id
    userbot = await get_assistant(message.chat.id)
    
    if message.chat.username:
        try:
            await userbot.join_chat(message.chat.username)
            await message.reply("Successfully joined!")
        except ChatAdminRequired:
            await message.reply_text("Make Me Admin For Invite My Assistant")
            return
        except UserNotParticipant:
            member = await app.get_chat_member(chat_id, userbot.id)
            if member.status in (ChatMemberStatus.BANNED, ChatMemberStatus.RESTRICTED):
                try:
                    await app.unban_chat_member(chat_id, userbot.id)
                except Exception as e:
                    await message.reply("Assistant is banned, unban it firstly.")
                    return
                invite_link = await app.create_chat_invite_link(chat_id)
                await userbot.join_chat(invite_link.invite_link)
                await message.reply("Assistant was banned, now unbanned, and joined!")
            else:
                await message.reply("Assistant is banned, unban it firstly.")
    else:
        try:
            invite_link = await app.create_chat_invite_link(chat_id)
            await userbot.join_chat(invite_link.invite_link)
            await message.reply("Bot's assistant joined successfully!")
        except ChatAdminRequired:
            await message.reply("I am not admin.")

        
@app.on_message(filters.command("userbotleave") & filters.group & admin_filter)
async def leave_one(client, message):
    try:
        userbot = await get_assistant(message.chat.id)
        await userbot.leave_chat(message.chat.id)
        await app.send_message(message.chat.id, "✅ Userbot Successfully Left Chat")
    except Exception as e:
        print(e)


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **Userbot** Leaving All Chats !")
    try:
        userbot = await get_assistant(message.chat.id)
        async for dialog in userbot.one.get_dialogs():
            if dialog.chat.id == -1001733534088:
                continue
            try:
                await userbot.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
                )
            await asyncio.sleep(3)
    finally:
        await app.send_message(
            message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
        )
