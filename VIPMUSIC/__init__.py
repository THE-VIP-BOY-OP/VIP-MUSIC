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
    "access_token": "ya29.a0AcM612x6xjTKmTpSHstn1vpFe4R-4nlC-a537bZMFvBAKrDA7MdjgKj71_dLwijsrP5ZLSKFIUNQyHpFOjGh5ifATiFHyXhc4sArPYlbIa_9PqfVJMyfDWLa8vw19SZwHo--fxjDusyV5nqvoGYNcIqyTN8zG7gJl3YIvcSa0P0-rLQNAs0AaCgYKAb0SARMSFQHGX2MivXte9hRxxKS07uayRvAw7w0187",
    "expires": 1729406829.524444,
    "refresh_token": "1//05vYI0c8OP0b4CgYIARAAGAUSNwF-L9IrJvP8EzLj-4wkJD-hYD9y1fXRNSGS9CjEQ1YwRxFw1OjatSgXsGooDbs5QcqAPOs3TvM",
    "token_type": "Bearer",
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
