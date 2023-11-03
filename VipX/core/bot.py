
import sys

from pyrogram import Client
from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class VipXBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"😛𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐁𝐚𝐛𝐲😜")
        super().__init__(
            "VipXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )
        try:
            os.system(f"rm -rf VipXMusic.session")

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║┣⪼🥀𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲🎉\n║\n║◈ {config.MUSIC_BOT_NAME}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠😍\n║\n╚══════════════❍⊱❁"
            )
            
        except:
            LOGGER(__name__).error(
                "🤬𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐀𝐝𝐝𝐞𝐝 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩, 𝐆𝐨 𝐀𝐧𝐝 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐭 𝐖𝐨𝐫𝐤🤬"
            )
            
        if config.SET_CMDS == str(True):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("start", "❥ ✨ᴛᴏ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ✨"),
                        BotCommand("ping", "❥ 🍁ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ🍁"),
                        BotCommand("help", "❥ 🥺ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ🥺"),
                        BotCommand("vctag", "❥ 😇ᴛᴀɢᴀʟʟ ғᴏʀ ᴠᴄ🙈"),
                        BotCommand("stopvctag", "❥ 📍sᴛᴏᴘ ᴛᴀɢᴀʟʟ ғᴏʀ ᴠᴄ 💢"),
                        BotCommand("tagall", "❥ 🔻ᴛᴀɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ʙʏ ᴛᴇxᴛ🔻"),
                        BotCommand("cancel", "❥ 🔻ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴛᴀɢɢɪɴɢ🔻"),
                        BotCommand("settings", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴇᴛᴛɪɴɢs🔻"),
                        BotCommand("reload", "❥ 🪐ᴛᴏ ʀᴇʟᴏᴀᴅ ᴛʜᴇ ʙᴏᴛ🪐"),
                        BotCommand("play", "❥ ❣️ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ sᴏɴɢ❣️"),
                        BotCommand("vplay", "❥ ❣️ᴛᴏ ᴘʟᴀʏ ᴛʜᴇ ᴍᴜsɪᴄ ᴡɪᴛʜ ᴠɪᴅᴇᴏ❣️"),
                        BotCommand("pause", "❥ 🥀ᴛᴏ ᴘᴀᴜsᴇ ᴛʜᴇ sᴏɴɢs🥀"),
                        BotCommand("resume", "❥ 💖ᴛᴏ ʀᴇsᴜᴍᴇ ᴛʜᴇ sᴏɴɢ💖"),
                        BotCommand("end", "❥ 🐚ᴛᴏ ᴇᴍᴘᴛʏ ᴛʜᴇ ϙᴜᴇᴜᴇ🐚"),
                        BotCommand("queue", "❥ 🤨ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ϙᴜᴇᴜᴇ🤨"),
                        BotCommand("playlist", "❥ 🕺ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴘʟᴀʏʟɪsᴛ🕺"),
                        BotCommand("stop", "❥ ❤‍🔥ᴛᴏ sᴛᴏᴘ ᴛʜᴇ sᴏɴɢs❤‍🔥"),
                        BotCommand("lyrics", "❥ 🕊️ᴛᴏ ɢᴇᴛ ᴛʜᴇ ʟʏʀɪᴄs🕊️"),
                        BotCommand("song", "❥ 🔸ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ sᴏɴɢ🔸"),
                        BotCommand("video", "❥ 🔸ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛʜᴇ ᴠɪᴅᴇᴏ sᴏɴɢ🔸"),
                        BotCommand("gali", "❥ 🔻ᴛᴏ ʀᴇᴘʟʏ ғᴏʀ ғᴜɴ🔻"),
                        BotCommand("shayri", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴀ sʜᴀʏᴀʀɪ🔻"),
                        BotCommand("love", "❥ 🔻ᴛᴏ ɢᴇᴛ ᴀ ʟᴏᴠᴇ sʜᴀʏᴀʀɪ🔻"),
                        BotCommand("sudolist", "❥ 🌱ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ sᴜᴅᴏʟɪsᴛ🌱"),
                        BotCommand("owner", "❥ 💝ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴏᴡɴᴇʀ💝"),
                        BotCommand("update", "❥ 🐲ᴛᴏ ᴜᴘᴅᴀᴛᴇ ʙᴏᴛ🐲"),
                        BotCommand("gstats", "❥ 💘ᴛᴏ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ💘"),
                        BotCommand("repo", "❥ 🍌ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ 𝚁𝙴𝙿𝙾🍌")
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "🤐𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩, 𝐆𝐨 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐭 𝐖𝐨𝐫𝐤🤬"
            )
            
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"🎉𝐘𝐨𝐮𝐫 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲 \n🥀𝐍𝐚𝐦𝐞:- {self.name}")
