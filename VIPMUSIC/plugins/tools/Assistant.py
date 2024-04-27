from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
STRING1 = getenv("STRING_SESSION", None)


client = Client(STRING1, API_ID, API_HASH)



@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & filters.private & filters.group)
async def start(client, message):
    await message.reply_text(f"**ᴀʟᴇxᴀ ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")
    
