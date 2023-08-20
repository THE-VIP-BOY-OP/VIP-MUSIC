from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_command
# Command
PLAY_COMMAND = get_command("PLAY_COMMAND")
GSTATS_COMMAND =get_command("GSTATS_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")
STOP_COMMAND = get_command("STOP_COMMAND")
SKIP_COMMAND = get_command("SKIP_COMMAND")


@app.on_message(
    filters.command("owner")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 𝐕𝐈𝐏 𝐁𝐎𝐘 🌹", url=f"https://t.me/THE_VIP_BOY")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("owner")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐃𝐌❤️𝐎𝐖𝐍𝐄𝐑🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 𝐕𝐈𝐏 𝐁𝐎𝐘 🌹", url=f"https://t.me/THE_VIP_BOY")
                ]
            ]
        ),
    )






@app.on_message(
    filters.command("repo")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("source")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""🍁𝐂𝐋𝐈𝐂𝐊🥰𝐁𝐄𝐋𝐎𝐖💝𝐁𝐔𝐓𝐓𝐎𝐍✨𝐓𝐎🙊𝐆𝐄𝐓🌱𝐑𝐄𝐏𝐎🍁""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌱ƨσʋяcɛ🌱", url=f"https://github.com/THE-VIP-BOY-OP/VIP-MUSIC")
                ]
            ]
        ),
    )

#Must Learn 

@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
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

@app.on_message(
    filters.command(GSTATS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /gstats 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /pause 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(REBOOT_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /reboot 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /stop 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SKIP_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /skip 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
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



@app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
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

 @app.on_message(
    filters.command(PLAY_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
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
