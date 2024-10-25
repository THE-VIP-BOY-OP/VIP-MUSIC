import json
import os

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.dir import dirr
from VIPMUSIC.core.git import git
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()

git()

dbb()

heroku()

sudo()

app = VIPBot()

userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
HELPABLE = {}
"""
YOUTUBE = {
    "access_token": "ya29.a0AeDClZBB45-A74hBincPf3KoXwbyoMXRL5sBIJa3bFyMoaX-XlFo2_Kan8M9Cgl4vbDgQh4STun6SBsm3iiUNXinWNa35x9ZzfTL6GzqCDJTP7Dijm32Y5d-xcSMRsSqntmGvFGtiIeWD_lcN0L9RRim4IkTaxgGFv2VcDSZ8dDQcYmTYrblaCgYKAa8SARMSFQHGX2Mi9zN0hAFOsodCY4xKbS2JNw0187",
    "expires": 1729874756.54895,
    "refresh_token": "1//05RuSol2SAJKxCgYIARAAGAUSNwF-L9IrYGaErHmm7Ij0mvCK7iZZwpbwDYnUfqQQdI0O6DGv7wIVmOkwvgIdYUqTSbW98NVJrB0",
    "token_type": "Bearer",
}
"""
YOUTUBE2 = {
    "access_token": "ya29.a0AcM612ziZLkUttobsw7iAbW6DQEpSE_yVxMN7cw0jYYB_Fa4KFeQVmcE6Hvzwz-dAuE-kQyDPkAsSzo21z3Ak_XZ047-8TRGJo_6jrzU5uFwqxUe0sZ-5Ho8Ysr9a3Gf8Gsc-d7Jd9JKoMzGozLoTNEAynBmzg2hyD4Xc5Y_4mO9KWMDUaNHaCgYKATMSARMSFQHGX2Mi4WVxr-yi2xDEGEsu63bGOQ0187",
    "expires": 1729902254.828461,
    "refresh_token": "1//05bxeXDV7UTJkCgYIARAAGAUSNwF-L9IrA0nhSzmZ1ktVPK9M98yHAssifTkVX6wBx4Ah1vCxvYS0PiG6XENXJ_eTqG5VpxXHqq8",
    "token_type": "Bearer",
}
os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE2)
