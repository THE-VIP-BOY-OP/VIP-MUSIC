#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
#

from VIPMUSIC.utils.database import get_client


async def get_assistant_details():
    ms = ""
    msg = "**ᴜsᴀsɢᴇ** : /setassistant [ᴀssɪsᴛᴀɴᴛ ɴᴏ ] ᴛᴏ ᴄʜᴀɴɢᴇ ᴀɴᴅ sᴇᴛ ᴍᴀɴᴜᴀʟʟʏ ɢʀᴏᴜᴘ ᴀssɪsᴛᴀɴᴛ \n ʙᴇʟᴏᴡ sᴏᴍᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴀssɪsᴛᴀɴᴛ ᴅᴇᴛᴀɪʟ's\n"
    try:
        a = await get_client(1)
        msg += f"ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ:- `1` \nɴᴀᴍᴇ :- [{a.name}](https://t.me/{a.username})  \nᴜsᴇʀɴᴀᴍᴇ :-  @{a.username} \nɪᴅ :- {a.id}\n\n"
    except:
        pass

    try:
        b = await get_client(2)
        msg += f"ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ:- `2` \nɴᴀᴍᴇ :- [{b.name}](https://t.me/{b.username})  \nᴜsᴇʀɴᴀᴍᴇ :-  @{b.username} \nɪᴅ :- {b.id}\n"
    except:
        pass

    try:
        c = await get_client(3)
        msg += f"ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ:- `3` \nɴᴀᴍᴇ :- [{c.name}](https://t.me/{c.username})  \nᴜsᴇʀɴᴀᴍᴇ :-  @{c.username} \nɪᴅ :- {c.id}\n"
    except:
        pass

    try:
        d = await get_client(4)
        msg += f"ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ:- `4` \nɴᴀᴍᴇ :- [{d.name}](https://t.me/{d.username})  \nᴜsᴇʀɴᴀᴍᴇ :-  @{d.username} \nɪᴅ :- {d.id}\n"
    except:
        pass

    try:
        e = await get_client(5)
        msg += f"ᴀssɪsᴛᴀɴᴛ ɴᴜᴍʙᴇʀ:- `5`\nɴᴀᴍᴇ :- [{e.name}](https://t.me/{e.username})\nᴜsᴇʀɴᴀᴍᴇ :-  @{e.username} \nɪᴅ :- {e.id}\n"
    except:
        pass

    return msg


async def is_avl_assistant():
    from config import STRING1, STRING2, STRING3, STRING4, STRING5

    filled_count = sum(
        1
        for var in [STRING1, STRING2, STRING3, STRING4, STRING5]
        if var and var.strip()
    )
    if filled_count == 1:
        return True
    else:
        return False