import random
from pyrogram import Client, filters
from pyrogram.types import Message

from VIPMUSIC.core.mongo import mongodb

chatdb = mongodb.chatai
vipdb = mongodb.Vipdb

@Client.on_message(filters.command("alive", prefixes=["/", ".", "?", "-"]))
async def start(client, message):
    await message.reply_text("**ᴀʟᴇxᴀ ᴀɪ ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")

async def handle_message(client, message, private=False):
    chatai = chatdb["Word"]["WordDb"]
    vip = vipdb["VipDb"]["Vip"]
    is_vip = vip.find_one({"chat_id": message.chat.id})

    if not is_vip:
        if not message.reply_to_message:
            await process_message(client, message, chatai, is_sticker=message.sticker is not None)
        else:
            getme = await client.get_me()
            user_id = getme.id
            if message.reply_to_message.from_user.id == user_id:
                await process_message(client, message, chatai, is_sticker=message.sticker is not None)
            else:
                await store_message(client, message, chatai)

async def process_message(client, message, chatai, is_sticker=False):
    K = []
    word = message.sticker.file_unique_id if is_sticker else message.text
    is_chat = chatai.find({"word": word})
    for x in is_chat:
        K.append(x["text"])
    if K:
        hey = random.choice(K)
        is_text = chatai.find_one({"text": hey})
        if is_text:
            Yo = is_text["check"]
            if Yo == "sticker":
                await message.reply_sticker(hey)
            else:
                await message.reply_text(hey)

async def store_message(client, message, chatai):
    if message.sticker:
        data = {
            "word": message.reply_to_message.text,
            "text": message.sticker.file_id,
            "check": "sticker",
            "id": message.sticker.file_unique_id,
        }
    elif message.text:
        data = {
            "word": message.reply_to_message.text,
            "text": message.text,
            "check": "none",
        }
    else:
        return

    existing_entry = chatai.find_one(data)
    if not existing_entry:
        chatai.insert_one(data)

@Client.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.me & ~filters.bot)
async def vipai(client: Client, message: Message):
    await handle_message(client, message)

@Client.on_message((filters.text | filters.sticker) & filters.private & ~filters.me & ~filters.bot)
async def vipprivate(client: Client, message: Message):
    await handle_message(client, message, private=True)
