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

YOUTUBE = {
    "access_token": "ya29.a0AeDClZDe07TKjHH6aQ94qq82lX6kXt-mEE0vT_5h9mta3BocIyZlFyy6NHfs_zh4L_ZFZe8JneQNqPFmRrpFFzP23NCluVtrsCkOgRkyyeq_8eLy292K9ns8b-S8Nmz0fahqZRyXDC12Om7wCGdODgXCRPFwsmPK5z2QjfgiWf1gPsrE5tQXaCgYKATESARMSFQHGX2MihtLX6e7SOKX7Vtgk5ErGHQ0187",
    "expires": 1729969967.445299,
    "refresh_token": "1//05jQWBk3WX51ZCgYIARAAGAUSNwF-L9IrrkvSReXsWVfbI6cN-pQrog8fNFBMEM1vKOk8fiDhgdNd2rPqoEWvIT-yDcwGZNc2atE",
    "token_type": "Bearer"
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
