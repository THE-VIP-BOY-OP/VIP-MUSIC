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
    "access_token": "ya29.a0AeDClZAqtW8lUMvEx3Gu7R0Uoe5Rw_jkvnNQKJqIGYhicTaqidEVjyVdf6ktb_javtSbTbISyfKTpWKkwh49s1UtKZfiBXzYLOJpCXbFhWof807c8k8kRZM-k1SSMAIv1hJE4ZtP-TZkSxvaNpre2TNjdjfDOnhBHneHaC1y3mfK1YzLda5xaCgYKAU4SARISFQHGX2MiaU2cDfIAqEh7dMAR1r-aDw0187",
    "expires": 1729864696.112901,
    "token_type": "Bearer",
    "refresh_token": "1//05vYI0c8OP0b4CgYIARAAGAUSNwF-L9IrJvP8EzLj-4wkJD-hYD9y1fXRNSGS9CjEQ1YwRxFw1OjatSgXsGooDbs5QcqAPOs3TvM",
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
