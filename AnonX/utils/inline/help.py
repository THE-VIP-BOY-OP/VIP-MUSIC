from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        )
    ]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"], callback_data=f"close"
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🍁𝐀𝐃𝐌𝐈𝐍🍁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🔺𝐀𝐔𝐓𝐇🔺",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="♨️𝐁𝐋𝐎𝐂𝐊♨️",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📣𝐆𝐂𝐀𝐒𝐓📢",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🚫𝐆𝐁𝐀𝐍🚫",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🍷𝐋𝐘𝐑𝐈𝐂𝐒🍷",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️𝐏𝐋𝐀𝐘𝐋𝐈𝐒𝐓🎙️",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="🎸𝐆𝐑𝐎𝐔𝐏-𝐕𝐂🎸",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️𝐏𝐋𝐀𝐘🕹️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸𝐃𝐎𝐒𝐓🍸",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️𝐒𝐓𝐀𝐑𝐓⚜️",
                    callback_data="help_callback hb11",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"], callback_data=f"close"
                )
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎭 𝐇𝐄𝐋𝐏 🎭",
                callback_data="settings_back_helper",
            ),
        ],
    ]
    return buttons
