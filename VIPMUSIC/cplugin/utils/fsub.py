from pyrogram.errors import ChatAdminRequired, UserNotParticipant
from config import LOGGER_ID
from pyrogram.enums import ChatMemberStatus
from VIPMUSIC.utils.database import get_assistant

async def is_joined(user_id):
    userbot = await get_assistant(LOGGER_ID)
    try:
        a = await userbot.get_chat_member(LOGGER_ID, userbot.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            return True
    except Exception:
    	return True
    try:
        try:
            await userbot.get_chat_member(LOGGER_ID, user_id)
            return True
        except UserNotParticipant:
        	return False
    except ChatAdminRequired:
        return True
