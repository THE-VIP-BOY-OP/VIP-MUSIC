from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid
from pytgcalls.exceptions import GroupCallNotFound

from VIPMUSIC import app
from VIPMUSIC.core.call import VIP


@app.on_message(
    filters.command(["voicechat", "vcusers", "vc", "vcuser"]) & filters.group
)
async def get_vc_users(client, message):
    try:
        A = await message.reply_text("🔍")
        AB = await VIP.get_participant(message.chat.id)
    except GroupCallNotFound:
        return await A.edit(
            "ᴍᴜsɪᴄ ɪs ɴᴏᴛ ᴘʟᴀʏɪɴɢ ʙʏ ʙᴏᴛ ᴛʜᴇʀᴇ ғᴏʀ Assɪsɪᴛᴀɴᴛ ɪs ᴜɴᴀʙʟᴇ ᴛᴏ ɢᴇᴛ ᴠᴏɪᴄᴇᴄʜᴀᴛ ᴜsᴇʀ's ʟɪsᴛ"
        )
    users_info = "ᴜsᴇʀs ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ"
    for participant in AB:
        user_id = participant.user_id
        try:
            user = await app.get_users(user_id)
            users_info += f"\n[{user.first_name}](tg://user?id={user_id})"
        except PeerIdInvalid:
            users_info += f"\n[ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ](tg://user?id={user_id})"
    if users_info == "ᴜsᴇʀs ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ":
        return await A.edit("🧐🧐ɴᴏ ᴏɴᴇ ɪɴ ᴠᴄ")
    await A.edit(users_info)
