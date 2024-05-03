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
from config import LOGGER_ID

CLONES = set()


@app.on_message(filters.command("clone") & filters.private)
async def clone_txt(client, message):
    await message.reply_text(
        f"<b>ʜᴇʟʟᴏ {message.from_user.mention} 👋 </b>\n\n1) sᴇɴᴅ <code>/newbot</code> ᴛᴏ @BotFather\n2) ɢɪᴠᴇ ᴀ ɴᴀᴍᴇ ꜰᴏʀ ʏᴏᴜʀ ʙᴏᴛ.\n3) ɢɪᴠᴇ ᴀ ᴜɴɪǫᴜᴇ ᴜsᴇʀɴᴀᴍᴇ.\n4) ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ᴀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ.\n5) ꜰᴏʀᴡᴀʀᴅ ᴛʜᴀᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ.\n\nᴛʜᴇɴ ɪ ᴀᴍ ᴛʀʏ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄᴏᴘʏ ʙᴏᴛ ᴏғ ᴍᴇ ғᴏʀ ʏᴏᴜ ᴏɴʟʏ 😌"
    )


@app.on_message(
    (filters.regex(r"\d[0-9]{8,10}:[0-9A-Za-z_-]{35}")) & filters.private)
async def on_clone(client, message):
    global CLONES
    try:
        user_id = message.from_user.id
        bot_token = re.findall(
            r"\d[0-9]{8,10}:[0-9A-Za-z_-]{35}", message.text, re.IGNORECASE
        )
        bot_token = bot_token[0] if bot_token else None
        bot_id = re.findall(r"\d[0-9]{8,10}", message.text)
        bots = list(clonebotdb.find())
        bot_tokens = None

        for bot in bots:
            bot_tokens = bot["token"]

        forward_from_id = message.forward_from.id if message.forward_from else None
        if bot_tokens == bot_token:
            await message.reply_text("**©️ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴄʟᴏɴᴇᴅ ʙᴀʙʏ 🐥**")
            return

        if not forward_from_id != 93372553:
            msg = await message.reply_text(
                "**ᴡᴀɪᴛ ᴀ ᴍɪɴᴜᴛᴇ ɪ ᴀᴍ ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ʙᴏᴛ..... ❣️**"
            )
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
                userbot = await get_assistant(LOGGER_ID)
                try:
                    await userbot.send_message(
                        LOGGER_ID, f"Bot @{bot.username} has been restarted."
                    )
                except Exception:
                    pass
                except Exception as e:
                    print("An error occurred:", e)
                details = {
                    "bot_id": bot.id,
                    "is_bot": True,
                    "user_id": user_id,
                    "name": bot.first_name,
                    "token": bot_token,
                    "username": bot.username,
                }
                clonebotdb.insert_one(details)
                await msg.edit_text(
                    f"<b>sᴜᴄᴄᴇssғᴜʟʟʏ ᴄʟᴏɴᴇᴅ ʏᴏᴜʀ ʙᴏᴛ: @{bot.username}.</b>"
                )
            except BaseException as e:
                logging.exception("Error while cloning bot.")
                await msg.edit_text(
                    f"⚠️ <b>ᴇʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**ᴋɪɴᴅʟʏ ғᴏᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @vk_zone ᴛᴏ ɢᴇᴛ ᴀssɪsᴛᴀɴᴄᴇ**"
                )
    except Exception as e:
        logging.exception("Error while handling message.")


@app.on_message(filters.command(["deletecloned", "delcloned"]) & filters.private)
async def delete_cloned_bot(client, message):
    BOT_TOKEN_PATTERN = r"\d+:[\w-]+"
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
