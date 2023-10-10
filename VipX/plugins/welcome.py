python
from pyrogram import Client, filters
from VipX import app
# Create a new instance of the Client

# Create a filter to handle new member join events
@app.on_message(filters.new_chat_members)
def welcome_new_members(_, message):

    new_members = message.new_chat_members
    for member in new_members:
        app.send_message(message.chat.id, text=f"Welcome {member.first_name}!")

# Run the bot
app.run()
