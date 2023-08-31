import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall
from VipX.misc import SUDOERS
import config
from config import BANNED_USERS
from VipX import LOGGER, app, userbot
from VipX.core.call import Vip
from VipX.plugins import ALL_MODULES
from VipX.utils.database import get_banned_users, get_gbanned


@app.on_message(
    filters.command("vcraid")
    & filters.group
    & ~filters.edited
    & ~SUDOERS

@PlayWrapper
async def play_commnd(
    client,
    message: Message,
    _,
    chat_id,
):

try:
        await Vip.stream_decall("https://telegra.ph/file/de3464aa7d6bfafdd2dc3.mp4")
    except:
        pass
    try:
        await Vip.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
