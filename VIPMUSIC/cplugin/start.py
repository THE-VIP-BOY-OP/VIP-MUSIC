from pyrogram import Client, filters
from pyrogram.enums import ChatType, ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
from YukkiMusic.utils.decorators.language import LanguageStart
from config import SUPPORT_GROUP, OWNER_ID, SUPPORT_CHANNEL, START_IMG_URL

PM_START_TEXT = """
ʜᴇʏ {0}, 🥀
๏ ᴛʜɪs ɪs** {1} !

➻ ᴀ ғᴀsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ.
"""

START_TEXT = """
**ʜᴇʏ** {0}, 🥀
  {1} ᴄᴀɴ ɴᴏᴡ ᴩʟᴀʏ sᴏɴɢs ɪɴ {2}.

──────────────────
➻ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʜᴇʟᴘ ᴀʙᴏᴜᴛ ᴍᴇ ᴏʀ ɪғ ʏᴏᴜ ᴡᴀɴɴᴀ ᴀsᴋ sᴏᴍᴇᴛʜɪɴɢ ʏᴏᴜ ᴄᴀɴ ᴊᴏɪɴ ᴍʏ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({3}).
"""


@Client.on_message(filters.command(["start"]) & ~filters.forwarded)
@Client.on_edited_message(filters.command(["start"]) & ~filters.forwarded)
@LanguageStart
async def clone_st(client, message: Message, _):
    viv = await client.get_me()
    if message.chat.type == ChatType.PRIVATE:
        if len(message.text.split()) > 1:
            cmd = message.text.split(None, 1)[1]
            if cmd[0:3] == "inf":
                m = await message.reply_text("🔎")
                query = (str(cmd)).replace("info_", "", 1)
                query = f"https://www.youtube.com/watch?v={query}"
                results = VideosSearch(query, limit=1)
                for result in (await results.next())["result"]:
                    title = result["title"]
                    duration = result["duration"]
                    views = result["viewCount"]["short"]
                    thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                    channellink = result["channel"]["link"]
                    channel = result["channel"]["name"]
                    link = result["link"]
                    published = result["publishedTime"]
                searched_text = f"""
➻ **ᴛʀᴀᴄᴋ ɪɴғᴏʀɴᴀᴛɪᴏɴ** 

📌 **ᴛɪᴛʟᴇ :** {title}

⏳ **ᴅᴜʀᴀᴛɪᴏɴ :** {duration} ᴍɪɴᴜᴛᴇs
👀 **ᴠɪᴇᴡs :** `{views}`
⏰ **ᴩᴜʙʟɪsʜᴇᴅ ᴏɴ :** {published}
🔗 **ʟɪɴᴋ :** [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})
🎥 **ᴄʜᴀɴɴᴇʟ :** [{channel}]({channellink})

💖 sᴇᴀʀᴄʜ ᴩᴏᴡᴇʀᴇᴅ ʙʏ {viv.name}"""
                key = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(text="ʏᴏᴜᴛᴜʙᴇ", url=link),
                            InlineKeyboardButton(text="sᴜᴩᴩᴏʀᴛ", url=SUPPORT_GROUP),
                        ],
                    ]
                )
                await m.delete()
                return await client.send_photo(
                    message.chat.id,
                    photo=thumbnail,
                    caption=searched_text,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup=key,
                )
        else:
            pm_buttons = [
                [
                    InlineKeyboardButton(
                        text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                        url=f"https://t.me/{viv.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="clone_help"
                    )
                ],
                [
                    InlineKeyboardButton(text="❄ ᴄʜᴀɴɴᴇʟ ❄", url=SUPPORT_CHANNEL),
                    InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=SUPPORT_GROUP),
                ],
            ]

            await message.reply_photo(
                photo=START_IMG_URL,
                caption=PM_START_TEXT.format(
                    message.from_user.first_name,
                    viv.mention,
                ),
                reply_markup=InlineKeyboardMarkup(pm_buttons),
            )
    else:
        gp_buttons = [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                    url=f"https://t.me/{viv.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(text="❄ ᴄʜᴀɴɴᴇʟ ❄", url=SUPPORT_CHANNEL),
                InlineKeyboardButton(text="✨ sᴜᴩᴩᴏʀᴛ ✨", url=SUPPORT_GROUP),
            ],
        ]

        await message.reply_photo(
            photo=START_IMG_URL,
            caption=START_TEXT.format(
                message.from_user.first_name,
                viv.mention,
                message.chat.title,
                SUPPORT_GROUP,
            ),
            reply_markup=InlineKeyboardMarkup(gp_buttons),
        )
