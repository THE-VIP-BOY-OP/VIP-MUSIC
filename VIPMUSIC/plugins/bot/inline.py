#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#


from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultPhoto,
)
from youtubesearchpython.__future__ import VideosSearch

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.utils.inlinequery import answer


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            description = f"{views} | {duration} Mins | {channel}  | {published}"
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ",
                            url=link,
                        )
                    ],
                ]
            )
            searched_text = f"""
❇️**ᴛɪᴛʟᴇ:** [{title}]({link})

⏳**ᴅᴜʀᴀᴛɪᴏɴ:** {duration} Mins
👀**ᴠɪᴇᴡs:** `{views}`
⏰**ᴘᴜʙʟɪsʜᴇᴅ ᴛɪᴍᴇ:** {published}
🎥**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** {channel}
📎**ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [ᴠɪsɪᴛ ғʀᴏᴍ ʜᴇʀᴇ]({channellink})

__ʀᴇᴘʟʏ ᴡɪᴛʜ /play ᴏɴ ᴛʜɪs sᴇᴀʀᴄʜᴇᴅ ᴍᴇssᴀɢᴇ ᴛᴏ sᴛʀᴇᴀᴍ ɪᴛ ᴏɴ ᴠᴏɪᴄᴇᴄʜᴀᴛ.__

⚡️ ** ɪɴʟɪɴᴇ sᴇᴀʀᴄʜ ʙʏ {app.mention} **"""
            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=answers)
        except:
            return
