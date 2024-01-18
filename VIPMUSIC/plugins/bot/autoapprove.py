from VIPMUSIC import app
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

# Extract environment variables or provide default values
chat_id_env = environ.get("CHAT_ID")
CHAT_ID = [int(app) for app in chat_id_env.split(",")] if chat_id_env else []

TEXT = environ.get("APPROVED_WELCOME_TEXT", "Hᴇʟʟᴏ {mention}\n Wᴇʟᴄᴏᴍᴇ Tᴏ {title}\n\n ")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# List of random photo links
random_photo_links = [
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    "https://telegra.ph/file/ca950c0b8316b968957fa.jpg",
    # Add more links as needed
]

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
            # Load the group photo using the file ID
            group_photo = await client.download_media(photo_path)
            
            # Draw on the group photo
            group_photo_with_text = draw_text_on_photo(group_photo, user.mention, chat.title)
            
            # Caption with button
            caption = TEXT.format(mention=user.mention, title=chat.title)
            button_text = "Your Button Text"
            button_data = "your_button_data"
            reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(button_text, callback_data=button_data)]])
            
            # Send the modified group photo with caption and button
            await client.send_photo(
                chat_id=chat.id,
                photo=BytesIO(group_photo_with_text),
                caption=caption,
                reply_markup=reply_markup
            )
        else:
            # If group photo is not available, send a random photo
            random_photo = random.choice(random_photo_links)
            await client.send_photo(chat_id=chat.id, photo=random_photo, caption=TEXT.format(mention=user.mention, title=chat.title))

def draw_text_on_photo(photo_path, mention, title):
    # Open the image using PIL
    image = Image.open(photo_path)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Choose a font and size
    font = ImageFont.load_default()
    
    # Specify the text and position
    text = f"Welcome {mention}\nTo {title}"
    position = (10, 10)
    
    # Draw the text on the image
    draw.multiline_text(position, text, font=font, fill="white")
    
    # Save the modified image to a BytesIO object
    modified_image_io = BytesIO()
    image.save(modified_image_io, format="JPEG")
    
    # Return the modified image as bytes
    return modified_image_io.getvalue()
