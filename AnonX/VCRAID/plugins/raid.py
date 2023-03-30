from pyrogram import Client
import asyncio
from config import OWNER
from AnonX import app
from VCRAID import bot, call_py
from pytgcalls import StreamType
from pyrogram.types import Message
from pyrogram import Client, filters
from VCRAID.tgcalls.queues import QUEUE, add_to_queue, get_queue
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped




#-------------------------------------CODES-------------------------

@app.on_message(filters.command(["vc"], prefixes=","))
async def raid(client, m: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        await message.delete()
        await bot.send_message(
                OWNER,
                "**USES:** /vc source chat_id example `/vc -1234567890`"           
        )
    else:
        args = message.text.split(maxsplit=1)[1]
        if ";" in args:
            chat = args.split(";")[0]
            limit = int(args.split(";")[1])
        else:
            chat = args
            limit = 10
            lmt = 9
        await bot.send_message(
                OWNER,
                f"**Vc Raid Starting With {limit} Audios From That Channel!**"
           )
        try:
            async for x in bot.search_messages(chat, limit=limit, filter="audio"):
                location = await x.download()
                if x.audio.title:
                    songname = x.audio.title[:30] + "..."
                else:
                    songname = x.audio.file_name[:30] + "..."
                link = x.link
                if chat_id in QUEUE:
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                else:
                    await call_py.join_group_call(
                        chat_id,
                        AudioPiped(location),
                        stream_type=StreamType().pulse_stream,
                    )
                    add_to_queue(chat_id, songname, location, link, "Audio", 0)
                    # await message.reply_to_message.delete()
                    await bot.send_message(
                            OWNER,
                            f"**Started Raid In**`{chat_id}` !"
                    )
        except Exception as e:
            await bot.send_message(OWNER, f"**ERROR** \n`{e}`")
