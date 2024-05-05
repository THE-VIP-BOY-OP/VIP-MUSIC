import re
import logging
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import (
    AccessTokenExpired,
    AccessTokenInvalid,
)
from config import API_ID, API_HASH
from VIPMUSIC import app
from VIPMUSIC.misc import SUDOERS
from pyrogram.types import Message
from VIPMUSIC.utils.database import get_assistant, clonebotdb
from config import LOGGER_ID

CLONES = set()

@app.on_message(filters.command("clone") & filters.private)
async def clone_txt(client, message):
    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        await message.reply_text("Please wait while I process the bot token.")
        try:
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="VIPMUSIC.cplugin"),
            )
            await ai.start()
            bot = await ai.get_me()
            
        except (AccessTokenExpired, AccessTokenInvalid):
            await message.reply_text("You have provided an invalid bot token. Please provide a valid bot token.")
            return
        except Exception as e:
            await message.reply_text(f"An error occurred: {str(e)}")
            return
        
        # Proceed with the cloning process
        await message.reply_text("Cloning process initiated. Please wait for the bot to be cloned.")
        try:
            
            await app.send_message(
                LOGGER_ID, f"Bot @{bot.username} has been cloned.\nCheck all cloned bot by /cloned"
            )
            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": message.from_user.id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
            }
            clonebotdb.insert_one(details)
            await message.reply_text(f"Bot @{bot.username} has been successfully cloned.")
        except BaseException as e:
            logging.exception("Error while cloning bot.")
            await message.reply_text(
                f"⚠️ <b>ᴇʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**ᴋɪɴᴅʟʏ ғᴏᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @vk_zone ᴛᴏ ɢᴇᴛ ᴀssɪsᴛᴀɴᴄᴇ**"
            )
    else:
        await message.reply_text("Please provide a bot token after the /clone command.")

@app.on_message(filters.command(["deletecloned", "delcloned", "delclone", "deleteclone", "removeclone", "cancelclone"]) & filters.private)
async def delete_cloned_bot(client, message):
    
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the bot token. after command **")
            return

        bot_token = " ".join(message.command[1:])

        if not re.match(BOT_TOKEN_PATTERN, bot_token):
            await message.reply_text(
                "**⚠️ you have not provided correct bot token from @botfather.**"
            )
            return

        cloned_bot = clonebotdb.find_one({"token": bot_token})
        if cloned_bot:
            clonebotdb.delete_one({"token": bot_token})
            await message.reply_text(
                "**🤖 The cloned bot has been removed from the list and its details have been removed from the database. ☠️**"
            )
        else:
            await message.reply_text(
                "**⚠️ The provided bot token is not in the cloned list.**"
            )
    except Exception as e:
        logging.exception("Error while deleting cloned bot.")
        await message.reply_text("An error occurred while deleting the cloned bot.")


async def restart_bots():
    global CLONES
    logging.info("Restarting all bots........")
    bots = list(clonebotdb.find())
    for bot in bots:
        bot_token = bot["token"]
        try:
            ai = Client(
                f"{bot_token}",
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="VIPMUSIC.cplugin"),
            )
            await ai.start()
            bot = await ai.get_me()
            if bot.id not in CLONES:
                try:
                    CLONES.add(bot.id)
                except Exception:
                    pass
        except (AccessTokenExpired, AccessTokenInvalid):
            clonebotdb.delete_one({"token": bot_token})
        except Exception as e:
            logging.exception(f"Error while restarting bot with token {bot_token}: {e}")
