from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from VipX import app
from VipX.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
╔════❰𝐏𝐋𝐀𝐘𝐈𝐍𝐆❱═══❍⊱❁۪۪

◈ 𝐂𝐡𝐚𝐭 ➪ **{message.chat.title}**

◈ 𝐂𝐡𝐚𝐭 𝐈𝐝 ➪ `{message.chat.id}`

◈ 𝐔𝐬𝐞𝐫 ➪ **{message.from_user.mention}**

◈ 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ➪ **@{message.from_user.username}**

◈ 𝐈𝐝 ➪ `{message.from_user.id}`

◈ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➪ **{chatusername}**

◈ 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 ➪ **{message.text}**

◈ 𝐁𝐲 ➪ **{streamtype} ▄ █ ▄ █ ▄**

╚═══❰ #𝐍𝐞𝐰𝐒𝐨𝐧𝐠 ❱══❍⊱❁۪۪"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
