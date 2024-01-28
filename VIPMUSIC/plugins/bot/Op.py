from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from VIPMUSIC import app as bot
from VIPMUSIC.utils import help_pannel
from VIPMUSIC.utils.database import get_lang
from VIPMUSIC.utils.decorators.language import LanguageStart, languageCB
from VIPMUSIC.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers
from VIPMUSIC.misc import SUDOERS

from typing import Union
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from VIPMUSIC import app as bot
from strings import get_string

# Callback Query

DOCS_MESSAGE = "**๏ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴏᴘᴇɴ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ🥀**"

DOCS_BUTTONS = [
    [
        InlineKeyboardButton('๏ ʜᴇʟᴘ ๏', callback_data="START READING")
    ]
]

@bot.on_message(filters.command("doc"))
def doc(bot, message):
    message.reply_photo(
        photo=START_IMG_URL,
        caption=DOCS_MESSAGE,
        reply_markup=InlineKeyboardMarkup(DOCS_BUTTONS)
    )

@bot.on_callback_query()
def callback_query(client, callback_query):
    if callback_query.data == "START READING":
        PAGE1_TEXT = "**๏ ᴛʜɪs ɪs ᴍᴜsɪᴄ ʜᴇʟᴘ ๏**"
        PAGE1_BUTTON = [
            

             [
                InlineKeyboardButton(
                    text="🍁αԃɱιɳ🍁",
                    callback_data="hb1",
                ),
                InlineKeyboardButton(
                    text="🔺αυƭɦ🔺",
                    callback_data="hb2",
                ),
            
                InlineKeyboardButton(
                    text="♨️вℓσ¢к♨️",
                    callback_data="hb3",
                ),
             ],
             [
                InlineKeyboardButton("BACK TO MENU", callback_data="GO TO MENU"),
                InlineKeyboardButton("READ PAGE 2", callback_data="GO TO PAGE 2")
            ]
        ]
        callback_query.edit_message_text(
            PAGE1_TEXT,
            reply_markup=InlineKeyboardMarkup(PAGE1_BUTTON)
        )
    elif callback_query.data == "GO TO MENU":
        callback_query.edit_message_text(
            DOCS_MESSAGE,
            reply_markup=InlineKeyboardMarkup(DOCS_BUTTONS)
        )
    elif callback_query.data == "GO TO PAGE 2":
        PAGE2_TEXT = "**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇ ʜᴇʟᴘ ๏**"
        PAGE2_BUTTON = [
            [InlineKeyboardButton("BACK TO PAGE 1", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            PAGE2_TEXT,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
      )
      
   elif callback_query.data == "hb1":
        PAGE2_TEXT = "This is the second page"
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
