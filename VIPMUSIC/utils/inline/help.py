from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app

def first_page(_):
	controll_button = [InlineKeyboardButton(text="๏ ᴍᴇɴᴜ ๏", callback_data=f"settingsback_helper"), InlineKeyboardButton(text="๏ ɴᴇxᴛ ๏", callback_data=f"dilXaditi")]
	first_page_menu = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1"), InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2"),InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3")],
			[InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4"), InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12"),InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5")],
			[InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6"), InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10")],
                        [InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8"), InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9")],
                        [InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11")],
			controll_button,
		]
	)
	return first_page_menu


def second_page(_):
	controll_button = [InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data=f"settings_back_helper")]
	second_page_menu = InlineKeyboardMarkup(
		[
			[InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7"), InlineKeyboardButton(text=_["H_B_19"], callback_data="help_callback hb19"),InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14")],
			[InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15"), InlineKeyboardButton(text=_["H_B_16"], callback_data="help_callback hb16"),InlineKeyboardButton(text=_["H_B_17"], callback_data="help_callback hb17")],
			[InlineKeyboardButton(text=_["H_B_18"], callback_data="help_callback hb18"), InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13")],
                        [InlineKeyboardButton(text=_["H_B_20"], callback_data="help_callback hb20"), InlineKeyboardButton(text=_["H_B_22"], callback_data="help_callback hb22")],
                        [InlineKeyboardButton(text=_["H_B_21"], callback_data="help_callback hb21")],
			controll_button,
		]
	)
	return second_page_menu
    

def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
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
                    text="🍁αԃɱιɳ🍁",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="🔺αυƭɦ🔺",
                    callback_data="help_callback hb2",
                ),
            
                InlineKeyboardButton(
                    text="♨️вℓσ¢к♨️",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📣ɠ¢αʂƭ📣",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="🚫ɠɓαɳ🚫",
                    callback_data="help_callback hb12",
                ),
                InlineKeyboardButton(
                    text="🍷ℓყɾเ¢ʂ🍷",
                    callback_data="help_callback hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️քℓαყℓเʂƭ🎙️",
                    callback_data="help_callback hb6",
                ),
                InlineKeyboardButton(
                    text="🎸ѵσเ¢ε-¢ɦαƭ🎸",
                    callback_data="help_callback hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️ρℓαყ🕹️",
                    callback_data="help_callback hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸ʂ𝖚∂σ🍸",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️SƬΛᏒƬ⚜️",
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
                ),

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

