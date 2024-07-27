import asyncio
import importlib

from pyrogram import idle

import config
from config import BANNED_USERS
from VIPMUSIC import HELPABLE, LOGGER, app, userbot
from VIPMUSIC.core.call import VIP
from VIPMUSIC.misc import sudo
from VIPMUSIC.plugins import ALL_MODULES
from VIPMUSIC.plugins.tools.clone import restart_bots
from VIPMUSIC.utils.database import get_banned_users, get_gbanned


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        imported_module = importlib.import_module(all_module)

        if hasattr(imported_module, "__MODULE__") and imported_module.__MODULE__:
            if hasattr(imported_module, "__HELP__") and imported_module.__HELP__:
                if imported_module.__MODULE__.lower() not in HELPABLE:
                    HELPABLE[imported_module.__MODULE__.lower()] = imported_module
                else:
                    raise Exception(
                        f"Can't have two plugins with same name! '{imported_module.__MODULE__}' Please Change One"
                    )

    LOGGER("VIPMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")

    await userbot.start()

    await VIP.start()
    await VIP.decorators()
    await restart_bots()
    LOGGER("VIPMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗩𝗜𝗣 𝗕𝗢𝗬♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("VIPMUSIC").info(
        "                 ╔═════ஜ۩۞۩ஜ════╗\n  ♨️𝗠𝗔𝗗𝗘 𝗕𝗬 𝗩𝗜𝗣 𝗕𝗢𝗬♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )


if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(init())
