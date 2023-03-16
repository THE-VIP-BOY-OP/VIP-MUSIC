from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋✦",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="✦𝐆𝐋𝐎𝐁𝐀𝐋✦", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐓𝐎𝐏 10 𝐋𝐈𝐒𝐓✦", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐎𝐖𝐍✦", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐆𝐋𝐎𝐁𝐀𝐋✦", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="✦𝐆𝐑𝐎𝐔𝐏✦", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁𝐀𝐂𝐊 ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐀𝐔𝐃𝐈𝐎✦", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="✦𝐕𝐈𝐃𝐄𝐎✦", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁𝐀𝐂𝐊 ☆", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✦𝐓𝐎𝐏 10 𝐋𝐈𝐒𝐓✦", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐏𝐄𝐑𝐒𝐎𝐍𝐀𝐋✦", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="✦𝐆𝐋𝐎𝐁𝐀𝐋✦", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="✦𝐆𝐑𝐎𝐔𝐏✦", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ 𝐁𝐀𝐂𝐊 ☆", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ 𝐁𝐀𝐂𝐊 ☆",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="✦𝐃𝐄𝐋𝐄𝐓𝐄✦",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☆ 𝐁𝐀𝐂𝐊 ☆",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="☆ 𝐂𝐋𝐎𝐒𝐄 ☆",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
