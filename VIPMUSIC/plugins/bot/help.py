from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from VIPMUSIC import app
from VIPMUSIC.utils import help_pannel
from VIPMUSIC.utils.database import get_lang
from VIPMUSIC.utils.decorators.language import LanguageStart, languageCB
from VIPMUSIC.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from VIPMUSIC.misc import SUDOERS

@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
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
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )


@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb9":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                   "😎𝗣𝗔𝗛𝗟𝗘 𓆩𝗩𝗜𝗣𓆪 𝗞𝗢 𝗣𝗔𝗣𝗔 𝗕𝗢𝗟 𝗝𝗔𝗞𝗘 😆😆", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_9, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    
     if cb == "next_page":
        # Logic to handle next page action
        await CallbackQuery.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Additional Button 1",
                            callback_data="help_callback hb14",
                        ),
                        InlineKeyboardButton(
                            text="Additional Button 2",
                            callback_data="help_callback hb15",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Additional Button 3",
                            callback_data="help_callback hb16",
                        ),
                        InlineKeyboardButton(
                            text="Additional Button 4",
                            callback_data="help_callback hb17",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Additional Button 5",
                            callback_data="help_callback hb18",
                        ),
                        InlineKeyboardButton(
                            text="Additional Button 6",
                            callback_data="help_callback hb19",
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            text="Additional Button 7",
                            callback_data="help_callback hb20",
                        ),
                        InlineKeyboardButton(
                            text="Additional Button 8",
                            callback_data="help_callback hb21",
                        ),
                    ],
                ]
            )
        )

    # Logic to handle other callback data
    elif cb in ("hb1", "hb2", ..., "hb21"):
        await CallbackQuery.edit_message_text(
            helpers[f"HELP_{cb[2:]}"], reply_markup=keyboard
        )
