import re
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors.exceptions.bad_request_400 import (
    AccessTokenExpired,
    AccessTokenInvalid,
)
from config import API_ID, API_HASH
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_assistant, clonebotdb
from VIPMUSIC.misc import SUDOERS
from config import LOG_GROUP_ID

CLONES = set()


@app.on_message(filters.command("clone") & SUDOERS)
async def clone_txt(client, message):
    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        bots = clonebotdb.find()
        bot_tokens = None

        async for bot in bots:
            bot_tokens = bot["token"]
        if bot_tokens == bot_token:
            return await message.reply_text("**©️ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ ʙᴀʙʏ 🐥**")
        mi = await message.reply_text("**ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ..... ❣️**")
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
            bot_id = bot.id

        except (AccessTokenExpired, AccessTokenInvalid):
            await mi.edit_text(
                "You have provided an invalid bot token. Please provide a valid bot token."
            )
            return
        except Exception as e:
            await mi.edit_text(f"An error occurred: {str(e)}")
            return
        try:

            await app.send_message(
                LOG_GROUP_ID, f"**#New_Clones**\n\n**Bot:- @{bot.username}**"
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
            CLONES.add(bot.id)
            await mi.edit_text(f"<b>sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴏɴᴇᴅ ʏᴏᴜʀ ʙᴏᴛ: @{bot.username}.</b>")
        except BaseException as e:
            logging.exception("Error while cloning bot.")
            await mi.edit_text(
                f"⚠️ <b>ᴇʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**ᴋɪɴᴅʟʏ ғᴏᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @vk_zone ᴛᴏ ɢᴇᴛ ᴀssɪsᴛᴀɴᴄᴇ**"
            )
    else:
        await message.reply_text(
            "<b>ʜᴇʟʟᴏ {message.from_user.mention} 👋 </b>\n\n1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather\n2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.\n3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.\n4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.\n5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.\n\nᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌"
        )


@app.on_message(filters.command(["deletecloned", "delcloned"]) & filters.private)
async def delete_cloned_bot(client, message):
    BOT_TOKEN_PATTERN = r"^\d+:[\w-]+$"
    try:
        if len(message.command) < 2:
            await message.reply_text("**⚠️ Please provide the bot token.**")
            return

        bot_token = " ".join(message.command[1:])

        if not re.match(BOT_TOKEN_PATTERN, bot_token):
            await message.reply_text(
                "**⚠️ The provided text is not a valid bot token.**"
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


@app.on_message(filters.command("delallclone") & SUDOERS)
async def delete_all_cloned_bots(client, message):
    try:
        await message.reply_text("Deleting all cloned bots...")
        await clonebotdb.delete_many({})
        CLONES.clear()

        await message.reply_text("All cloned bots have been deleted successfully.")
    except Exception as e:
        await message.reply_text("An error occurred while deleting all cloned bots.")
        logging.exception(e)


@app.on_message(filters.command("cloned") & SUDOERS)
async def list_cloned_bots(client, message):
    try:
        cloned_bots = list(clonebotdb.find())
        if not cloned_bots:
            await message.reply_text("No bots have been cloned yet.")
            return

        total_clones = len(cloned_bots)
        text = f"**Total Cloned Bots: {total_clones}**\n\n"

        for bot in cloned_bots:
            text += f"**Bot ID:** {bot['bot_id']}\n"
            text += f"**Bot Name:** {bot['name']}\n"
            text += f"**Bot Username:** @{bot['username']}\n\n"

        await message.reply_text(text)
    except Exception as e:
        logging.exception(e)
        await message.reply_text("An error occurred while listing cloned bots.")


async def restart_bots():
    global CLONES
    logging.info("Restarting all bots........")
    cursor = clonebotdb.find()
    async for bot in cursor:
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
