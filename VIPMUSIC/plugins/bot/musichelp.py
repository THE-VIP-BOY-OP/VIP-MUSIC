from typing import Union

from pyrogram import Client, filters, types
from pyrogram.types import CallbackQuery

from config import BANNED_USERS, START_IMG_URL
from config import SUPPORT_GROUP as SUPPORT_CHAT
from strings import get_string, helpers
from VIPMUSIC import app
from VIPMUSIC.utils import music_pannel
from VIPMUSIC.utils.database import get_lang
from VIPMUSIC.utils.decorators.language import languageCB
from VIPMUSIC.utils.inline.help import (
    about_help_panel,
    feature_help_panel,
    music_back_markup,
    music_help_panel,
    support_help_panel,
)


@app.on_callback_query(filters.regex("music") & ~BANNED_USERS)
async def music_private(client: app, update: Union[types.Message, types.CallbackQuery]):

    is_callback = isinstance(update, types.CallbackQuery)

    if is_callback:

        try:

            await update.answer()

        except:

            pass

        chat_id = update.message.chat.id

        language = await get_lang(chat_id)

        _ = get_string(language)

        keyboard = music_pannel(_, True)

        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )

    else:

        try:

            await update.delete()

        except:

            pass

        language = await get_lang(update.chat.id)

        _ = get_string(language)

        keyboard = music_pannel(_)

        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_callback_query(filters.regex("music_callback") & ~BANNED_USERS)
@languageCB
async def music_helper_cb(client, CallbackQuery, _):

    callback_data = CallbackQuery.data.strip()

    cb = callback_data.split(None, 1)[1]

    keyboard = music_back_markup(_)

    if cb == "hb1":

        await CallbackQuery.edit_message_text(helpers.HELP_1, reply_markup=keyboard)

    elif cb == "hb2":

        await CallbackQuery.edit_message_text(helpers.HELP_2, reply_markup=keyboard)

    elif cb == "hb3":

        await CallbackQuery.edit_message_text(helpers.HELP_3, reply_markup=keyboard)

    elif cb == "hb4":

        await CallbackQuery.edit_message_text(helpers.HELP_4, reply_markup=keyboard)

    elif cb == "hb5":

        await CallbackQuery.edit_message_text(helpers.HELP_5, reply_markup=keyboard)

    elif cb == "hb6":

        await CallbackQuery.edit_message_text(helpers.HELP_6, reply_markup=keyboard)

    elif cb == "hb7":

        await CallbackQuery.edit_message_text(helpers.HELP_7, reply_markup=keyboard)

    elif cb == "hb8":

        await CallbackQuery.edit_message_text(helpers.HELP_8, reply_markup=keyboard)

    elif cb == "hb9":

        await CallbackQuery.edit_message_text(helpers.HELP_9, reply_markup=keyboard)

    elif cb == "hb10":

        await CallbackQuery.edit_message_text(helpers.HELP_10, reply_markup=keyboard)

    elif cb == "hb11":

        await CallbackQuery.edit_message_text(helpers.HELP_11, reply_markup=keyboard)

    elif cb == "hb12":

        await CallbackQuery.edit_message_text(helpers.HELP_12, reply_markup=keyboard)

    elif cb == "hb13":

        await CallbackQuery.edit_message_text(helpers.HELP_13, reply_markup=keyboard)

    elif cb == "hb14":

        await CallbackQuery.edit_message_text(helpers.HELP_14, reply_markup=keyboard)

    elif cb == "hb15":

        await CallbackQuery.edit_message_text(helpers.HELP_15, reply_markup=keyboard)


@app.on_callback_query(filters.regex("developer"))
async def developer_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Here is the information about the developer...",
        reply_markup=about_help_panel(_),
    )


@app.on_callback_query(filters.regex("feature"))
async def feature_callback(client: Client, callback_query: CallbackQuery):
    keyboard = feature_help_panel(_)
    await callback_query.message.edit_text(
        "Here are the bot features...", reply_markup=InlineKeyboardMarkup(keyboard)
    )


@app.on_callback_query(filters.regex("home"))
async def home_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Welcome back to the home page!", reply_markup=about_help_panel(_)
    )


@app.on_callback_query(filters.regex("music"))
async def music_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Here are the music options...", reply_markup=music_back_markup(_)
    )


@app.on_callback_query(filters.regex("music_helper"))
async def settings_back_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Returning to all settings...", reply_markup=music_help_panel(_)
    )


@app.on_callback_query(filters.regex("music_back_helper"))
async def music_back_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Returning to music options...", reply_markup=feature_help_panel(_)
    )


# If the back button has different meanings in various panels, you can set different callbacks
@app.on_callback_query(filters.regex("support"))
async def back_button_callback(client: Client, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        "Returning to the previous menu...", reply_markup=support_help_panel(_)
    )
