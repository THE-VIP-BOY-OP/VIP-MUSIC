import sys

from pyrogram import Client

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
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "administrator":
            LOGGER(__name__).error(
                "🤐𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩, 𝐆𝐨 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐭 𝐖𝐨𝐫𝐤🤬"
            )
            
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
        try:
            await self.send_message(
                config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} 𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐛𝐚𝐛𝐲🤩 **\n\n✨ 𝐈𝐃 : `{self.id}`\n🥰𝐍𝐀𝐌𝐄 : {self.name}\n💫 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : @{self.username}"
            )
        except:
            LOGGER(__name__).error(
                "🤬𝐘𝐨𝐮𝐫 𝐁𝐨𝐭 𝐈𝐬 𝐍𝐨𝐭 𝐀𝐝𝐝𝐞𝐝 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩, 𝐆𝐨 𝐀𝐧𝐝 𝐀𝐝𝐝 𝐁𝐨𝐭 𝐈𝐧 𝐋𝐨𝐠𝐠𝐞𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐎𝐭𝐡𝐞𝐫𝐰𝐢𝐬𝐞 𝐁𝐨𝐭 𝐖𝐢𝐥𝐥 𝐍𝐨𝐭 𝐖𝐨𝐫𝐤🤬"
            )
            
