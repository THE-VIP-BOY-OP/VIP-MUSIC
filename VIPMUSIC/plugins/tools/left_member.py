from VIPMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

# -------------

@app.on_chat_member_updated(filters.group, group=20)
async def member_has_left(client: app, member: ChatMemberUpdated):

    if (
        not member.new_chat_member
        and member.old_chat_member.status not in {
            "banned", "left", "restricted"
        }
        and member.old_chat_member
    ):
        pass
    else:
        return

    user = (
        member.old_chat_member.user
        if member.old_chat_member
        else member.from_user
    )

    try:
        # Add the photo path, caption, and button details
        photo_path = "https://telegra.ph/file/7e1f95dbfd13fb5d51539.jpg"
        caption = f"**Goodbye {user.mention}!**"
        button_text = "View Member"

        # Generate a deep link to open the user's profile
        deep_link = f"tg://user?id={user.id}"

        # Send the message with the photo, caption, and button
        await client.send_photo(
            chat_id=member.chat.id,
            photo=photo_path,
            caption=caption,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(button_text, url=deep_link)]
            ])
        )
    except RPCError as e:
        print(e)
        return
  
