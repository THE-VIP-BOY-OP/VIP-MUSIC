
import asyncio
import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_command, get_string
from VipX import Telegram, YouTube, app
from VipX.misc import SUDOERS, _boot_
from VipX.plugins.playlist import del_plist_msg
from VipX.plugins.sudoers import sudoers_list
from VipX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from VipX.utils.decorators.language import LanguageStart
from VipX.utils.formatters import get_readable_time
from VipX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            await message.reply_sticker("CAACAgEAAxkBAAEIS2FkHfJQpbvRTfhyfS67BxulycCtegAC-gADUSkNORIJSVEUKRrhLwQ")
            return await message.reply_photo(
                       photo=config.START_IMG_URL,
                       caption=_["help_1"].format(config.SUPPORT_HEHE), reply_markup=keyboard
            )
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                f"🥱 𝐆𝐞𝐭𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐏𝐞𝐫𝐬𝐨𝐧𝐚𝐥 𝐒𝐭𝐚𝐭𝐬 𝐅𝐫𝐨𝐦 {config.MUSIC_BOT_NAME} sᴇʀᴠᴇʀ."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ](https://t.me/TG_FRIENDSS) ** ᴩʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) ** played {count} times**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(
                    None, get_stats
                )
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐓𝐡𝐞 𝐕𝐢𝐩 𝐁𝐨𝐭 𝐓𝐨 𝐂𝐡𝐞𝐜𝐤 𝐒𝐨𝐧𝐠 𝐈𝐧𝐟𝐨 <code>𝐒𝐮𝐝𝐨𝐥𝐢𝐬𝐭</code>\n\n**𝐔𝐒𝐄𝐑 𝐈𝐃:-** {sender_id}\n**𝐍𝐀𝐌𝐄:-** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text(
                    "𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐆𝐞𝐭 𝐋𝐲𝐫𝐢𝐜𝐬🥺 𝐓𝐫𝐲 𝐀𝐠𝐚𝐢𝐧 𝐏𝐥𝐞𝐚𝐬𝐞🥀."
                )
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nᴛʜᴀɴᴋs ғᴏʀ ᴠᴇʀɪғʏɪɴɢ ʏᴏᴜʀsᴇʟғ ɪɴ {config.MUSIC_BOT_NAME}, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ɢᴏ ʙᴀᴄᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴜsɪɴɢ ᴍᴇ.")
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ <code>ᴠᴇʀɪғʏ ʜɪᴍsᴇʟғ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
            return
        if name[0:3] == "inf":
            m = await message.reply_text("🥀𝐒𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠 𝐅𝐨𝐫 𝐮𝐡....")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[
                    0
                ]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
ㅤㅤ**🔔 ❰ 𝐒ᴏɴɢ🎙𝐈ɴғᴏʀᴍᴀᴛɪᴏɴ ❱ 🔔**
        
★•.¸¸♡¸¸.•*¨*•☆•*♫*•.¸¸♡¸¸.•*☆*•.¸¸♡¸¸.•★
● 🎸 **𝐍𝐚𝐦𝐞 ➪ [{title}]({link})**　　
★ 　° :. ★　 ♫ • ○ ° ★ ☆ . * ● ¸ .✦ .✮
● 💽 **𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 ➪ [{duration} ᴍɪɴ.]({link})**☆¸¸♡¸¸★
★ 　° :. ★　 ♫ • ○ ° ★ ☆ . * ● ¸ .✦ .❊
● 🕹 **𝐕𝐢𝐞𝐰𝐬 ➪ [{views}]({link})**.♫.☆ ¸¸♡¸¸ ✭
•✰˚♫. * ● ¸ .★ .¸¸♡¸¸★ :●. ♫°☆ ¸. ● .. ✫
● ⏰ **𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐎𝐧 ➪ [{published}]({link})**. ✰
° °☆ 　¸. ● . .¸¸♡¸¸.★　★✰˚♫. ○  ✦ .✵
● 📺 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ➪ [{channel}]({link})**★
•✰˚♫. * ● ¸ . ★ .¸¸♡¸¸★ :●. *°☆ ¸. ● .. ✧
● 🗯 **𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐋𝐢𝐧𝐤 ➪ [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})**✰
•✰˚♫. * ● ¸ . ★ .¸¸♡¸¸★ :●. *°☆ ¸. ● .. ★
● 📡 **𝐋𝐢𝐧𝐤 ➪ [ᴡᴀᴛᴄʜ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})**☆.♡
•✰˚♫. * ● ¸ . ★ .¸¸♡¸¸★ :●. *°☆ ¸. ● .. ✷

☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🥀𝐘𝐎𝐔𝐓𝐔𝐁𝐄🥀", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🏓𝐒𝐔𝐏𝐏𝐎𝐑𝐓🏓", url="https://t.me/TG_FRIENDSS"
                        ),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐨𝐭 𝐓𝐨 𝐂𝐡𝐞𝐜𝐤<code>𝐒𝐨𝐧𝐠 𝐈𝐧𝐟𝐨</code>\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:-** {sender_id}\n**𝐍𝐚𝐦𝐞:-** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(
                        config.MUSIC_BOT_NAME
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    _["start_2"].format(config.MUSIC_BOT_NAME),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                _["start_2"].format(config.MUSIC_BOT_NAME),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} 𝐉𝐮𝐬𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐕𝐢𝐩 𝐁𝐨𝐭😍.\n\n**𝐔𝐬𝐞𝐫 𝐈𝐝:-** {sender_id}\n**𝐍𝐚𝐦𝐞:-** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND"))
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    OWNER = OWNER_ID[0]
    out = start_pannel(_, app.username, OWNER)
    return await message.reply_photo(
               photo=config.START_IMG_URL,
               caption=_["start_1"].format(
            message.chat.title, config.MUSIC_BOT_NAME
        ),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐕𝐢𝐩 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭**\n\n𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐓𝐡𝐞 𝐂𝐡𝐚𝐭𝐬 𝐀𝐥𝐥𝐨𝐰𝐞𝐝 𝐁𝐲 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫, 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 𝐈𝐧 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫'𝐬 𝐏𝐦 𝐓𝐨 𝐀𝐥𝐥𝐨𝐰 𝐘𝐨𝐮𝐫 𝐂𝐡𝐚𝐭 𝐀𝐧𝐝 𝐈𝐟 𝐘𝐨𝐮 𝐃𝐨𝐧𝐭 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐃𝐨 𝐓𝐡𝐞𝐧 𝐌𝐚𝐚 𝐂𝐡𝐮𝐝𝐚𝐨👿 𝐛𝐜𝐨𝐳 𝐈'𝐦 𝐋𝐞𝐚𝐯𝐢𝐧𝐠..."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != "supergroup":
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                OWNER = OWNER_ID[0]
                out = start_pannel(_, app.username, OWNER)
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(
                        config.MUSIC_BOT_NAME, member.mention
                    )
                )
            return
        except:
            return
