import asyncio
import random
from datetime import datetime, timedelta

import config
from VIPMUSIC import app
from VIPMUSIC.utils.decorators.language import language, languageCB
from VIPMUSIC.utils.database import (get_lang, 
                                      get_served_users as get_private_served_chats,
                                      get_served_chats,
                                       )
from VIPMUSIC.core.mongo import mongodb

AUTO_SUGGESTION_MODE = "True"
CLEANMODE_DELETE_MINS = 5
CLEANMODE_MINS = 5
AUTO_SUGGESTION_TIME = 5400
AUTO_DOWNLOADS_CLEAR = True

LEAVE_TIME = config.AUTO_SUGGESTION_TIME
PRIVATE_BOT_MODE = False
cleandb = mongodb.cleanmode
suggdb = mongodb.suggestion
suggestion = {}
cleanmode = []

strings = []
suggestor = {}

# SUGGESTION

async def is_suggestion(chat_id: int) -> bool:
    mode = suggestion.get(chat_id)
    if not mode:
        user = await suggdb.find_one({"chat_id": chat_id})
        if not user:
            suggestion[chat_id] = True
            return True
        suggestion[chat_id] = False
        return False
    return mode


async def suggestion_on(chat_id: int):
    suggestion[chat_id] = True
    user = await suggdb.find_one({"chat_id": chat_id})
    if user:
        return await suggdb.delete_one({"chat_id": chat_id})


async def suggestion_off(chat_id: int):
    suggestion[chat_id] = False
    user = await suggdb.find_one({"chat_id": chat_id})
    if not user:
        return await suggdb.insert_one({"chat_id": chat_id})

# Clean Mode
async def is_cleanmode_on(chat_id: int) -> bool:
    if chat_id not in cleanmode:
        return True
    else:
        return False


async def cleanmode_off(chat_id: int):
    if chat_id not in cleanmode:
        cleanmode.append(chat_id)


async def cleanmode_on(chat_id: int):
    try:
        cleanmode.remove(chat_id)
    except:
        pass


for item in get_string("en"):
    if item[0:3] == "sug" and item != "sug_0":
        strings.append(item)


async def dont_do_this():
    if config.AUTO_SUGGESTION_MODE == str(True):
        while not await asyncio.sleep(LEAVE_TIME):
            try:
                chats = []
                if config.PRIVATE_BOT_MODE == str(True):
                    schats = await get_private_served_chats()
                else:
                    schats = await get_served_chats()
                for chat in schats:
                    chats.append(int(chat["chat_id"]))
                total = len(chats)
                if total >= 100:
                    total //= 10
                send_to = 0
                random.shuffle(chats)
                for x in chats:
                    if send_to == total:
                        break
                    if x == config.LOGGER_ID:
                        continue
                    if not await is_suggestion(x):
                        continue
                    try:
                        language = await get_lang(x)
                        _ = get_string(language)
                    except:
                        _ = get_string("en")
                    string = random.choice(strings)
                    previous = suggestor.get(x)
                    if previous:
                        while previous == (string.split("_")[1]):
                            string = random.choice(strings)
                    suggestor[x] = string.split("_")[1]
                    try:
                        msg = _["sug_0"] + _[string]
                        sent = await app.send_message(x, msg)
                        if x not in clean:
                            clean[x] = []
                        time_now = datetime.now()
                        put = {
                            "msg_id": sent.message_id,
                            "timer_after": time_now
                            + timedelta(
                                minutes=config.CLEANMODE_DELETE_MINS
                            ),
                        }
                        clean[x].append(put)
                        send_to += 1
                    except:
                        pass
            except:
                pass


asyncio.create_task(dont_do_this())
