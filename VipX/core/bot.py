
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
                        BotCommand("ping", "Check that bot is alive or dead"),
                        BotCommand("play", "Starts playing the requested song"),
                        BotCommand("skip", "Moves to the next track in queue"),
                        BotCommand("pause", "Pause the current playing song"),
                        BotCommand("resume", "Resume the paused song"),
                        BotCommand("end", "Clear the queue and leave voice chat"),
                        BotCommand("shuffle", "Randomly shuffles the queued playlist."),
                        BotCommand("playmode", "Allows you to change the default playmode for your chat"),
                        BotCommand("settings", "Open the settings of the music bot for your chat.")
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
