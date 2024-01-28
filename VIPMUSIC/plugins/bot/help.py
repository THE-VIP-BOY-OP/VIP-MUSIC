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

import time
import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, Message
from youtubesearchpython.__future__ import VideosSearch
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
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from strings import get_string
import config
from VIPMUSIC.misc import _boot_
from VIPMUSIC.plugins.sudo.sudoers import sudoers_list
from VIPMUSIC.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from VIPMUSIC.utils.decorators.language import LanguageStart
from VIPMUSIC.utils.formatters import get_readable_time
from VIPMUSIC.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

START_MESSAGE = "**📝𝐅ree  𝐕c  𝐒ong  𝐏layer  𝐁oт❤️**\n\n➻ 24 × 7 𝗥υn + 𝗟ᴀɢ 𝗙ʀᴇᴇ..\n➖➖➖➖➖➖➖➖➖➖\n➻ 𝗧agall 𝗢ɴe 𝗕y 𝗢ɴe...\n➖➖➖➖➖➖➖➖➖➖\n➻ 𝗜nvιтeall 𝗙or 𝗝oιn 𝗩c...\n➖➖➖➖➖➖➖➖➖➖\n➻ 𝗦ʜᴀʏʀɪ 𝗙ᴇᴀᴛᴜʀᴇ...\n➖➖➖➖➖➖➖➖➖➖\n➻ 𝗡o 𝗔ny 𝗔dѕ/𝗣roмo... ✨\n\n**🌺 ᴀᴅᴅ ᴍᴇ & ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ʜᴀɴᴅʟᴇ ʏᴏᴜʀ ᴍᴜꜱɪᴄ Qᴜᴇʀɪᴇꜱ.**\n\n🏓 𝐌𝐲 𝐑𝐞𝐩𝐨 ➪ **[ᴄʟɪᴄᴋ ʜᴇʀᴇ](https://github.com/THE-VIP-BOY-OP/VIP-MUSIC) 💞**\n📡 𝐌𝐚𝐝𝐞 𝐁𝐲 ➪ **[ᴠɪᴘ ✯ ʙᴏʏ](https://t.me/the_vip_boy) 💞**"
            
DOCS_MESSAGE = "**๏ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴏᴘᴇɴ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ🥀**"

DOCS_BUTTONS = [
    [
        InlineKeyboardButton('๏ sᴛᴀʀᴛ ๏', callback_data="STARTUP"),
        InlineKeyboardButton('๏ ʜᴇʟᴘ ๏', callback_data="START READING")]
]

@bot.on_message(filters.command("help") & ~BANNED_USERS)
def doc(bot, message):
    bot.send_photo(
        chat_id=message.chat.id,
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

    elif callback_query.data == "HELPS":
        # Handle "HELPS" callback data
        PAGE1_TEXT = "**๏ ᴛʜɪs ɪs ʏᴏᴜʀ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ๏**"
        PAGE1_BUTTON = [
            [InlineKeyboardButton("Back", callback_data="GO TO MENU")]
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

    elif callback_query.data == "STARTUP":
        callback_query.edit_message_text(
            START_MESSAGE,
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        
    elif callback_query.data == "GO TO PAGE 2":
        PAGE2_TEXT = "**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇ ʜᴇʟᴘ ๏**"
        PAGE2_BUTTON = [
            [
                InlineKeyboardButton(
                    text="🍁sᴛᴀᴛs🍁",
                    callback_data="hb7",
                ),
                InlineKeyboardButton(
                    text="🎸ɪɴғᴏ🎸",
                    callback_data="hb19",
                ),
            
                InlineKeyboardButton(
                    text="♨️sᴏɴɢ♨️",
                    callback_data="hb14",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="📣sᴘᴇᴇᴅ📣",
                    callback_data="hb15",
                ),
                InlineKeyboardButton(
                    text="🚫ᴀᴄᴛɪᴏɴ🚫",
                    callback_data="hb16",
                ),
                InlineKeyboardButton(
                    text="🍷sᴛɪᴄᴋᴇʀ🍷",
                    callback_data="hb17",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎙️sʜᴀʏʀɪ🎙️",
                    callback_data="hb18",
                ),
                InlineKeyboardButton(
                    text="🔺ᴛᴀɢᴀʟʟ🔺",
                    callback_data="hb13",
                ),
            ],
            [
           
                InlineKeyboardButton(
                    text="🕹️ɢʀᴏᴜᴘ🕹️",
                    callback_data="hb20",
                ),
            
            
                InlineKeyboardButton(
                    text="🍸Iᴍᴀɢᴇ🍸",
                    callback_data="hb22",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚜️ᴇxᴛʀᴀ⚜️",
                    callback_data="hb21",
                ),
            ],
            [
                InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏",
                    callback_data="START READING"
                )
            ]
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
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
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
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_13,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb14":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_14,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb15":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_15,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb16":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_16,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb17":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_17,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )

    elif callback_query.data == "hb18":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_18,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb19":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_19,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb20":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_20,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        
    elif callback_query.data == "hb21":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_21,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
    
    elif callback_query.data == "hb22":
        PAGE2_BUTTON = [
            [InlineKeyboardButton("๏ ʙᴀᴄᴋ ๏", callback_data="GO TO PAGE 2")]
        ]
        callback_query.edit_message_text(
            helpers.HELP_22,
            reply_markup=InlineKeyboardMarkup(PAGE2_BUTTON)
        )
        






#start.py functions





YUMI_PICS = [
"https://telegra.ph/file/3ed81ef4e352a691fb0b4.jpg",
"https://telegra.ph/file/3134ed3b57eb051b8c363.jpg",
"https://telegra.ph/file/6ca0813b719b6ade1c250.jpg",
"https://telegra.ph/file/5a2cbb9deb62ba4b122e4.jpg",
"https://telegra.ph/file/cb09d52a9555883eb0f61.jpg"

]

buttons = [
        [
            InlineKeyboardButton(
                text="•─╼⃝𖠁𝐀ᴅᴅ ◈ 𝐌ᴇ ◈ 𝐁ᴀʙʏ𖠁⃝╾─•",
                url=f"https://t.me/{bot.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ🥀", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="START READING")
        ],
    ]

@bot.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.reply_photo(
            photo=config.START_IMG_URL,
            caption=_["start_2"].format(message.from_user.mention, bot.mention),
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if await is_on_off(2):  # Ensure this function is asynchronous
        return await bot.send_message(
            chat_id=config.LOGGER_ID,
            text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
        )



@bot.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        photo=config.START_IMG_URL,
        caption=_["start_1"].format(bot.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
    return await add_served_chat(message.chat.id)

