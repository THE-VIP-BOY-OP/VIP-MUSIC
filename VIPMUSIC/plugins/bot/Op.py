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


DOCS_MESSAGE = "**๏ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴏᴘᴇɴ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ🥀**"

DOCS_BUTTONS = [
    [InlineKeyboardButton('๏ ʜᴇʟᴘ ๏', callback_data="START READING")]
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
                InlineKeyboardButton(
                    text="📣ɠ¢αʂƭ📣",
                    callback_data="hb4",
                ),
                InlineKeyboardButton(
                    text="🚫ɠɓαɳ🚫",
                    callback_data="hb12",
                ),
                InlineKeyboardButton(
                    text="🍷ℓყɾเ¢ʂ🍷",
                    callback_data="hb5",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️քℓαყℓเʂƭ🎙️",
                    callback_data="hb6",
                ),
                InlineKeyboardButton(
                    text="🎸ѵσเ¢ε-¢ɦαƭ🎸",
                    callback_data="hb10",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️ρℓαყ🕹️",
                    callback_data="hb8",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸ʂ𝖚∂σ🍸",
                    callback_data="hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️SƬΛᏒƬ⚜️",
                    callback_data="hb11",
                ),
            ],
            [
                InlineKeyboardButton("๏ ᴍᴇɴᴜ ๏", callback_data="GO TO MENU"),
                InlineKeyboardButton("๏ ɴᴇxᴛ ๏", callback_data="GO TO PAGE 2")
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
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            PAGE2_TEXT,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb1":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_1,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb2":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_2,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb3":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_3,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb4":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_4,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb5":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_5,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb6":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_6,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb7":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_7,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb8":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_8,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb9":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_9,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb10":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_10,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb11":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_11,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb12":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_12,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb13":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_13,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb14":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_14,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb15":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="START READING")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_15,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
)
    
