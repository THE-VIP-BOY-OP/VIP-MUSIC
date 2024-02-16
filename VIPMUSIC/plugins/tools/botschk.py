import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from dotenv import load_dotenv
import config
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC import app
from datetime import datetime

# Assuming Userbot is defined elsewhere
userbot = Userbot()

last_checked_time = None

@app.on_message(filters.command("botschk") & filters.group)
async def check_bots_command(client, message):
    global last_checked_time
    try:
        # Start the Pyrogram client
        await userbot.one.start()

        # Get current time before sending messages
        start_time = datetime.now()

        # Extract bot username from command
        command_parts = message.command
        if len(command_parts) == 2:
            bot_username = command_parts[1]
            try:  # Proper indentation and missing colon
                bot = await userbot.one.get_users(bot_username)
                bot_id = bot.id
                await asyncio.sleep(0.5)
                bot_info = await userbot.one.send_message(bot_id, "/start")
                await asyncio.sleep(3)
                # Check if bot responded to /start message
                async for bot_message in userbot.one.get_chat_history(bot_id, limit=1):
                if bot_message.from_user.id == bot_id:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏɴʟɪɴᴇ ✨**\n\n"
                else:
                    response += f"╭⎋ [{bot.first_name}](tg://user?id={bot.id})\n╰⊚ **sᴛᴀᴛᴜs: ᴏғғʟɪɴᴇ ❄**\n\n"
        except Exception:
            response += f"╭⎋ {bot_username}\n╰⊚ **sᴛᴀᴛᴜs: ᴇʀʀᴏʀ ❌**\n"
                # Update last checked time
                last_checked_time = start_time.strftime("%Y-%m-%d %H:%M:%S")

                await message.reply_text(f"{response}\n\nLast checked time: {last_checked_time}")
            except Exception as e:
                await message.reply_text(f"An error occurred: {e}")
                print(f"Error occurred during /botschk command: {e}")
        else:
            await message.reply_text("Invalid command format. Please use /botschk Bot_Username\n\nLike :- `/botschk @TG_VC_BOT`")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
        print(f"Error occurred during /botschk command: {e}")
    finally:
        # Stop the Pyrogram client after sending messages
        await userbot.one.stop()
