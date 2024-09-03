from pyrogram import filters
from VIPMUSIC import app
from TheApi import api

# List of color combinations
color_combinations = {
    "blackpink": api.blackpink,
    "redblack": api.redblack,
    "bluegreen": api.bluegreen,
    "purpleyellow": api.purpleyellow,
    "orangeblue": api.orangeblue,
    "cyanmagenta": api.cyanmagenta,
    "greengray": api.greengray,
    "blackwhite": api.blackwhite,
    "redblue": api.redblue,
    "yellowgreen": api.yellowgreen,
    "pinkblue": api.pinkblue,
    "orangegreen": api.orangegreen,
    "purpleblack": api.purpleblack,
    "tealyellow": api.tealyellow,
    "brownorange": api.brownorange,
    "blackgold": api.blackgold,
    "redwhite": api.redwhite,
    "bluegray": api.bluegray,
    "greenyellow": api.greenyellow,
    "purplecyan": api.purplecyan
}

@app.on_message(filters.command("colours"))
async def list_colours(client, message):
    colour_list = "\n".join(color_combinations.keys())
    await message.reply_text(f"Available color combinations:\n\n{colour_list}")

@app.on_message(filters.command(list(color_combinations.keys())))
async def generate_coloured_text(client, message):
    if len(message.command) < 2:
        await message.reply_text(f"Usage: /{message.command[0]} <text>")
        return

    text = message.command[1]
    color_function = color_combinations[message.command[0]]
    photo = color_function(text)
    await message.reply_photo(photo)
