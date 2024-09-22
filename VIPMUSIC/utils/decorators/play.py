import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PLAYLIST_IMG_URL, PRIVATE_BOT_MODE
from config import SUPPORT_GROUP as SUPPORT_CHAT
from config import adminlist
from strings import get_string
from VIPMUSIC import YouTube, app
from VIPMUSIC.misc import SUDOERS
from VIPMUSIC.utils.database import (
    get_assistant,
    get_cmode,
    get_lang,
    get_playmode,
    get_playtype,
    is_active_chat,
    is_commanddelete_on,
    is_maintenance,
    is_served_private_chat,
)
from VIPMUSIC.utils.inline import botplaylist_markup

links = {}

from pyrogram.errors import ChatAdminRequired


@app.on_callback_query(filters.regex("unban_userbot"))
async def unban_assistant_callback(client, callback_query):
    chat_id = callback_query.message.chat.id
    userbot = await get_assistant(chat_id)
    ubot = userbot.username if username else userbot.id

    try:
        # Unban the assistant
        await app.unban_chat_member(chat_id, userbot.id)

        # Notify user of the success
        await callback_query.answer(
            "Assistant unbanned successfully✅\nNow trying to join the group⌛\n\nThanks for unbanning🥰"
        )

        # After unbanning, try to join the group using the method from your code
        if callback_query.message.chat.username:
            invitelink = callback_query.message.chat.username
            try:
                await userbot.resolve_peer(invitelink)
                await asyncio.sleep(1)
                await userbot.join_chat(invitelink)
                await callback_query.message.reply_text(
                    "**Assistant has successfully joined the group. Now you can play songs✅**"
                )
            except Exception as e:
                await callback_query.message.reply_text(
                    f"**Failed to invite assistant after unbanning. Please give the bot [ (Invite Users Via Link) Admin Power ] to invite assistant in group.**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                )
        else:
            try:
                invitelink = await client.export_chat_invite_link(chat_id)
                await asyncio.sleep(1)
                await userbot.join_chat(invitelink)
                await callback_query.message.reply_text(
                    "**Assistant Joined successfully✅**\nThanks for unbanning🥰"
                )
            except ChatAdminRequired:
                await callback_query.message.reply_text(
                    f"**Please make the bot admin to invite the assistant**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                )
            except Exception as e:
                await callback_query.message.reply_text(f"Failed: {e}")
    except Exception as e:
        await callback_query.answer(
            f"Failed to unban assistant: [ MAKE THE BOT ADMIN AND GIVE BAN POWER FOR UNBAN ASSISTANT ID ]",
            show_alert=True,
        )


def PlayWrapper(command):
    async def wrapper(client, message):
        userbot = await get_assistant(message.chat.id)
        userbot_id = userbot.id
        language = await get_lang(message.chat.id)
        _ = get_string(language)

        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴏᴡ ᴛᴏ ғɪx ?",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(_["general_4"], reply_markup=upl)

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_CHAT}>sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ</a> ғᴏʀ ᴋɴᴏᴡɪɴɢ ᴛʜᴇ ʀᴇᴀsᴏɴ.",
                    disable_web_page_preview=True,
                )

        if PRIVATE_BOT_MODE == str(True):
            if not await is_served_private_chat(message.chat.id):
                await message.reply_text(
                    "**ᴘʀɪᴠᴀᴛᴇ ᴍᴜsɪᴄ ʙᴏᴛ**\n\nᴏɴʟʏ ғᴏʀ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴄʜᴀᴛs ғʀᴏᴍ ᴛʜᴇ ᴏᴡɴᴇʀ. ᴀsᴋ ᴍʏ ᴏᴡɴᴇʀ ᴛᴏ ᴀʟʟᴏᴡ ʏᴏᴜʀ ᴄʜᴀᴛ ғɪʀsᴛ."
                )
                return await app.leave_chat(message.chat.id)

        if await is_commanddelete_on(message.chat.id):
            try:
                await message.delete()
            except:
                pass

        # Telegram audio/video or URL check
        audio_telegram = (
            (message.reply_to_message.audio or message.reply_to_message.voice)
            if message.reply_to_message
            else None
        )
        video_telegram = (
            (message.reply_to_message.video or message.reply_to_message.document)
            if message.reply_to_message
            else None
        )
        url = await YouTube.url(message)
        if audio_telegram is None and video_telegram is None and url is None:
            if len(message.command) < 2:
                if "stream" in message.command:
                    return await message.reply_text(_["str_1"])
                buttons = botplaylist_markup(_)
                return await message.reply_photo(
                    photo=PLAYLIST_IMG_URL,
                    caption=_["playlist_1"],
                    reply_markup=InlineKeyboardMarkup(buttons),
                )

        # Get chat mode and play mode
        if message.command[0][0] == "c":
            chat_id = await get_cmode(message.chat.id)
            if chat_id is None:
                return await message.reply_text(_["setting_12"])
            try:
                chat = await app.get_chat(chat_id)
            except:
                return await message.reply_text(_["cplay_4"])
            channel = chat.title
        else:
            chat_id = message.chat.id
            channel = None

        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)

        # Check for permissions
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])

        # Video play check
        video = True if (message.command[0][0] == "v" or "-v" in message.text) else None
        fplay = True if message.command[0][-1] == "e" else None

        # Assistant join logic with modifications
        if not await is_active_chat(chat_id):
            # userbot = await get_assistant(message.chat.id)

            # Common chats check between bot and assistant
            common_chats = await userbot.get_common_chats(app.username)
            if chat_id in [chat.id for chat in common_chats]:
                return await command(
                    client, message, _, chat_id, video, channel, playmode, url, fplay
                )

            # Handle public and private group cases
            try:

                get = await app.get_chat_member(chat_id, userbot_id)

            except UserNotParticipant:
                if message.chat.username:
                    invitelink = message.chat.username
                    try:
                        await userbot.resolve_peer(invitelink)
                        await userbot.join_chat(invitelink)
                    except InviteRequestSent:
                        await app.approve_chat_join_request(chat_id, userbot_id)
                        return await command(
                            client,
                            message,
                            _,
                            chat_id,
                            video,
                            channel,
                            playmode,
                            url,
                            fplay,
                        )
                    except Exception as e:
                        return await message.reply_text(
                            f"**Failed to invite assistant. Please make the bot an admin to invite it.**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                        )
                else:
                    # If private, export invite link and try inviting
                    try:
                        invitelink = await client.export_chat_invite_link(
                            message.chat.id
                        )
                        await asyncio.sleep(1)
                        await userbot.join_chat(invitelink)
                        return await command(
                            client,
                            message,
                            _,
                            chat_id,
                            video,
                            channel,
                            playmode,
                            url,
                            fplay,
                        )
                    except ChatAdminRequired:
                        return await message.reply_text(
                            f"**Please make the bot admin to invite my assistant**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                        )
                    except UserAlreadyParticipant:
                        pass
                    except Exception as e:
                        return await message.reply_text(f"Failed: {e}")

            except ChatAdminRequired:
                return await message.reply_text(
                    f"**Please make the bot admin to invite my assistant**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                )
            # Check if assistant is banned or restricted
            if (
                get.status == ChatMemberStatus.BANNED
                or get.status == ChatMemberStatus.RESTRICTED
            ):
                try:
                    await app.unban_chat_member(chat_id, userbot_id)
                except:
                    return await message.reply_text(
                        text=f"**Assistant is banned in this group. Please unban the assistant to play songs!**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}",
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        text="Unban Assistant",
                                        callback_data=f"unban_userbot",
                                    )
                                ]
                            ]
                        ),
                    )

            # If group is public, try joining directly
            if message.chat.username:
                invitelink = message.chat.username

                try:
                    await userbot.resolve_peer(invitelink)
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                    return await command(
                        client,
                        message,
                        _,
                        chat_id,
                        video,
                        channel,
                        playmode,
                        url,
                        fplay,
                    )
                except InviteRequestSent:

                    await app.approve_chat_join_request(chat_id, userbot.id)
                    await message.reply_text(
                        "**Assistant joined the group now playing...**"
                    )
                    return await command(
                        client,
                        message,
                        _,
                        chat_id,
                        video,
                        channel,
                        playmode,
                        url,
                        fplay,
                    )
                except Exception as e:
                    return await message.reply_text(
                        f"**Failed to invite assistant. Please make the bot an admin to invite it.**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                    )
            else:
                # If private, export invite link and try inviting
                try:
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                    return await command(
                        client,
                        message,
                        _,
                        chat_id,
                        video,
                        channel,
                        playmode,
                        url,
                        fplay,
                    )
                except ChatAdminRequired:
                    return await message.reply_text(
                        f"**Please make the bot admin to invite my assistant**\n\n**ID:** `{userbot.id}`\n**Username:** @{userbot.username}"
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    return await message.reply_text(f"Failed: {e}")

        return await command(
            client, message, _, chat_id, video, channel, playmode, url, fplay
        )

    return wrapper
