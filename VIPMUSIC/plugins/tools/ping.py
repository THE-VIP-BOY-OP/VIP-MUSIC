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
    code = (
        f"from datetime import datetime\n"
        f"import requests\n"
        f"from io import BytesIO\n"
        f"from pyrogram import filters\n"
        f"from pyrogram.types import Message\n"
        f"from VIPMUSIC import app\n"
        f"from VIPMUSIC.core.call import VIP\n"
        f"from VIPMUSIC.utils import bot_sys_stats\n"
        f"from VIPMUSIC.utils.decorators.language import language\n"
        f"from VIPMUSIC.utils.inline import supp_markup\n"
        f"from config import BANNED_USERS, PING_IMG_URL\n"
        f"\n"
        f"CARBON_API = 'https://carbonara.vercel.app/api/cook'\n"
        f"CARBON_DEFAULT_THEME = '3024-night'\n"
        f"\n"
        f"@app.on_message(filters.command('ping', prefixes=['/', '!', '%', ',', '', '.', '@', '#']) & ~BANNED_USERS)\n"
        f"@language\n"
        f"async def ping_com(client, message: Message, _):\n"
        f"    start = datetime.now()\n"
        f"    code = (\n"
        f"        # Your original code here\n"
        f"    )\n"
        f"    data = {{\n"
        f"        'code': code,\n"
        f"        'theme': CARBON_DEFAULT_THEME,\n"
        f"        'backgroundColor': 'rgba(171, 184, 195, 1)',\n"
        f"        'lineNumbers': False,\n"
        f"        'dropShadow': True,\n"
        f"        'dropShadowOffsetY': '3px',\n"
        f"        'dropShadowBlurRadius': '15px',\n"
        f"        'windowControls': True,\n"
        f"        'fontFamily': 'Hack',\n"
        f"        'exportSize': '2x',\n"
        f"    }}\n"
        f"    response = requests.post(CARBON_API, json=data)\n"
        f"    if response.status_code == 200:\n"
        f"        img_url = response.json()['data']\n"
        f"        img_response = requests.get(img_url)\n"
        f"        if img_response.status_code == 200:\n"
        f"            img_bytes = BytesIO(img_response.content)\n"
        f"            await message.reply_photo(img_bytes, caption=_['ping_1'].format(app.mention))\n"
        f"        else:\n"
        f"            await message.reply_text('Failed to fetch Carbon image.')\n"
        f"    else:\n"
        f"        await message.reply_text('Failed to generate Carbon image.')\n"
    )
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
