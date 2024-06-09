import os
import shutil

from pyrogram import filters

from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS


@app.on_message(filters.command("clean") & SUDOERS)
async def clean(_, message):
    A = await message.reply_text("ᴄʟᴇᴀɴɪɴɢ ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs...")
    dir = "downloads"
    dir1 = "cache"
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    await A.edit("ᴛᴇᴍᴘ ᴅɪʀᴇᴄᴛᴏʀɪᴇs ᴀʀᴇ ᴄʟᴇᴀɴᴇᴅ")


__MODULE__ = "Clean"
__HELP__ = """
## Clean Command

### Command: /clean
**Description:**
Cleans up temporary directories to free up space.

**Usage:**
/clean

**Details:**
- Deletes the 'downloads' and 'cache' directories and recreates them to ensure temporary files are removed.
- Only accessible to users in the SUDOERS list.
"""
