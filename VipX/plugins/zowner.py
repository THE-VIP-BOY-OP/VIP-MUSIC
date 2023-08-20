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
ACTIVEVC_COMMAND = get_command("ACTIVEVC_COMMAND")
ACTIVEVIDEO_COMMAND = get_command("ACTIVEVIDEO_COMMAND")
RESTART_COMMAND = get_command("RESTART_COMMAND")
SEEK_COMMAND = get_command("SEEK_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
UNGBAN_COMMAND = get_command("UNGBAN_COMMAND")
GBANNED_COMMAND = get_command("GBANNED_COMMAND")
SETTINGS_COMMAND = get_command("SETTINGS_COMMAND")
RELOAD_COMMAND = get_command("RELOAD_COMMAND")
GETVAR_COMMAND = get_command("GETVAR_COMMAND")
UPDATE_COMMAND = get_command("UPDATE_COMMAND")
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")
ADDSUDO_COMMAND = get_command("ADDSUDO_COMMAND")
DELSUDO_COMMAND = get_command("DELSUDO_COMMAND")
GETLOG_COMMAND = get_command("GETLOG_COMMAND")
BROADCAST_COMMAND = get_command("BROADCAST_COMMAND")

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
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(ACTIVEVC_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(ACTIVEVC_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(ACTIVEVIDEO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(RESTART_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(RESTART_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(GETVAR_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(GETVAR_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(SEEK_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /seek (count) 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
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
    filters.command(RESUME_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /resume 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
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
    filters.command(SETTINGS_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /settings 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
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
    filters.command("gban")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command("gban")
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(UNGBAN_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(UNGBAN_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(RELOAD_COMMAND)
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
    filters.command(UPDATE_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(UPDATE_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(SPEEDTEST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(SPEEDTEST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(ADDSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(ADDSUDO_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(DELSUDO_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(BROADCAST_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
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
    filters.command(BROADCAST_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/4b52da6d880cbb199298a.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐈𝚂 𝐎𝙽𝙻𝚈 𝐅𝙾𝚁 𝐒𝚄𝙳𝙾 𝐔𝚂𝙴𝚁𝚂 𝐁𝙰𝙱𝚈..**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )

