from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from VIPMUSIC import app


# Define constants for pagination
BUTTONS_PER_PAGE = 6

# Modify the help_pannel function to split buttons into pages
def help_pannel(_, START: Union[bool, int] = None, page: int = 1):
    buttons_page_1 = [
        [
            InlineKeyboardButton(
                text="🍁αԃɱιɳ🍁",
                callback_data="help_callback hb1",
            ),
            InlineKeyboardButton(
                text="🔺αυƭɦ🔺",
                callback_data="help_callback hb2",
            ),
            ...
        ],
        ...
    ]
    
    buttons_page_2 = [
        [
            InlineKeyboardButton(
                text="🎙️քℓαყℓเʂƭ🎙️",
                callback_data="help_callback hb6",
            ),
            ...
        ],
        ...
    ]

    # Determine which page to display
    buttons_to_display = buttons_page_1 if page == 1 else buttons_page_2
    
    # Add back button if not on the first page
    if page > 1:
        buttons_to_display.append([InlineKeyboardButton(text="Back", callback_data="back")])

    # Create InlineKeyboardMarkup with the buttons to display
    upl = InlineKeyboardMarkup(buttons_to_display)
    return upl

# Modify the helper_cb function to handle pagination
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)

    # Handle pagination
    if cb == "back":
        # Go back to the previous page
        current_page = int(callback_data.split()[-1])
        new_page = current_page - 1 if current_page > 1 else 1
        keyboard = help_pannel(_, page=new_page)
        await CallbackQuery.edit_message_reply_markup(reply_markup=keyboard)
        return await CallbackQuery.answer()

    # Handle other callbacks as before
    ...

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
