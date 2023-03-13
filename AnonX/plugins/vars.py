import asyncio

from pyrogram import filters

import config
from strings import get_command
from AnonX import app
from AnonX.misc import SUDOERS
from AnonX.utils.database.memorydatabase import get_video_limit
from AnonX.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.. Getting your config"
    )
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[Repo]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "Yes"
    else:
        pvt = "No"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "Yes"
    else:
        a_sug = "No"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "Yes"
    else:
        down = "No"

    if not config.GITHUB_REPO:
        git = "No"
    else:
        git = f"[Repo]({config.GITHUB_REPO})"
    if not config.START_IMG_URL:
        start = "No"
    else:
        start = f"[Image]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "No"
    else:
        s_c = f"[Channel]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "No"
    else:
        s_g = f"[Group]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "No"
    else:
        token = "Yes"
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        sotify = "No"
    else:
        sotify = "Yes"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**MUSIC BOT CONFIG:**

**<u>Basic Vars:</u>**
`MUSIC_BOT_NAME` : **NIKAL MADHERCHODD**
`DURATION_LIMIT` : **NIKAL MADHERCHODD**
`SONG_DOWNLOAD_DURATION_LIMIT` :**NIKAL MADHERCHODD**
`OWNER_ID` : **{owner_id}**
    
**<u>Custom Repo Vars:</u>**
`UPSTREAM_REPO` : **NIKAL MADHERCHODD**
`UPSTREAM_BRANCH` : **NIKAL MADHERCHODD**
`GITHUB_REPO` :**NIKAL MADHERCHODD**
`GIT_TOKEN `:**NIKAL MADHERCHODD**


**<u>Bot Vars:</u>**
`AUTO_LEAVING_ASSISTANT` : **NIKAL MADHERCHODD**
`ASSISTANT_LEAVE_TIME` : **NIKAL MADHERCHODD**
`AUTO_SUGGESTION_MODE` :**NIKAL MADHERCHODD**
`AUTO_SUGGESTION_TIME` : **NIKAL MADHERCHODD**
`AUTO_DOWNLOADS_CLEAR` : **NIKAL MADHERCHODD**
`PRIVATE_BOT_MODE` : **NIKAL MADHERCHODD**
`YOUTUBE_EDIT_SLEEP` : **NIKAL MADHERCHODD**
`TELEGRAM_EDIT_SLEEP` :**NIKAL MADHERCHODD**
`CLEANMODE_MINS` : **NIKAL MADHERCHODD**
`VIDEO_STREAM_LIMIT` : **NIKAL MADHERCHODD**
`SERVER_PLAYLIST_LIMIT` :**NIKAL MADHERCHODD**
`PLAYLIST_FETCH_LIMIT` :**NIKAL MADHERCHODD**

**<u>Spotify Vars:</u>**
`SPOTIFY_CLIENT_ID` :**NIKAL MADHERCHODD**
`SPOTIFY_CLIENT_SECRET` : **NIKAL MADHERCHODD**

**<u>Playsize Vars:</u>**
`TG_AUDIO_FILESIZE_LIMIT` :**NIKAL MADHERCHODD**
`TG_VIDEO_FILESIZE_LIMIT` :**NIKAL MADHERCHODD**

**<u>URL Vars:</u>**
`SUPPORT_CHANNEL` : **NIKAL MADHERCHODD**
`SUPPORT_GROUP` : **NIKAL MADHERCHODD**
`START_IMG_URL` : **NIKAL MADHERCHODD**
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
