import random
import string
from ast import ExceptHandler

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto,
                            Message)
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS, lyrical
from strings import get_command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram,
                        YouTube, app)
from AnonX.core.call import Anon
from AnonX.utils import seconds_to_min, time_to_seconds
from AnonX.utils.channelplay import get_channeplayCB
from AnonX.utils.database import is_video_allowed
from AnonX.utils.decorators.language import languageCB
from AnonX.utils.decorators.play import PlayWrapper
from AnonX.utils.formatters import formats
from AnonX.utils.inline.play import (livestream_markup,
                                          playlist_markup,
                                          slider_markup, track_markup)
from AnonX.utils.database import is_served_user
from AnonX.utils.inline.playlist import botplaylist_markup
from AnonX.utils.logger import play_logs
from AnonX.utils.stream.stream import stream

# Command
RAID_COMMAND = get_command("RAID_COMMAND")


@app.on_message(
    filters.command("vcraid")
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
