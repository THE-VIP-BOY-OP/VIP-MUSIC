import os
import re
import random

import aiofiles
import aiohttp

from PIL import Image, ImageDraw, ImageEnhance
from PIL import ImageFilter, ImageFont, ImageOps

from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from VIPMUSIC import app
from config import YOUTUBE_IMG_URL


async def get_thumb(videoid):
    try:
        query = f"https://www.youtube.com/watch?v={videoid}"
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            title = result["title"]
            duration = result["duration"]
            views = result["viewCount"]["short"]
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            channellink = result["channel"]["link"]
            channel = result["channel"]["name"]
            link = result["link"]
            published = result["publishedTime"]
    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
