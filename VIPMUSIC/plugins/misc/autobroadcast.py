import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import AUTO_GCAST, AUTO_GCAST_MSG, LOGGER_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_served_chats

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://graph.org/file/760169f7f8dd536c50793.jpg"

MESSAGES = f"""**🌹𝗟𝗼𝗼𝗸𝗶𝗻𝗴 𝗙𝗼𝗿 𝗔𝗴𝗲𝗻𝘁 𝗪𝗼𝗿𝗸 𝗜𝗻 𝗡𝗲𝘄 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺 𝗝𝘂𝘀𝘁 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗠𝗲 𝗪𝗵𝗼 𝗪𝗮𝗻𝘁 𝘁𝗼 𝗪𝗼𝗿𝗸 𝗔𝘀 𝗔 𝗔𝗴𝗲𝗻𝘁.

𝗠𝘀𝗴 𝗛𝗲𝗿𝗲 :- @OkWinAgent

𝗦𝗮𝗹𝗹𝗲𝗿𝘆 𝗦𝘁𝗮𝗿𝘁𝘀 𝘄𝗶𝘁𝗵 𝟮 𝗔𝗰𝘁𝗶𝘃𝗲 𝗣𝗹𝗮𝘆𝗲𝗿.

🎁𝗥𝗲𝗴𝗶𝘀𝘁𝗲𝗿 𝗹𝗶𝗻𝗸 :- https://oko888.com/#/register?invitationCode=8284112316

➻ 𝗟𝗼𝘀𝘀 𝗥𝗲𝗳𝘂𝗻𝗱 𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 ✅
➥ 𝗣𝗿𝗲𝗱𝗶𝗰𝘁𝗶𝗼𝗻 » @OK_WIN_PREDICTIONS**"""
BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ Click & Get ₹100 ๏",
                url=f"https://okwin.one/#/register?invitationCode=8284112316",
            )
        ]
    ]
)

MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

🎧 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 🎧

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ᴛᴀɢᴀʟʟ, ᴠᴄᴛᴀɢ, ʙᴀɴ - ᴍᴜᴛᴇ, sʜᴀʏʀɪ, ʟᴜʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ᴇᴛᴄ... ❤️

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "๏ ᴋɪᴅɴᴀᴘ ᴍᴇ ๏",
                url=f"https://t.me/TG_VC_BOT?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGES

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass


async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTONS,
                    )
                    await asyncio.sleep(
                        20
                    )  # Sleep for 20 seconds between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 100000 seconds before next broadcast
        await asyncio.sleep(100000)


# Start the continuous broadcast loop if AUTO_GCASTS is True
if AUTO_GCASTS:
    asyncio.create_task(continuous_broadcast())
