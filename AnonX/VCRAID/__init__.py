from config import *
from pytgcalls import PyTgCalls
from pyrogram import Client, filters

API_ID = API_ID
API_HASH = API_HASH
SESSION = STRING_SESSION
SUDO_USERS = OWNER_ID


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCRAID.plugins"))
call_py = PyTgCalls(bot)
