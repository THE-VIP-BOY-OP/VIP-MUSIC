from VIPMUSIC import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from VIPMUSIC.utils.vip_ban import admin_filter
import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from VIPMUSIC.utils.database import get_assistant
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5

random_photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]
# --------------------------------------------------------------------------------- #




LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



def circle(pfp, size=(500, 500), brightness_factor=10):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname, brightness_factor=1.3):
    background = Image.open("VIPMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor) 
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('VIPMUSIC/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('VIPMUSIC/assets/font.ttf', size=60)
    draw.text((2100, 1420), f'ID: {id}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("awelcome") & ~filters.private)
async def auto_state(_, message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /awelcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("**ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title} ʙʏ ᴀssɪsᴛᴀɴᴛ")
        elif state == "on":
            if not A:
                await message.reply_text("**ᴇɴᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"**ᴇɴᴀʙʟᴇᴅ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ** {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴀssɪsᴛᴀɴᴛ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")



@app.on_chat_member_updated(filters.group, group=-2)
async def greet_new_members(_, member: ChatMemberUpdated):
    try:
        
        chat_id = member.chat.id
        userbot = await get_assistant(chat_id)
        count = await app.get_chat_members_count(chat_id)
        A = await wlcm.find_one(chat_id)
        if A:
            return

        user = member.new_chat_member.user if member.new_chat_member else member.from_user
        
        # Add the modified condition here
        if member.new_chat_member and not member.old_chat_member:
            welcome_text = f"""**Wᴇʟᴄᴏᴍᴇ** {user.mention}\n**@{user.username}**"""
            await asyncio.sleep(3) 
            await userbot.send_message(chat_id, text=welcome_text)
    except Exception as e:
       LOGGER.error(e)
    
