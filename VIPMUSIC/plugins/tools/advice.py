from pyrogram import filters

from VIPMUSIC import api, app


async def get_advice():
    b = await api.advice()
    c = b["advice"]
    return c


@app.on_message(filters.command("advice"))
async def clean(_, message):
    A = await message.reply_text("...")
    B = await get_advice()
    await A.edit(B)


__MODULE__ = "Advice"
__HELP__ = """
## Advice Command

### Command: /advice
**Description:**
Fetches a random piece of advice from an API and displays it.
**Usage:**
/advice

**Details:**
- Sends a random piece of advice as a message in the chat.

**Examples:**
- /advice: Retrieves and displays advice.

**Notes:**
- This command can be used by any user to get a random advice.
"""
