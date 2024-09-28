from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def music_pannel(_):

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="music_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="music_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="music_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="music_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="music_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="music_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="music_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="music_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="music_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_10"],
                    callback_data="music_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["H_B_11"],
                    callback_data="music_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["H_B_12"],
                    callback_data="music_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_13"],
                    callback_data="music_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["H_B_14"],
                    callback_data="music_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["H_B_15"],
                    callback_data="music_callback hb15",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"feature",
                )
            ],
        ]
    )
    return upl
