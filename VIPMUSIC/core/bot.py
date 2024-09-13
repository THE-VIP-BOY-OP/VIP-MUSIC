# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#

import uvloop

uvloop.install()

import pyrogram
import pyromod.listen  # noqa
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import (
    BotCommand,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllPrivateChats,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

import config

from ..logging import LOGGER


class VIPBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "VIPMUSIC",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        # Create the button
        button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="๏ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ๏",
                        url=f"https://t.me/{self.username}?startgroup=true",
                    )
                ]
            ]
        )

        # Try to send a message to the logger group
        if config.LOG_GROUP_ID:
            try:
                await self.send_photo(
                    config.LOG_GROUP_ID,
                    photo=config.START_IMG_URL,
                    caption=f"╔════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪\n║\n║┣⪼🥀𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲🎉\n║\n║┣⪼ {self.name}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠😍\n║\n╚════════════════❍⊱❁",
                    reply_markup=button,
                )
            except pyrogram.errors.ChatWriteForbidden as e:
                LOGGER(__name__).error(f"Bot cannot write to the log group: {e}")
                try:
                    await self.send_message(
                        config.LOG_GROUP_ID,
                        f"╔═══❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱═══❍⊱❁۪۪\n║\n║┣⪼🥀𝐁𝐨𝐭 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐚𝐛𝐲🎉\n║\n║◈ {self.name}\n║\n║┣⪼🎈𝐈𝐃:- `{self.id}` \n║\n║┣⪼🎄@{self.username} \n║ \n║┣⪼💖𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠😍\n║\n╚══════════════❍⊱❁",
                        reply_markup=button,
                    )
                except Exception as e:
                    LOGGER(__name__).error(f"Failed to send message in log group: {e}")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Unexpected error while sending to log group: {e}"
                )
        else:
            LOGGER(__name__).warning(
                "LOG_GROUP_ID is not set, skipping log group notifications."
            )

        # Setting commands
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "Start the bot"),
                        BotCommand("help", "Get the help menu"),
                        BotCommand("ping", "Check if the bot is alive or dead"),
                    ],
                    scope=BotCommandScopeAllPrivateChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("play", "Start playing requested song"),
                        BotCommand("stop", "Stop the current song"),
                        BotCommand("pause", "Pause the current song"),
                        BotCommand("resume", "Resume the paused song"),
                        BotCommand("queue", "Check the queue of songs"),
                        BotCommand("skip", "Skip the current song"),
                        BotCommand("volume", "Adjust the music volume"),
                        BotCommand("lyrics", "Get lyrics of the song"),
                    ],
                    scope=BotCommandScopeAllGroupChats(),
                )
                await self.set_bot_commands(
                    commands=[
                        BotCommand("start", "❥ Start the bot"),
                        BotCommand("ping", "❥ Check the ping"),
                        BotCommand("help", "❥ Get help"),
                        BotCommand("vctag", "❥ Tag all for voice chat"),
                        BotCommand("stopvctag", "❥ Stop tagging for VC"),
                        BotCommand("tagall", "❥ Tag all members by text"),
                        BotCommand("cancel", "❥ Cancel the tagging"),
                        BotCommand("settings", "❥ Get the settings"),
                        BotCommand("reload", "❥ Reload the bot"),
                        BotCommand("play", "❥ Play the requested song"),
                        BotCommand("vplay", "❥ Play video along with music"),
                        BotCommand("end", "❥ Empty the queue"),
                        BotCommand("playlist", "❥ Get the playlist"),
                        BotCommand("stop", "❥ Stop the song"),
                        BotCommand("lyrics", "❥ Get the song lyrics"),
                        BotCommand("song", "❥ Download the requested song"),
                        BotCommand("video", "❥ Download the requested video song"),
                        BotCommand("gali", "❥ Reply with fun"),
                        BotCommand("shayri", "❥ Get a shayari"),
                        BotCommand("love", "❥ Get a love shayari"),
                        BotCommand("sudolist", "❥ Check the sudo list"),
                        BotCommand("owner", "❥ Check the owner"),
                        BotCommand("update", "❥ Update bot"),
                        BotCommand("gstats", "❥ Get stats of the bot"),
                        BotCommand("repo", "❥ Check the repo"),
                    ],
                    scope=BotCommandScopeAllChatAdministrators(),
                )
            except Exception as e:
                LOGGER(__name__).error(f"Failed to set bot commands: {e}")

        # Check if bot is an admin in the logger group
        if config.LOG_GROUP_ID:
            try:
                chat_member_info = await self.get_chat_member(
                    config.LOG_GROUP_ID, self.id
                )
                if chat_member_info.status != ChatMemberStatus.ADMINISTRATOR:
                    LOGGER(__name__).error(
                        "Please promote Bot as Admin in Logger Group"
                    )
            except Exception as e:
                LOGGER(__name__).error(f"Error occurred while checking bot status: {e}")

        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
