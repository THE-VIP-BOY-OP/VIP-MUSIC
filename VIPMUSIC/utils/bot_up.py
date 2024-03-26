import time

import psutil

from VIPMUSIC.misc import _boot_
from VIPMUSIC.utils.formatters import get_readable_time


async def bot_up_time():
    bot_up_time = int(time.time() - _boot_)
    BOT_UP = f"{get_readable_time(bot_up_time)}"
    return BOT_UP
