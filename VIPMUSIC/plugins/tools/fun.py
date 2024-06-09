from pyrogram import filters
from pyrogram.types import Message

from VIPMUSIC import app


@app.on_message(filters.command(["dice", "ludo"]))
async def dice(c, m: Message):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
    await dicen.reply_text("results is {0}".format(dicen.dice.value))


__MODULE__ = "Fun"
__HELP__ = """
## Fun Commands Help

### 1. /dice or /ludo
**Description:**
Rolls a virtual dice or plays a game of Ludo.

**Usage:**
/dice or /ludo

**Details:**
- Initiates a dice roll or a game of Ludo.
- Sends the result of the dice roll.
- For Ludo, the game is played directly in the chat.

**Examples:**
- `/dice`
- `/ludo`

"""
