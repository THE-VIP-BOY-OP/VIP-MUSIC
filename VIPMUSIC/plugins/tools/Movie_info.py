from pyrogram import Client, filters
import requests
from VIPMUSIC import app
from time import time
import asyncio
from VIPMUSIC.utils.extraction import extract_user

# Define a dictionary to track the last message timestamp for each user
user_last_message_time = {}
user_command_count = {}
# Define the threshold for command spamming (e.g., 20 commands within 60 seconds)
SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5


TMDB_API_KEY = "23c3b139c6d59ebb608fe6d5b974d888"


@app.on_message(filters.command("movie"))
async def movie_command(client, message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(f"**{message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**")
            await asyncio.sleep(3)
            await hu.delete()
            return 
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    try:
        # Check if the user provided a movie name after the /movie command
        if len(message.command) > 1:
            movie_name = " ".join(message.command[1:])

            # Fetch movie information from TMDb API
            movie_info = get_movie_info(movie_name)

            # Send the movie information as a reply
            await message.reply_text(movie_info)
        else:
            await message.reply_text("Please enter a movie name after the /movie command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

def get_movie_info(movie_name):
    tmdb_api_url = f"https://api.themoviedb.org/3/search/movie"
    params = {"api_key": TMDB_API_KEY, "query": movie_name}
    
    response = requests.get(tmdb_api_url, params=params)
    data = response.json()

    if data.get("results"):
        # Get information about the first movie in the results
        movie = data["results"][0]
        
        # Fetch additional details using the movie ID
        details_url = f"https://api.themoviedb.org/3/movie/{movie['id']}"
        details_params = {"api_key": TMDB_API_KEY}
        details_response = requests.get(details_url, params=details_params)
        details_data = details_response.json()
        
        # Extract relevant information
        title = details_data.get("title", "N/A")
        release_date = details_data.get("release_date", "N/A")
        overview = details_data.get("overview", "N/A")
        providers = details_data.get("providers", "N/A")
        vote_average = details_data.get("vote_average", "N/A")
        
        # Extract actor names
        cast_url = f"https://api.themoviedb.org/3/movie/{movie['id']}/credits"
        cast_params = {"api_key": TMDB_API_KEY}
        cast_response = requests.get(cast_url, params=cast_params)
        cast_data = cast_response.json()
        actors = ", ".join([actor["name"] for actor in cast_data.get("cast", [])])
        
        # Extract total collection
        revenue = details_data.get("revenue", "N/A")
        
        # Format and return movie information
        info = (
            f"Title: {title}\n\n"
            f"Release Date: {release_date}\n\n"
            f"Overview: {overview}\n\n"
            f"Vote Average: {vote_average}\n\n"
            f"Actor Names: {actors}\n\n"
            f"Total Collection: {revenue}\n\n"
            f"Available Platforms: {providers}\n"
        )
        return info
    else:
        return "Movie not found or API request failed."
