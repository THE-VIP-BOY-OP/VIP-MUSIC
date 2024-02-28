import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper
from VIPMUSIC.utils.database import get_assistant
links = {}


@app.on_message(filters.group & filters.command(["userbotjoin", f"userbotjoin@{app.username}"]) & ~filters.private)
async def join_group(client, message):
    userbot = await get_assistant(message.chat.id)
    if message.chat.username:
        # Userbot joins the username
        await userbot.join_chat(message.chat.username)
        await message.reply("Successfully joined!")
        return

    if not await app.get_chat_member(message.chat.id, "me").status in ["administrator", "creator"]:
        # Make me admin
        await message.reply("Make me admin for invite my assistant id.")

    elif userbot.id in message.chat.id:
        # Userbot already joined, no action required
        await message.reply("Bot's assistant already joined this group.")

    else:
        # Generate invite link and store it
        invite_link = await app.export_chat_invite_link(message.chat.id)
        links[message.chat.id] = invite_link
        # Userbot joins the group
        await userbot.join_chat(message.chat.id)
        await message.reply("Bot's assistant joined successfully!")


@app.on_message(filters.group)
async def check_member_status(client, message):
    if message.from_user.id == "assistant_user_id":
        if message.new_chat_members:
            for member in message.new_chat_members:
                if member.id == userbot.get_me().id:
                    await message.reply("Assistant already joined this group.")
                    return
    else:
        # Check if the assistant is banned or restricted
        member = await userbot.get_chat_member(message.chat.id, "assistant_user_id")
        if member.status in ["kicked", "restricted"]:
            await userbot.unban_chat_member(message.chat.id, "assistant_user_id")
            await message.reply("Assistant was banned, now unbanned.")
        else:
            await message.reply("Assistant is banned, unban it.")


        
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
