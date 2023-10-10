python
from pyrogram import Client, filters
from VipX import app
# Create a new instance of the Client
app = Client("my_bot")

# Create a filter to handle new member join events
@app.on_message(filters.new_chat_members)
async def welcome_new_members(client, message):
    chat_id = message.chat.id
    new_members = message.new_chat_members
    for member in new_members:
        await client.send_message(chat_id=chat_id, text=f"Welcome {member.first_name}!")

# Run the bot
with app:
    app.run()
