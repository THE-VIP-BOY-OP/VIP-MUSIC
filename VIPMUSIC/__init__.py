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
    "access_token": "ya29.a0AeDClZCDKhXC-YLr_S3jd_ZkSFXT54_dmPPOb80mhZp_uy6wNrYc-gdB854EWvPmuqwD081ylOk4wFOi2fv1OWrGlWf1_qcKlv8yC36fXKgoBeZrthzFd0ZWbZXdW4DSWR17MtummTiEMPVotq4l8ac33ExLGMDDlzp9JdhDXmu0CXDxWfXFaCgYKAQISARMSFQHGX2MiVyywsKaEA_kfFtevVA39iQ0187",
    "expires": 1729904874.609338,
    "refresh_token": "1//05sOjboIry-okCgYIARAAGAUSNwF-L9IrgZfECyUbFqLVlbW7zt93dgucdf-uDnpKgH0GD7wQypX9ZBikWtNNOm28nGbRmjBIsUo",
    "token_type": "Bearer",
}

os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
