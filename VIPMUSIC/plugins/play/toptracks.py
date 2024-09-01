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

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from pyrogram.types import InlineKeyboardMarkup

from config import BANNED_USERS
from VIPMUSIC import app
from VIPMUSIC.utils.database import (
    get_assistant,
    get_global_tops,
    get_particulars,
    get_userss,
)
from VIPMUSIC.utils.decorators.language import languageCB
from VIPMUSIC.utils.inline.playlist import (
    botplaylist_markup,
    failed_top_markup,
    top_play_markup,
)
from VIPMUSIC.utils.stream.stream import stream

loop = asyncio.get_running_loop()


@app.on_callback_query(filters.regex("get_playmarkup") & ~BANNED_USERS)
@languageCB
async def get_play_markup(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    buttons = botplaylist_markup(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex("get_top_playlists") & ~BANNED_USERS)
@languageCB
async def get_topz_playlists(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    buttons = top_play_markup(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex("SERVERTOP") & ~BANNED_USERS)
@languageCB
async def server_to_play(client, CallbackQuery, _):
    userbot = await get_assistant(CallbackQuery.message.chat.id)
    try:
        try:
            get = await app.get_chat_member(CallbackQuery.message.chat.id, userbot.id)
        except ChatAdminRequired:
            return await CallbackQuery.answer(
                f"» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ᴛᴏ {CallbackQuery.message.chat.title}.",
                show_alert=True,
            )
        if get.status == ChatMemberStatus.BANNED:
            return await CallbackQuery.answer(
                text=f"»ᴀssɪsᴛᴀɴᴛ ɪs ʙᴀɴɴᴇᴅ ɪɴ {CallbackQuery.message.chat.title}",
                show_alert=True,
            )
    except UserNotParticipant:
        if CallbackQuery.message.chat.username:
            invitelink = CallbackQuery.message.chat.username
            try:
                await userbot.resolve_peer(invitelink)
            except Exception as ex:
                logging.exception(ex)
        else:
            try:
                invitelink = await client.export_chat_invite_link(
                    CallbackQuery.message.chat.id
                )
            except ChatAdminRequired:
                return await CallbackQuery.answer(
                    f"» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ғᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.",
                    show_alert=True,
                )
            except InviteRequestSent:
                try:
                    await app.approve_chat_join_request(
                        CallbackQuery.message.chat.id, userbot.id
                    )
                except Exception as e:
                    return await CallbackQuery.message.reply_text(
                        f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}\nʀᴇᴀsᴏɴ :{e}"
                    )
            except Exception as ex:
                if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                    return await CallbackQuery.answer(
                        f"» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ғᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.",
                        show_alert=True,
                    )
                else:
                    return await CallbackQuery.message.reply_text(
                        f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.\n\n**ʀᴇᴀsᴏɴ :** `{ex}`"
                    )
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace("https://t.me/+", "https://t.me/joinchat/")
        try:
            await userbot.join_chat(invitelink)
            await asyncio.sleep(2)
        except UserAlreadyParticipant:
            pass
        except InviteRequestSent:
            try:
                await app.approve_chat_join_request(
                    CallbackQuery.message.chat.id, userbot.id
                )
            except Exception as e:
                if "messages.HideChatJoinRequest" in str(e):
                    return await CallbackQuery.answer(
                        f"» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ғᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.",
                        show_alert=True,
                    )
                else:
                    return await CallbackQuery.message.reply_text(
                        f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.\n\nʀᴇᴀsᴏɴ :{e}"
                    )
        except Exception as ex:
            if "channels.JoinChannel" in str(ex) or "Username not found" in str(ex):
                return await CallbackQuery.answer(
                    f"» ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ ғᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.",
                    show_alert=True,
                )
            else:
                return await CallbackQuery.message.reply_text(
                    f"ғᴀɪʟᴇᴅ ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ {CallbackQuery.message.chat.title}.\n\nʀᴇᴀsᴏɴ : {ex}"
                )

        try:
            await userbot.resolve_peer(invitelink)
        except:
            pass

    chat_id = CallbackQuery.message.chat.id
    user_name = CallbackQuery.from_user.first_name
    try:
        await CallbackQuery.answer()
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    mystic = await CallbackQuery.edit_message_text(
        _["tracks_1"].format(
            what,
            CallbackQuery.from_user.first_name,
        )
    )
    upl = failed_top_markup(_)
    if what == "Global":
        stats = await get_global_tops()
    elif what == "Group":
        stats = await get_particulars(chat_id)
    elif what == "Personal":
        stats = await get_userss(CallbackQuery.from_user.id)
    if not stats:
        return await mystic.edit(_["tracks_2"].format(what), reply_markup=upl)

    def get_stats():
        results = {}
        for i in stats:
            top_list = stats[i]["spot"]
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["tracks_2"].format(what), reply_markup=upl)
        details = []
        limit = 0
        for vidid, count in list_arranged.items():
            if vidid == "telegram":
                continue
            if limit == 10:
                break
            limit += 1
            details.append(vidid)
        if not details:
            return mystic.edit(_["tracks_2"].format(what), reply_markup=upl)
        return details

    try:
        details = await loop.run_in_executor(None, get_stats)
    except Exception as e:
        print(e)
        return
    try:
        await stream(
            _,
            mystic,
            CallbackQuery.from_user.id,
            details,
            chat_id,
            user_name,
            CallbackQuery.message.chat.id,
            video=False,
            streamtype="playlist",
        )
    except Exception as e:
        ex_type = type(e).__name__
        err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
        return await mystic.edit_text(err)
    return await mystic.delete()
