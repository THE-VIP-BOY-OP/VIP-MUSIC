from AnonX import app
from pyrogram import filters


@app.on_message(filters.command('gali'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"{reply.from_user.mention} **😡MADHERRRCHODDD😡** "
        )
    else:
        message.reply(
            f"**🍁REPLY ANY PERSON MESSAGE🍁**"
        )
