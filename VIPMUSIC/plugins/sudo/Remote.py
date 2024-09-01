from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatPrivileges, Message

from config import OWNER_ID
from VIPMUSIC import app


@app.on_message(filters.command("addme") & filters.user(OWNER_ID))
async def rpromote(client, message: Message):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ Group id.")

    if user_id.startswith("@"):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"

    AMBOT = await message.reply_text(
        f"#ʀᴇᴍᴏᴛᴇ_ᴘʀᴏᴍᴏᴛᴇ\nᴘʀᴏᴍᴏᴛᴇ ᴜꜱᴇʀ : {mention}\nᴛᴀʀɢᴇᴛ ɢʀᴏᴜᴘ ɪᴅ : <code>{group_id}</code>\n\n"
    )

    try:
        await app.promote_chat_member(
            group_id,
            user_id,
            privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
            ),
        )
        await app.set_administrator_title(group_id, user_id, "AMBOT OP")
    except RPCError as e:
        await AMBOT.edit(f"An error occurred: {str(e)}")
        return

    await AMBOT.edit(
        f"#ʀᴇᴍᴏᴛᴇ_ᴘʀᴏᴍᴏᴛᴇᴅ\nᴘʀᴏᴍᴏᴛᴇᴅ ᴜꜱᴇʀ : {mention}\nᴛᴀʀɢᴇᴛ ɢʀᴏᴜᴘ ɪᴅ : <code>{group_id}</code>\n\n"
    )


@app.on_message(filters.command("demoteme") & filters.user(OWNER_ID))
async def rpromote(client, message: Message):
    try:
        user_id, group_id = message.text.split(maxsplit=2)[1:]
    except ValueError:
        return await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ Group id.")

    if user_id.startswith("@"):
        user = await client.get_users(user_id)
        user_id = user.id
        mention = user.mention
    else:
        user = await client.get_users(int(user_id))
        first_name = user.first_name
        user_id = user.id
        mention = f"<a href=tg://user?id={user_id}>{first_name}</a>"

    AMBOT = await message.reply_text(
        f"#ʀᴇᴍᴏᴛᴇ_ᴘʀᴏᴍᴏᴛᴇ\nᴘʀᴏᴍᴏᴛᴇ ᴜꜱᴇʀ : {mention}\nᴛᴀʀɢᴇᴛ ɢʀᴏᴜᴘ ɪᴅ : <code>{group_id}</code>\n\n"
    )

    try:
        await app.promote_chat_member(
            group_id,
            user_id,
            privileges=ChatPrivileges(
                can_change_info=False,
                can_invite_users=False,
                can_delete_messages=False,
                can_restrict_members=False,
                can_pin_messages=False,
                can_promote_members=False,
                can_manage_chat=False,
                can_manage_video_chats=False,
            ),
        )
    except RPCError as e:
        await AMBOT.edit(f"An error occurred: {str(e)}")
        return

    await AMBOT.edit(
        f"#ʀᴇᴍᴏᴛᴇ_ᴘʀᴏᴍᴏᴛᴇᴅ\nᴘʀᴏᴍᴏᴛᴇᴅ ᴜꜱᴇʀ : {mention}\nᴛᴀʀɢᴇᴛ ɢʀᴏᴜᴘ ɪᴅ : <code>{group_id}</code>\n\n"
    )
