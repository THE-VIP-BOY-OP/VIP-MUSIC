#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#

import asyncio

import speedtest
from pyrogram import filters

from strings import get_command
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...")
        test.download()
        m = m.edit("⇆ ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("↻ sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ")
    loop = asyncio.get_event_loop_policy().get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**ɪsᴘ :** {result['client']['isp']}
**ᴄᴏᴜɴᴛʀʏ :** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ :**</u>
**ɴᴀᴍᴇ :** {result['server']['name']}
**ᴄᴏᴜɴᴛʀʏ :** {result['server']['country']}, {result['server']['cc']}
**sᴘᴏɴsᴏʀ :** {result['server']['sponsor']}
**ʟᴀᴛᴇɴᴄʏ :** {result['server']['latency']}  
**ᴘɪɴɢ :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
