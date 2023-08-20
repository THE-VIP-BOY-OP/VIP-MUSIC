# 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗜𝗡 𝗢𝗨𝗥 𝗟𝗘𝗔𝗥𝗡𝗜𝗡𝗚 𝗙𝗜𝗟𝗘 𝗗𝗔𝗥𝗟𝗜𝗡𝗚.
# 𝗜 𝗪𝗜𝗟𝗟 𝗧𝗘𝗟𝗟 𝗨𝗛 𝗔𝗕𝗢𝗨𝗧 𝗨𝗦𝗘 𝗢𝗙 𝗖𝗢𝗠𝗠𝗔𝗠𝗗𝗦.

from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VipX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# Command
PING_COMMAND = ["ping", "alive"]
START_COMMAND = ["start", "mstart"]
HELP_COMMAND = ["help", "mhelp"]
SETTINGS_COMMAND = ["settings", "setting"]
RELOAD_COMMAND = ["admincache", "reload"]
GSTATS_COMMAND = ["gstats", "globalstats"]
STATS_COMMAND = ["stats"]
LANGUAGE_COMMAND = ["language", "langs", "lang"]
PLAY_COMMAND = ["play", "gplay", "vplay", "cplay", "cvplay", "playforce", "vplayforce", "cplayforce", "cvplayforce"]
SHAYRI_COMMAND = ["shayri", "s_h", "love", "gf", "bf", "sayri", "sari", "sairi"]
RAID_COMMAND = ["vcraid", "raid"]
PLAYMODE_COMMAND = ["playmode", "mode"]
CHANNELPLAY_COMMAND = ["channelplay", "cplay", "cp"]
STREAM_COMMAND = ["stream", "cstream", "streamforce"]
PLAYLIST_COMMAND = ["playlist"]
DELETEPLAYLIST_COMMAND = ["deleteplaylist", "delplaylist"]
QUEUE_COMMAND = ["queue", "cqueue", "player", "cplayer", "playing", "cplaying"]
SONG_COMMAND = ["song", "video", "vsong", "music"]
LYRICS_COMMAND = ["lyrics", "lyric"]
AUTH_COMMAND = ["auth"]
UNAUTH_COMMAND = ["unauth"]
AUTHUSERS_COMMAND = ["authusers", "authlist"]
PAUSE_COMMAND = ["pause", "cpause"]
RESUME_COMMAND = ["resume", "cresume"]
STOP_COMMAND = ["stop", "end", "cstop", "cend"]
SKIP_COMMAND = ["skip", "cskip", "next", "change"]
SHUFFLE_COMMAND = ["shuffle", "cshuffle"]
LOOP_COMMAND = ["loop", "cloop"]
SEEK_COMMAND = ["seek", "cseek", "seekback", "cseekback"]
RESTART_COMMAND = ["reboot"]
ADDSUDO_COMMAND = ["addsudo", "addrandi", "randi"]
DELSUDO_COMMAND = ["delsudo", "rmsudo", "bsdk", "bhakkbsdk"]
SUDOUSERS_COMMAND = ["sudolist", "listsudo", "sudoers", "sudo"]
BROADCAST_COMMAND = ["broadcast", "gcast"]
BLACKLISTCHAT_COMMAND = ["blacklistchat", "blchat"]
WHITELISTCHAT_COMMAND = ["whitelistchat", "unblchat", "wlchat"]
BLACKLISTEDCHAT_COMMAND = ["blacklistedchat", "blchats"]
VIDEOLIMIT_COMMAND = ["set_video_limit"]
VIDEOMODE_COMMAND = ["videomode"]
MAINTENANCE_COMMAND = ["maintenance"]
LOGGER_COMMAND = ["logger"]
GETLOG_COMMAND = ["get_log", "logs", "getlog", "log"]
GETVAR_COMMAND = ["get_v", "getv", "showv"]
DELVAR_COMMAND = ["del_v", "delv"]
SETVAR_COMMAND = ["set_v", "setv", "addv"]
USAGE_COMMAND = ["usage"]
VARS_COMMAND = ["v", "c"]
UPDATE_COMMAND = ["update", "upgrade"]
REBOOT_COMMAND = ["restart"]
AUTOEND_COMMAND = ["autoend"]
AUTHORIZE_COMMAND = ["authorize"]
UNAUTHORIZE_COMMAND = ["unauthorize"]
AUTHORIZED_COMMAND = ["authorized"]
BLOCK_COMMAND = ["block"]
UNBLOCK_COMMAND = ["unblock"]
BLOCKED_COMMAND = ["blockedusers", "blocked", "blusers"]
SPEEDTEST_COMMAND = ["speedtest", "spt"]
ACTIVEVC_COMMAND = ["activevoice", "activevc"]
ACTIVEVIDEO_COMMAND = ["activevideo", "activev"]
GBAN_COMMAND = ["gban", "gandban", "gandfaadban", "globalban"]
UNGBAN_COMMAND = ["ungban", "gandback", "globalunban"]
GBANNED_COMMAND = ["gbannedusers", "gbanlist", "gbanned"]


@app.on_message(
    filters.command("PLAY_COMMAND")
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/2ff2dab0dd5953e674c79.jpg",
        caption=f"""**◈ 𝐓𝙷𝙸𝚂 𝐂𝙾𝙼𝙼𝙰𝙽𝙳 𝐔𝚂𝙴 𝐈𝙽 𝐎𝙽𝙻𝚈 𝐆𝚁𝙾𝚄𝙿𝚂 𝐁𝙰𝙱𝚈 **\n**◈ 𝐆𝙾 𝐓𝙾 𝐆𝚁𝙾𝚄𝙿𝚂/𝐀𝙳𝙳 𝐌𝙴 𝐈𝙽 𝐆𝚁𝙾𝚄𝙿𝚂 𝐀𝙽𝙳 𝐔𝚂𝙴 /play 𝐂𝙾𝙼𝙼𝙰𝙽𝙳.**\n**◈ 𝐓𝙷𝙰𝙽𝙺 𝐔𝙷 𝐁𝙰𝙱𝚈.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•─╼⃝𖠁𝐀𝙳𝙳 ◈ 𝐌𝙴 ◈ 𝐁𝙰𝙱𝚈𖠁⃝╾─•", url=f"https://t.me/{app.username}?startgroup=true")
                ]
            ]
        ),
    )
