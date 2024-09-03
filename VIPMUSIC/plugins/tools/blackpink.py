from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters

# Initialize Pyrogram Client
from VIPMUSIC import app

# Load the background image
background_path = (
    "https://telegra.ph/file/b28ef4f44c081700ee2e9.jpg"  # Adjust the path if needed
)
font_path = "assets/font.ttf"  # Specify the path to your font file


@app.on_message(filters.command("blackpink"))
def blackpink(client, message):
    if len(message.command) < 2:
        message.reply("Please provide a name after the command.")
        return

    # Extract the name from the command
    text = message.command[1].upper()

    # Open the background image
    img = Image.open(background_path)

    # Draw on the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 100)

    # Calculate the position for the text to be centered
    text_width, text_height = draw.textsize(text, font=font)
    image_width, image_height = img.size
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    # Draw the text on the image
    draw.text((x, y), text, fill=(255, 105, 180), font=font)  # Pink color

    # Optionally, draw a border around the text
    border_width = 10
    draw.rectangle(
        [
            x - border_width,
            y - border_width,
            x + text_width + border_width,
            y + text_height + border_width,
        ],
        outline=(255, 105, 180),
        width=5,
    )

    # Save the edited image
    output_path = f"/mnt/data/{text}.png"
    img.save(output_path)

    # Send the edited image
    message.reply_photo(photo=output_path)
