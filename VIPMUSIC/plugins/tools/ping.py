from datetime import datetime
import requests
from io import BytesIO

from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app
from VIPMUSIC.core.call import VIP
from VIPMUSIC.utils import bot_sys_stats
from VIPMUSIC.utils.decorators.language import language
from VIPMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


CARBON_API = "https://carbonara.vercel.app/api/cook"
CARBON_DEFAULT_THEME = "3024-night"


@app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    code = f"""
    from datetime import datetime
    import requests
    from io import BytesIO

    from pyrogram import filters
    from pyrogram.types import Message

    from VIPMUSIC import app
    from VIPMUSIC.core.call import VIP
    from VIPMUSIC.utils import bot_sys_stats
    from VIPMUSIC.utils.decorators.language import language
    from VIPMUSIC.utils.inline import supp_markup
    from config import BANNED_USERS, PING_IMG_URL


    CARBON_API = "https://carbonara.vercel.app/api/cook"
    CARBON_DEFAULT_THEME = "3024-night"


    @app.on_message(filters.command("ping", prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~BANNED_USERS)
    @language
    async def ping_com(client, message: Message, _):
        start = datetime.now()
        code = f\"\"\"{message.text}\"\"\"
        data = {
            "code": code,
            "theme": CARBON_DEFAULT_THEME,
            "backgroundColor": "rgba(171, 184, 195, 1)",
            "lineNumbers": False,
            "dropShadow": True,
            "dropShadowOffsetY": "3px",
            "dropShadowBlurRadius": "15px",
            "windowControls": True,
            "fontFamily": "Hack",
            "exportSize": "2x",
        }
        response = requests.post(CARBON_API, json=data)
        if response.status_code == 200:
            img_url = response.json()["data"]
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_bytes = BytesIO(img_response.content)
                await message.reply_photo(img_bytes, caption=_["ping_1"].format(app.mention))
            else:
                await message.reply_text("Failed to fetch Carbon image.")
        else:
            await message.reply_text("Failed to generate Carbon image.")
        """
    data = {
        "code": code,
        "theme": CARBON_DEFAULT_THEME,
        "backgroundColor": "rgba(171, 184, 195, 1)",
        "lineNumbers": False,
        "dropShadow": True,
        "dropShadowOffsetY": "3px",
        "dropShadowBlurRadius": "15px",
        "windowControls": True,
        "fontFamily": "Hack",
        "exportSize": "2x",
    }
    response = requests.post(CARBON_API, json=data)
    if response.status_code == 200:
        img_url = response.json()["data"]
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            img_bytes = BytesIO(img_response.content)
            await message.reply_photo(img_bytes, caption=_["ping_1"].format(app.mention))
        else:
            await message.reply_text("Failed to fetch Carbon image.")
    else:
        await message.reply_text("Failed to generate Carbon image.")
