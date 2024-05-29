import logging
from inspect import getfullargspec

from pyrogram import Client, filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    approve_pmpermit,
    disapprove_pmpermit,
    is_on_off,
    is_pmpermit_approved,
)

flood = {}
ASSISTANT_PREFIX = "."


@Client.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~SUDOERS
)
async def awaiting_message(client, message):
    if await is_on_off(2):
        try:
            await message.forward(LOG_GROUP_ID)
        except Exception as err:
            logging.exception(err)
    user_id = message.from_user.id
    if await is_pmpermit_approved(user_id):
        return
    async for m in client.get_chat_history(user_id, limit=6):
        if m.reply_markup:
            await m.delete()
    if str(user_id) in flood:
        flood[str(user_id)] += 1
    else:
        flood[str(user_id)] = 1
    if flood[str(user_id)] > 5:
        await message.reply_text("Spam Detected. User Blocked")
        await client.send_message(
            LOG_GROUP_ID,
            f"**Spam Detect Block On Assistant**\n\n- **Blocked User:** {message.from_user.mention}\n- **User ID:** {message.from_user.id}",
        )
        return await client.block_user(user_id)
    await message.reply_text(
        f"Hello, I am {app.mention} Assistant.\n\nPlease dont spam here , else you'll get blocked.\nFor more Help start :- {app.mention}"
    )


@Client.on_message(
    filters.command(["a", "approve"], prefixes=ASSISTANT_PREFIX)
    & SUDOERS
    & ~filters.via_bot
)
@Client.on_message(
    filters.command(["a", "approve"], prefixes=ASSISTANT_PREFIX)
    & filters.user("me")
    & ~filters.via_bot
)
async def pm_approve(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to approve.")
    user_id = message.reply_to_message.from_user.id
    if await is_pmpermit_approved(user_id):
        return await eor(message, text="User is already approved to pm")
    await approve_pmpermit(user_id)
    await eor(message, text="User is approved to pm")


@Client.on_message(
    filters.command("disapprove", prefixes=ASSISTANT_PREFIX)
    & filters.user("me")
    & ~filters.via_bot
)
@Client.on_message(
    filters.command("disapprove", prefixes=ASSISTANT_PREFIX)
    & SUDOERS
    & ~filters.via_bot
)
async def pm_disapprove(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to disapprove.")
    user_id = message.reply_to_message.from_user.id
    if not await is_pmpermit_approved(user_id):
        await eor(message, text="User is already disapproved to pm")
        async for m in client.iter_history(user_id, limit=6):
            if m.reply_markup:
                try:
                    await m.delete()
                except Exception:
                    pass
        return
    await disapprove_pmpermit(user_id)
    await eor(message, text="User is disapproved to pm")


@Client.on_message(
    filters.command("block", prefixes=ASSISTANT_PREFIX)
    & ~filters.via_bot
    & filters.user("me")
)
@Client.on_message(
    filters.command("block", prefixes=ASSISTANT_PREFIX) & SUDOERS & ~filters.via_bot
)
async def block_user_func(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to block.")
    user_id = message.reply_to_message.from_user.id
    await eor(message, text="Successfully blocked the user")
    await client.block_user(user_id)


@Client.on_message(
    filters.command("unblock", prefixes=ASSISTANT_PREFIX)
    & ~filters.via_bot
    & filters.user("me")
)
@Client.on_message(
    filters.command("unblock", prefixes=ASSISTANT_PREFIX) & SUDOERS & ~filters.via_bot
)
async def unblock_user_func(client, message):
    if not message.reply_to_message:
        return await eor(message, text="Reply to a user's message to unblock.")
    user_id = message.reply_to_message.from_user.id
    await client.unblock_user(user_id)
    await eor(message, text="Successfully Unblocked the user")


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
