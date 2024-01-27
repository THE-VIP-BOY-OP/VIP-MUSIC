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

#Callback Query

DOCS_MESSAGE = "Let's start reading the docs"

DOCS_BUTTONS = [

[

InlineKeyboardButton('START READING', callback_data="START READING")

)

]

@bot.on_message(filters.command("doc") & filters.private)

def doc(bot, message):

message.reply(

text = DOCS MESSAGE,

reply_markup = InlineKeyboardMarkup(DOCS_BUTTONS)

@bot.on_callback_query()

def callback_query(Client, CallbackQuery):

if CallbackQuery.data == "START READING":

PAGE1_TEXT = "This is the first page"

PAGE1_BUTTON = [

[


InlineKeyboardButton("BACK TO MENU", callback_data="GO TO MENU"),

InlineKeyboardButton("READ PAGE 2", callback_data="GO TO PAGE 2")

]

]

CallbackQuery.edit_message_text(

PAGE1_TEXT,

reply_markup = InlineKeyboardMarkup (PAGE1_BUTTON)

)

elif CallbackQuery.data == "GO TO MENU":

CallbackQuery.edit_message_text(

DOCS_MESSAGE,

reply_markup = InlineKeyboardMarkup(DOCS_BUTTONS)

)
elif CallbackQuery.data == "GO TO PAGE 2":

PAGE2_TEXT = "This is the second page"

PAGE2_BUTTON = [

InlineKeyboardButton("BACK TO PAGE 1", callback_data="START READING")

]

CallbackQuery.edit_message_text(

PAGE2_TEXT,

reply_markup = InlineKeyboardMarkup (PAGE2_BUTTON)

)
