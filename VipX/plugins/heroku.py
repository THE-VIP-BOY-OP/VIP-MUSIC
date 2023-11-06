import asyncio
import math
import os
import shutil
import socket
from datetime import datetime

import dotenv
import heroku3
import requests
import urllib3
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import filters

import config
from strings import get_command
from VipX import app
from VipX.misc import HAPP, SUDOERS, XCB
from VipX.utils.database import (get_active_chats,
                                       remove_active_chat,
                                       remove_active_video_chat)
from VipX.utils.decorators.language import language
from VipX.utils.pastebin import Vipbin

# Commands
GETLOG_COMMAND = get_command("GETLOG_COMMAND")
GETVAR_COMMAND = get_command("GETVAR_COMMAND")
DELVAR_COMMAND = get_command("DELVAR_COMMAND")
SETVAR_COMMAND = get_command("SETVAR_COMMAND")
USAGE_COMMAND = get_command("USAGE_COMMAND")
UPDATE_COMMAND = get_command("UPDATE_COMMAND")
REBOOT_COMMAND = get_command("REBOOT_COMMAND")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


async def is_heroku():
    return "heroku" in socket.getfqdn()


@app.on_message(filters.command(GETLOG_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def log_(client, message, _):
    try:
        if await is_heroku():
            if HAPP is None:
                return await message.reply_text(_["heroku_1"])
            data = HAPP.get_log()
            link = await Vipbin(data)
            return await message.reply_text(link)
        else:
            if os.path.exists(config.LOG_FILE_NAME):
                log = open(config.LOG_FILE_NAME)
                lines = log.readlines()
                data = ""
                try:
                    NUMB = int(message.text.split(None, 1)[1])
                except:
                    NUMB = 100
                for x in lines[-NUMB:]:
                    data += x
                link = await Vipbin(data)
                return await message.reply_text(link)
            else:
                return await message.reply_text(_["heroku_2"])
    except Exception as e:
        print(e)
        await message.reply_text(_["heroku_2"])


@app.on_message(filters.command(GETVAR_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def varget_(client, message, _):
    usage = _["heroku_3"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text(_["heroku_4"])
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(_["heroku_5"])
        output = dotenv.get_key(path, check_var)
        if not output:
            await message.reply_text(_["heroku_4"])
        else:
            return await message.reply_text(
                f"**{check_var}:** `{str(output)}`"
            )


@app.on_message(filters.command(DELVAR_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def vardel_(client, message, _):
    usage = _["heroku_6"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
        heroku_config = HAPP.config()
        if check_var in heroku_config:
            await message.reply_text(_["heroku_7"].format(check_var))
            del heroku_config[check_var]
        else:
            return await message.reply_text(_["heroku_4"])
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(_["heroku_5"])
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text(_["heroku_4"])
        else:
            await message.reply_text(_["heroku_7"].format(check_var))
            os.system(f"kill -9 {os.getpid()} && rm -rf VipXMusic.session && bash start")


@app.on_message(filters.command(SETVAR_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def set_var(client, message, _):
    usage = _["heroku_8"]
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
        heroku_config = HAPP.config()
        if to_set in heroku_config:
            await message.reply_text(_["heroku_9"].format(to_set))
        else:
            await message.reply_text(_["heroku_10"].format(to_set))
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(_["heroku_5"])
        dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            await message.reply_text(_["heroku_9"].format(to_set))
        else:
            await message.reply_text(_["heroku_10"].format(to_set))
        os.system(f"kill -9 {os.getpid()} && rm -rf VipXMusic.session && bash start")


@app.on_message(filters.command(USAGE_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def usage_dynos(client, message, _):
    ### Credits CatUserbot
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
    else:
        return await message.reply_text(_["heroku_11"])
    dyno = await message.reply_text(_["heroku_12"])
    Heroku = heroku3.from_key(config.HEROKU_API_KEY)
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**𝐇ᴇʀᴏᴋᴜ 𝐃ʏɴᴏs 𝐔sᴀɢᴇ**

<u>𝐔sᴀɢᴇ:</u>
ᴛᴏᴛᴀʟ ᴜsᴇᴅ: `{AppHours}`**ʜ**  `{AppMinutes}`**ᴍ**  [`{AppPercentage}`**%**]

<u>𝐑ᴇᴍᴀɪɴɪɴɢ 𝐃ʏɴᴏs:</u>
ᴛᴏᴛᴀʟ ʟᴇғᴛ: `{hours}`**ʜ**  `{minutes}`**ᴍ**  [`{percentage}`**%**]"""
    return await dyno.edit(text)


@app.on_message(filters.command(UPDATE_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & ~filters.edited & SUDOERS)
@language
async def update_(client, message, _):
    if await is_heroku():
        if HAPP is None:
            return await message.reply_text(_["heroku_1"])
    response = await message.reply_text(_["heroku_13"])
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(_["heroku_14"])
    except InvalidGitRepositoryError:
        return await response.edit(_["heroku_15"])
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[
        0
    ]  # main git repository
    for checks in repo.iter_commits(
        f"HEAD..origin/{config.UPSTREAM_BRANCH}"
    ):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("𝐁ᴏᴛ 𝐈s 𝐔ᴩ-𝐓ᴏ-𝐃ᴀᴛᴇ 𝐖ɪᴛʜ 𝐔ᴩsᴛʀᴇᴀᴍ 𝐑ᴇᴩᴏ !")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1)
            * (format % 10 < 4)
            * format
            % 10 :: 4
        ],
    )
    for info in repo.iter_commits(
        f"HEAD..origin/{config.UPSTREAM_BRANCH}"
    ):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    _update_response_ = "<b>𝐀 𝐍ᴇᴡ 𝐔ᴩᴅᴀᴛᴇ 𝐈s 𝐀ᴠᴀɪʟᴀʙʟᴇ 𝐅ᴏʀ 𝐓ʜᴇ 𝐁ᴏᴛ !</b>\n\n➣ 𝐏ᴜsʜɪɴɢ 𝐔ᴩᴅᴀᴛᴇs 𝐍ᴏᴡ</code>\n\n**<u>𝐔ᴩᴅᴀᴛᴇs:</u>**\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await Vipbin(updates)
        nrs = await response.edit(
            f"<b>𝐀 𝐍ᴇᴡ 𝐔ᴩᴅᴀᴛᴇ 𝐈s 𝐀ᴠᴀɪʟᴀʙʟᴇ 𝐅ᴏʀ 𝐓ʜᴇ 𝐁ᴏᴛ !</b>\n\n➣ 𝐏ᴜsʜɪɴɢ 𝐔ᴩᴅᴀᴛᴇs 𝐍ᴏᴡ</code>\n\n**<u>𝐔ᴩᴅᴀᴛᴇs:</u>**\n\n[ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs]({url})"
        )
    else:
        nrs = await response.edit(
            _final_updates_, disable_web_page_preview=True
        )
    os.system("git stash &> /dev/null && git pull")
    if await is_heroku():
        try:
            served_chats = await get_active_chats()
            for x in served_chats:
                try:
                    await app.send_message(
                        x,
                        f"𝐈 𝐀𝐦 𝐔𝐩𝐝𝐚𝐭𝐢𝐧𝐠...\n\n𝐘𝐨𝐮 𝐂𝐚𝐧 𝐉𝐨𝐢𝐧👇👇\n➣ @TG_FRIENDSS \n➣ @VIP_CREATORS",
                    )
                    await remove_active_chat(x)
                    await remove_active_video_chat(x)
                except Exception:
                    pass
            await response.edit(
                f"{nrs.text}\n\nʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ᴀɴᴅ ᴩᴜsʜ ᴄʜᴀɴɢᴇs."
            )
            os.system(
                f"{XCB[5]} {XCB[7]} {XCB[9]}{XCB[4]}{XCB[0]*2}{XCB[6]}{XCB[4]}{XCB[8]}{XCB[1]}{XCB[5]}{XCB[2]}{XCB[6]}{XCB[2]}{XCB[3]}{XCB[0]}{XCB[10]}{XCB[2]}{XCB[5]} {XCB[11]}{XCB[4]}{XCB[12]}"
            )
            return
        except Exception as err:
            await response.edit(
                f"{nrs.text}\n\nsᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ ᴡʜᴇɴ ᴛʀɪᴇᴅ ᴛᴏ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ, ᴩʟᴇᴀsᴇ ᴄʜᴇᴄᴋ ʟᴏɢs ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ's ᴡʀᴏɴɢ."
            )
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"ᴀɴ ᴇxᴄᴇᴩᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ ᴀᴛ #ᴜᴩᴅᴀᴛᴇʀ ᴅᴜᴇ ᴛᴏ: <code>{err}</code>",
            )
    else:
        served_chats = await get_active_chats()
        for x in served_chats:
            try:
                await app.send_message(
                    x,
                    f"{config.MUSIC_BOT_NAME} ʜᴀs ᴊᴜsᴛ ʀᴇsᴛᴀʀᴛᴇᴅ ʜᴇʀsᴇʟғ ғᴏʀ ᴜᴩᴅᴀᴛɪɴɢ ᴛʜᴇ ʙᴏᴛ. sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪssᴜᴇs.\n\nʏᴏᴜ ᴄᴀɴ sᴛᴀʀᴛ ᴩʟᴀʏɪɴɢ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 15-20 sᴇᴄᴏɴᴅs.",
                )
                await remove_active_chat(x)
                await remove_active_video_chat(x)
            except Exception:
                pass
        await response.edit(
            f"{nrs.text}\n\nʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ᴀɴᴅ ᴩᴜsʜ ᴄʜᴀɴɢᴇs !"
        )
        os.system("pip3 install -r requirements.txt")
        os.system(f"kill -9 {os.getpid()} && rm -rf VipXMusic.session && bash start")
        exit()


@app.on_message(filters.command(REBOOT_COMMAND, prefixes=["/", "!", "%", ",", "", ".", "@", "#"]) & SUDOERS)
async def restart_(_, message):
    response = await message.reply_text("𝐑ᴇsᴛᴀʀᴛɪɴɢ...")
    served_chats = await get_active_chats()
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f"𝐈 𝐀𝐦 𝐔𝐩𝐝𝐚𝐭𝐢𝐧𝐠...\n\n𝐘𝐨𝐮 𝐂𝐚𝐧 𝐉𝐨𝐢𝐧👇👇\n➣ @TG_FRIENDSS \n➣ @VIP_CREATORS",
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except Exception:
            pass
    A = "downloads"
    B = "raw_files"
    C = "cache"
    try:
        shutil.rmtree(A)
        shutil.rmtree(B)
        shutil.rmtree(C)
    except:
        pass
    await response.edit(
        "🥳𝐁𝐨𝐭 𝐑𝐞𝐬𝐭𝐚𝐫𝐭𝐢𝐧𝐠..."
    )
    os.system(f"kill -9 {os.getpid()} && rm -rf VipXMusic.session && bash start")

