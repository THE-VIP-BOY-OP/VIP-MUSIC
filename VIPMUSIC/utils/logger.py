from pyrogram.enums import ParseMode

from VIPMUSIC import app
from VIPMUSIC.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝗗𝗫 𝗟𝗨𝗖𝗞𝗬 𝗣𝗟𝗔𝗬 𝗟𝗢𝗚</b>

<b>𝗖𝗛𝗔𝗧 𝗜𝗗 :</b> <code>{message.chat.id}</code>
<b>𝗖𝗛𝗔𝗧 𝗡𝗔𝗠𝗘 :</b> {message.chat.title}
<b>𝗖𝗛𝗔𝗧 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 :</b> @{message.chat.username}

<b>𝗨𝗦𝗘𝗥 𝗜𝗗 :</b> <code>{message.from_user.id}</code>
<b>𝗡𝗔𝗠𝗘 :</b> {message.from_user.mention}
<b>𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 :</b> @{message.from_user.username}

<b>𝗤𝗨𝗘𝗥𝗬 :</b> {message.text.split(None, 1)[1]}
<b>𝗦𝗧𝗥𝗘𝗔𝗠𝗧𝗬𝗣𝗘 :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
