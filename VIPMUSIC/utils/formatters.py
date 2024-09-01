#
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, < https://github.com/THE-VIP-BOY-OP >.
#
# This file is part of < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC > project,
# and is released under the MIT License.
# Please see < https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE >
#
# All rights reserved.
import json
import os
import subprocess
import threading

import requests


def download_chunk(url, start, end, filename, session):
    headers = {"Range": f"bytes={start}-{end}"}
    response = session.get(url, headers=headers, stream=True)
    with open(filename, "ab") as f:
        for chunk in response.iter_content(1024 * 1024):
            f.write(chunk)


def download_file(vidid, audio=True, num_threads=10):
    link = "https://api.cobalt.tools/api/json"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if audio:
        data = {
            "url": "https://www.youtube.com/watch?v=LLF3GMfNEYU",
            "isAudioOnly": "True",
            "aFormat": "opus",
        }
    else:
        data = {"url": "https://www.youtube.com/watch?v=LLF3GMfNEYU", "vQuality": "240"}
    url = requests.post(link, headers=headers, json=data).json()["url"]
    session = requests.Session()
    response = session.head(url)
    if audio:
        filename = os.path.join("downloads", f"{vidid}.mp3")
    else:
        filename = os.path.join("downloads", f"{vidid}.mp4")

    total_size = response.headers.get("Content-Length")
    if total_size is None:
        if audio:
            total_size = 1024 * 1024 * 50
        else:
            total_size = 1024 * 1024 * 100
    else:
        total_size = int(total_size)

    total_size = int(total_size)
    chunk_size = total_size // num_threads
    open(filename, "wb").close()

    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size - 1
        if i == num_threads - 1:
            end = total_size - 1
        t = threading.Thread(
            target=download_chunk, args=(url, start, end, filename, session)
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return filename


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


def convert_bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])


async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


def seconds_to_min(seconds):
    if seconds is not None:
        seconds = int(seconds)
        d, h, m, s = (
            seconds // (3600 * 24),
            seconds // 3600 % 24,
            seconds % 3600 // 60,
            seconds % 3600 % 60,
        )
        if d > 0:
            return "{:02d}:{:02d}:{:02d}:{:02d}".format(d, h, m, s)
        elif h > 0:
            return "{:02d}:{:02d}:{:02d}".format(h, m, s)
        elif m > 0:
            return "{:02d}:{:02d}".format(m, s)
        elif s > 0:
            return "00:{:02d}".format(s)
    return "-"


def speed_converter(seconds, speed):
    if str(speed) == str("0.5"):
        seconds = seconds * 2
    if str(speed) == str("0.75"):
        seconds = seconds + ((50 * seconds) // 100)
    if str(speed) == str("1.5"):
        seconds = seconds - ((25 * seconds) // 100)
    if str(speed) == str("2.0"):
        seconds = seconds - ((50 * seconds) // 100)
    collect = seconds
    if seconds is not None:
        seconds = int(seconds)
        d, h, m, s = (
            seconds // (3600 * 24),
            seconds // 3600 % 24,
            seconds % 3600 // 60,
            seconds % 3600 % 60,
        )
        if d > 0:
            convert = "{:02d}:{:02d}:{:02d}:{:02d}".format(d, h, m, s)
            return convert, collect
        elif h > 0:
            convert = "{:02d}:{:02d}:{:02d}".format(h, m, s)
            return convert, collect
        elif m > 0:
            convert = "{:02d}:{:02d}".format(m, s)
            return convert, collect
        elif s > 0:
            convert = "00:{:02d}".format(s)
            return convert, collect
    return "-"


def check_duration(file_path):
    command = [
        "ffprobe",
        "-loglevel",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        file_path,
    ]

    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = pipe.communicate()
    _json = json.loads(out)

    if "format" in _json:
        if "duration" in _json["format"]:
            return float(_json["format"]["duration"])

    if "streams" in _json:
        for s in _json["streams"]:
            if "duration" in s:
                return float(s["duration"])

    return "Unknown"


formats = [
    "webm",
    "mkv",
    "flv",
    "vob",
    "ogv",
    "ogg",
    "rrc",
    "gifv",
    "mng",
    "mov",
    "avi",
    "qt",
    "wmv",
    "yuv",
    "rm",
    "asf",
    "amv",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m4v",
    "svi",
    "3gp",
    "3g2",
    "mxf",
    "roq",
    "nsv",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
]
