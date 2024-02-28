import asyncio
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from VIPMUSIC import app
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.decorators.userbotjoin import UserbotWrapper

userbot = Userbot()

@app.on_message(filters.command(["userbotjoin", f"userbotjoin@{app.username}"]) & ~filters.private)
@UserbotWrapper
async def join_group(client, message):
    chid = message.chat.id
    try:
        await userbot.one.stop()
    except Exception as e:
        print(e)
        pass
    
    try:
        await userbot.one.start()
        invitelink = await app.export_chat_invite_link(chid)
        await userbot.one.join_chat(invitelink)
        await message.reply_text("**Userbot Successfully Entered Chat**")
    except Exception as e:
        print(e)
        pass

    # Userbot join karne ke baad, turant stop karna
    await userbot.one.stop()

        
@app.on_message(filters.command("userbotleave") & filters.group & admin_filter)
async def leave_one(client, message):
    try:
        await userbot.one.stop()
    except Exception as e:
        print(e)
        pass

    try:
        await userbot.one.start()
        await userbot.one.leave_chat(message.chat.id)
        await stop_userbot()
        await app.send_message(message.chat.id, "✅ Userbot Successfully Left Chat")
    except Exception as e:
        print(e)

    # Userbot leave karne ke baad, turant stop karna
    await userbot.one.stop()


@app.on_message(filters.command(["leaveall", f"leaveall@{app.username}"]) & SUDOERS)
async def leave_all(client, message):
    if message.from_user.id not in SUDOERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **Userbot** Leaving All Chats !")
    try:
        await userbot.one.stop()
    except Exception as e:
        print(e)
        pass

    try:
        await userbot.one.start()
        async for dialog in userbot.one.get_dialogs():
            if dialog.chat.id == -1001733534088:
                continue
            try:
                await userbot.one.leave_chat(dialog.chat.id)
                left += 1
                await lol.edit(
                    f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
                )
            except BaseException:
                failed += 1
                await lol.edit(
                    f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
                )
            await asyncio.sleep(2)
    finally:
        await userbot.one.stop()
        await app.send_message(
            message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
        )
