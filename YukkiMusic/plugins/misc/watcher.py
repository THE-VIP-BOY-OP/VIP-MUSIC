#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#
from pyrogram import filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from YukkiMusic import app
from YukkiMusic.core.call import Yukki


@app.on_message(filters.video_chat_started, group=20)
@app.on_message(filters.video_chat_ended, group=30)
@app.on_message(filters.left_chat_member)
async def force_stop_stream(_, message: Message):
    try:
        if message.left_chat_member and not message.left_chat_member is None:
            if message.left_chat_member.id == (await get_assistant(message.chat.id)).id:
                return await Yukki.force_stop_stream(message.chat.id)
        await Yukki.force_stop_stream(message.chat.id)
    except Exception as e:
        await app.send_message(LOG_GROUP_ID, f"error in wathcher.py error is {e}")
