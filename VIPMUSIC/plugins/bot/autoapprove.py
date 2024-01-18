from VIPMUSIC import app
from os import environ
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InputMediaPhoto, InlineKeyboardButton, InlineKeyboardMarkup

# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hᴇʟʟᴏ {mention}\n Wᴇʟᴄᴏᴍᴇ Tᴏ {title}\n\n ")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Define an event handler for chat join requests
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: app, message: ChatJoinRequest):
    chat = message.chat  # Chat
    user = message.from_user  # User
    print(f"{user.first_name} Joined 🤝")  # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)

    if APPROVED == "on":
        # Get chat information to retrieve the group photo
        chat_info = await client.get_chat(chat.id)
        photo_path = chat_info.photo.big_file_id if chat_info.photo else None

        if photo_path:
            # Caption with button
            caption = TEXT.format(mention=user.mention, title=chat.title)
            button_text = "Your Button Text"
            button_data = "your_button_data"
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, callback_data=button_data)]])
            
            # Send message with group photo, caption, and button
            await client.send_photo(
                chat_id=chat.id,
                photo=photo_path,
                caption=caption,
                reply_markup=reply_markup
            )
        else:
            print("Group photo not available.")
