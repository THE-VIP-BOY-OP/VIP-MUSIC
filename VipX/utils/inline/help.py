from typing import Union
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext.dispatcher import run_async
from telegram.ext import CallbackContext
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
        InlineKeyboardButton(
            text="★ ηєϰᴛ ★", callback_data=f"Next_"
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
                InlineKeyboardButton(
                    text="★ ηєϰᴛ ★", callback_data=f"settings_back_helper"
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

@run_async
def Music_about_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == "Next_":
        query.message.edit_text(
            text=f"""
 **👀𝐇𝐞𝐲""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        
                InlineKeyboardButton(
                    text="🍁αԃɱιɳ🍁",
                    callback_data="Music_1",
                ),
                
                ]
              ]
           ),
        )
    elif query.data == "Music_1":
        query.message.edit_text(
            text=f"*» 🎄ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ🎄 «*"
            f"""


ᴊᴜsᴛ ᴀᴅᴅ ᴄ ɪɴ ᴛʜᴇ sᴛᴀʀᴛɪɴɢ ᴏғ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴛᴏ ᴜsᴇ ᴛʜᴇᴍ ғᴏʀ ᴄʜᴀɴɴᴇʟ.

/pause : ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

/resume : ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.

/skip : sᴋɪᴩ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ.

/end ᴏʀ /stop : ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.

/player : ɢᴇᴛ ᴀ ɪɴᴛᴇʀᴀᴄᴛɪᴠᴇ ᴩʟᴀʏᴇʀ ᴩᴀɴᴇʟ.

/queue : sʜᴏᴡs ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.

☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆
""")
