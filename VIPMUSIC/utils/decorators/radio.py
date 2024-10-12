import asyncio

from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PRIVATE_BOT_MODE
from config import SUPPORT_GROUP as SUPPORT_CHAT
from strings import get_string
from VIPMUSIC import YouTube, app
from VIPMUSIC.core.call import _st_ as clean
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

links = {}


def RadioWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        userbot = await get_assistant(message.chat.id)
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

        try:
            is_call_active = (await app.get_chat(chat_id)).is_call_active
            if not is_call_active:
                return await message.reply_text(
                    f"**» ɴᴏ ᴀᴄᴛɪᴠᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ ғᴏᴜɴᴅ.**\n\nᴩʟᴇᴀsᴇ ᴍᴀᴋᴇ sᴜʀᴇ ʏᴏᴜ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ᴠɪᴅᴇᴏᴄʜᴀᴛ."
                )
        except Exception:
            pass

        playmode = await get_playmode(message.chat.id)
        playty = await get_playtype(message.chat.id)
        if playty != "Everyone":
            if message.from_user.id not in SUDOERS:
                admins = adminlist.get(message.chat.id)
                if not admins:
                    return await message.reply_text(_["admin_18"])
                else:
                    if message.from_user.id not in admins:
                        return await message.reply_text(_["play_4"])
        if message.command[0][0] == "v":
            video = True
        else:
            if "-v" in message.text:
                video = True
            else:
                video = True if message.command[0][1] == "v" else None
        if message.command[0][-1] == "e":
            if not await is_active_chat(chat_id):
                return await message.reply_text(_["play_18"])
            fplay = True
        else:
            fplay = None

        # Check if userbot is already present in the chat using common chats
        userbot = await get_assistant(message.chat.id)
        common_chats = await userbot.get_common_chats(app.username)
        chat_matched = any(chat.id == message.chat.id for chat in common_chats)

        if chat_matched:
            # If common chat matches, skip join process and proceed
            call_participants_id = [
                member.chat.id async for member in userbot.get_call_members(chat_id)
            ]
            if await is_active_chat(chat_id) and userbot.id not in call_participants_id:
                await clean(chat_id)

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

        # If common chat doesn't match, try to join via username if available
        if message.chat.username:
            try:
                await userbot.join_chat(message.chat.username)
                call_participants_id = [
                    member.chat.id async for member in userbot.get_call_members(chat_id)
                ]
                if (
                    await is_active_chat(chat_id)
                    and userbot.id not in call_participants_id
                ):
                    await clean(chat_id)

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
                pass

        # Fallback to previous flow if join via username fails
        if not await is_active_chat(chat_id):
            userbot_id = userbot.id
            try:
                try:
                    get = await app.get_chat_member(chat_id, userbot_id)
                except ChatAdminRequired:
                    return await message.reply_text(_["call_1"])
                if (
                    get.status == ChatMemberStatus.BANNED
                    or get.status == ChatMemberStatus.RESTRICTED
                ):
                    try:
                        await app.unban_chat_member(chat_id, userbot_id)
                    except:
                        return await message.reply_text(
                            text=_["call_2"].format(userbot.username, userbot_id),
                        )
            except UserNotParticipant:
                if chat_id in links:
                    invitelink = links[chat_id]
                else:
                    if message.chat.username:
                        invitelink = message.chat.username
                        try:
                            await userbot.resolve_peer(invitelink)
                        except:
                            pass
                    else:
                        try:
                            invitelink = await client.export_chat_invite_link(
                                message.chat.id
                            )
                        except ChatAdminRequired:
                            return await message.reply_text(_["call_1"])
                        except Exception as e:
                            return await message.reply_text(
                                _["call_3"].format(app.mention, type(e).__name__)
                            )

                if invitelink.startswith("https://t.me/+"):
                    invitelink = invitelink.replace(
                        "https://t.me/+", "https://t.me/joinchat/"
                    )
                myu = await message.reply_text(_["call_5"])
                try:
                    await asyncio.sleep(1)
                    await userbot.join_chat(invitelink)
                except InviteRequestSent:
                    try:
                        await app.approve_chat_join_request(chat_id, userbot.id)
                    except Exception as e:
                        return await myu.edit(_["call_3"].format(type(e).__name__))
                    await asyncio.sleep(1)
                    await myu.edit(_["call_6"].format(app.mention))
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    return await myu.edit(_["call_3"].format(type(e).__name__))

                links[chat_id] = invitelink
                try:
                    await myu.delete()
                except Exception:
                    pass

                try:
                    await userbot.resolve_peer(chat_id)
                except:
                    pass

        # Fetch call participants and stop the stream if userbot is not in the call
        userbot = await get_assistant(message.chat.id)
        call_participants_id = [
            member.chat.id async for member in userbot.get_call_members(chat_id)
        ]
        if await is_active_chat(chat_id) and userbot.id not in call_participants_id:
            await clean(chat_id)

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

    return wrapper
