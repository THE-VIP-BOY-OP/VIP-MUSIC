import os
import aiofiles
import aiohttp
from youtubesearchpython import VideosSearch

async def get_thumb(videoid):
    # Check if thumbnail already exists
    if os.path.isfile(f"cache/{videoid}.png"):
        return f"cache/{videoid}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    
    try:
        # Fetch video details including thumbnail URL
        videosSearch = VideosSearch(url, limit = 1)
        result = await videosSearch.next()
        thumbnails = result['result'][0]['thumbnails']
        
        # Choose the highest resolution thumbnail available
        thumbnail_url = thumbnails[-1]['url']
        
        # Download and save the thumbnail
        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail_url) as resp:
                if resp.status == 200:
                    image_data = await resp.read()
                    with open(f"cache/{videoid}.png", "wb") as f:
                        f.write(image_data)
                    return f"cache/{videoid}.png"
                else:
                    print(f"Failed to fetch thumbnail. Status code: {resp.status}")
                    return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
