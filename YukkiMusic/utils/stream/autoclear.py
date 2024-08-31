#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the MIT License.
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
