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

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from strings import PLAY_COMMAND


@app.on_message(
    filters.command("PLAY_COMMAND")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
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
