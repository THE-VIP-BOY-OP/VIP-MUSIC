import asyncio

from pyrogram.types import InlineKeyboardMarkup

from strings import get_string
from VIPMUSIC.misc import db
from VIPMUSIC.utils.database import get_active_chats, get_lang, is_music_playing
from VIPMUSIC.utils.formatters import seconds_to_min
from VIPMUSIC.utils.inline import stream_markup_timer, telegram_markup_timer

from ..admins.callback import wrong

checker = {}
WARNING_THRESHOLD = 10  # Time in seconds to warn before the song ends


async def timer():
    while not await asyncio.sleep(1):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            if not await is_music_playing(chat_id):
                continue
            playing = db.get(chat_id)
            if not playing:
                continue
            file_path = playing[0]["file"]
            if "index_" in file_path or "live_" in file_path:
                continue
            duration = int(playing[0]["seconds"])
            if duration == 0:
                continue
            db[chat_id][0]["played"] += 1


asyncio.create_task(timer())


async def markup_timer():
    while not await asyncio.sleep(2):
        active_chats = await get_active_chats()
        for chat_id in active_chats:
            try:
                if not await is_music_playing(chat_id):
                    continue
                playing = db.get(chat_id)
                if not playing:
                    continue
                duration_seconds = int(playing[0]["seconds"])
                if duration_seconds == 0:
                    continue
                try:
                    mystic = playing[0]["mystic"]
                    markup = playing[0]["markup"]
                except:
                    continue
                try:
                    check = wrong[chat_id][mystic.message_id]
                    if check is False:
                        continue
                except:
                    pass
                try:
                    language = await get_lang(chat_id)
                    _ = get_string(language)
                except:
                    _ = get_string("en")

                played_seconds = playing[0]["played"]
                remaining_seconds = duration_seconds - played_seconds

                # Check if the song is about to end
                if remaining_seconds <= WARNING_THRESHOLD:
                    try:
                        # Send a warning message if not already sent
                        if (
                            "warning_sent" not in playing[0]
                            or not playing[0]["warning_sent"]
                        ):
                            warning_message = _("The song is about to end!")
                            await mystic.reply(warning_message)
                            playing[0]["warning_sent"] = True
                    except:
                        continue

                # Update the message with remaining time or end message
                try:
                    buttons = (
                        stream_markup_timer(
                            _,
                            playing[0]["vidid"],
                            chat_id,
                            seconds_to_min(played_seconds),
                            playing[0]["dur"],
                        )
                        if markup == "stream"
                        else telegram_markup_timer(
                            _,
                            chat_id,
                            seconds_to_min(played_seconds),
                            playing[0]["dur"],
                        )
                    )

                    # If song has ended, update message to indicate the song has ended
                    if remaining_seconds <= 0:
                        await mystic.edit_text(_("The song has ended."))
                        # Remove old warning message
                        if "warning_sent" in playing[0]:
                            del playing[0]["warning_sent"]
                    else:
                        await mystic.edit_reply_markup(
                            reply_markup=InlineKeyboardMarkup(buttons)
                        )
                except:
                    continue
            except:
                continue


asyncio.create_task(markup_timer())
