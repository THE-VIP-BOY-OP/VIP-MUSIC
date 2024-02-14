from telegraph import upload_file
from pyrogram import filters
import base64
import httpx
import os
from PIL import Image, ImageEnhance
from VIPMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from telegraph import upload_video

@app.on_message(filters.reply & filters.command(["tgm", "telegraph"]))
async def create_telegraph_link(client, message):
    try:
        if not message.reply_to_message:
            await message.reply_text("**ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ ᴛᴏ ᴄʀᴇᴀᴛᴇ ɪᴛs ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ..**")
            return

        sent_message = await message.reply_text("**ᴘʀᴏᴄᴇssɪɴɢ...**")

        if message.reply_to_message.video:
            # Process video
            media = message.reply_to_message.video
            video_file_id = media.file_id
            video_file_path = await client.download_media(video_file_id)
            telegraph_url = upload_video(video_file_path)[0]
            caption_text = "Video ka Telegraph Link:"
        elif message.reply_to_message.photo:
            # Process photo
            media = message.reply_to_message.photo
            image_file_id = media.file_id
            image_file_path = await client.download_media(image_file_id)
            image = Image.open(image_file_path)
            enhancer = ImageEnhance.Brightness(image)
            brightened_image = enhancer.enhance(1.1)  # Increase brightness by 10%
            brightened_file_path = "brightened_image.png"
            brightened_image.save(brightened_file_path)
            telegraph_url = upload_file(brightened_file_path)[0]
            caption_text = "Image ka Telegraph Link:"
        elif message.reply_to_message.sticker:
            # Process sticker
            media = message.reply_to_message.sticker
            sticker_file_id = media.file_id
            sticker_file_path = await client.download_media(sticker_file_id)
            sticker_image = Image.open(sticker_file_path)
            if sticker_image.is_animated:
                # Convert animated sticker to video
                await client.send_chat_action(message.chat.id, "record_video")
                sticker_image.save("animated_sticker.mp4")
                telegraph_url = upload_video("animated_sticker.mp4")[0]
            else:
                # Convert sticker to image
                sticker_image.save("sticker_as_image.png")
                telegraph_url = upload_file("sticker_as_image.png")[0]
            caption_text = "Sticker ka Telegraph Link:"
        else:
            await message.reply_text("**ᴜɴsᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ, ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ, ᴠɪᴅᴇᴏ ᴏʀ sᴛɪᴄᴋᴇʀ...**")
            return

        # Delete the "Processing..." message after sending the results
        await sent_message.delete()

        button_text = "Open in Telegraph"
        button_url = "https://telegra.ph" + telegraph_url
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(button_text, url=button_url)]]
        )

        await client.send_message(
            message.chat.id,
            media=media,
            caption=f"{caption_text} {button_url}",
            reply_markup=reply_markup,
        )

    except Exception as e:
        print(f"Failed to create Telegraph link: {e}")
        await message.reply_text("**Failed to create Telegraph link. Please provide a valid media file.**")
