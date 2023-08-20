# 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗜𝗡 𝗢𝗨𝗥 𝗟𝗘𝗔𝗥𝗡𝗜𝗡𝗚 𝗙𝗜𝗟𝗘 𝗗𝗔𝗥𝗟𝗜𝗡𝗚.
# 𝗜 𝗪𝗜𝗟𝗟 𝗧𝗘𝗟𝗟 𝗨𝗛 𝗔𝗕𝗢𝗨𝗧 𝗨𝗦𝗘 𝗢𝗙 𝗖𝗢𝗠𝗠𝗔𝗠𝗗𝗦.

from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app
import string
from strings import get_command
import config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import START_IMG_URL

# Command

START_COMMAND = get_command("PLAY_COMMAND")
HELP_COMMAND = get_command("PLAY_COMMAND")
SETTINGS_COMMAND = get_command("PLAY_COMMAND")
RELOAD_COMMAND = get_command("PLAY_COMMAND")
GSTATS_COMMAND =get_command("PLAY_COMMAND")
STATS_COMMAND = get_command("PLAY_COMMAND")
LANGUAGE_COMMAND = get_command("PLAY_COMMAND")
PLAY_COMMAND = get_command("PLAY_COMMAND")
PLAYMODE_COMMAND = get_command("PLAY_COMMAND")
CHANNELPLAY_COMMAND = get_command("PLAY_COMMAND")
STREAM_COMMAND = get_command("PLAY_COMMAND")
PLAYLIST_COMMAND = get_command("PLAY_COMMAND")
DELETEPLAYLIST_COMMAND = get_command("PLAY_COMMAND")
QUEUE_COMMAND = get_command("PLAY_COMMAND")
LYRICS_COMMAND = get_command("PLAY_COMMAND")
AUTH_COMMAND = get_command("PLAY_COMMAND")
UNAUTH_COMMAND = get_command("PLAY_COMMAND")
AUTHUSERS_COMMAND = get_command("PLAY_COMMAND")
PAUSE_COMMAND = get_command("PLAY_COMMAND")
RESUME_COMMAND = get_command("PLAY_COMMAND")
STOP_COMMAND = get_command("PLAY_COMMAND")
SKIP_COMMAND = get_command("PLAY_COMMAND")
SHUFFLE_COMMAND = get_command("PLAY_COMMAND")
LOOP_COMMAND = get_command("PLAY_COMMAND")
SEEK_COMMAND = get_command("PLAY_COMMAND")
RESTART_COMMAND = get_command("PLAY_COMMAND")
SUDOUSERS_COMMAND = get_command("PLAY_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")



@app.on_message(
    filters.command("PLAY_COMMAND")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"START_IMG_URL",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /play 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
