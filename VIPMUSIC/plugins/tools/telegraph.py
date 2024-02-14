from telegraph import upload_file
from pyrogram import filters
import base64
import httpx
import os
from PIL import Image, ImageEnhance
from VIPMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@app.on_message(filters.reply & filters.command(["tgm", "telegraph"]))
async def create_telegraph_link(client, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("**ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴄʀᴇᴀᴛᴇ ɪᴛs ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ..**")
            return

        sent_message = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ...**")

        if message.reply_to_message.photo:
            media = message.reply_to_message.photo
        elif message.reply_to_message.sticker:
            sticker_file_id = message.reply_to_message.sticker.file_id
            sticker_file = await client.download_media(sticker_file_id)
            # Convert sticker to image
            sticker_image = Image.open(sticker_file)
            sticker_image.save("sticker_as_image.png")
            media = "sticker_as_image.png"
        else:
            await message.reply_text("**ᴜɴsᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ, ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ...**")
            return

        # Increase brightness
        if isinstance(media, str):  # Check if media is an image file path
            image = Image.open(media)
        else:  # Media is a photo object
            image = Image.open(await client.download_media(media))

        enhancer = ImageEnhance.Brightness(image)
        brightened_image = enhancer.enhance(1.1)  # Increase brightness by 50%

        # Save the brightened image
        brightened_file_path = "brightened_image.png"
        brightened_image.save(brightened_file_path)

        # Upload the brightened image to Telegraph
        telegraph_url = upload_file(brightened_file_path)[0]

        # Create caption with the Telegraph link as a button
        button_text = "Open in Telegraph"
        button_url = "https://telegra.ph" + telegraph_url
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(button_text, url=button_url)]]
        )

        await client.send_media(
            message.chat.id,
            media=brightened_file_path,
            caption=f"**ʜᴇʀᴇ ɪs ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ɪɴ ʜᴅ:**\n\n{button_url}\n\n**ᴍᴀᴅᴇ ʙʏ » @{app.username}**",
            reply_markup=reply_markup,
        )

        # Delete the "Processing..." message after sending the results
        await sent_message.delete()

    except Exception as e:
        print(f"ғᴀɪʟᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴍᴇᴅɪᴀ: {e}")
        await message.reply_text("**ғᴀɪʟᴇᴅ ᴛᴏ ᴄʀᴇᴀᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʏᴏᴜʀ ɢɪᴠᴇɴ ᴍᴇᴅɪᴀ. ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴍᴇ ɪɴ ᴄᴏʀʀᴇᴄᴛ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ ғᴏʀᴍᴀᴛ.**")
