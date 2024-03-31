from youtubesearchpython import VideosSearch

async def get_thumb(videoid):
    query = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(query, limit=1)
        for result in (await results.next())["result"]:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        return thumbnail
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
