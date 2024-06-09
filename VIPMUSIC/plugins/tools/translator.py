__MODULE__ = "Translator"
__HELP__ = """
This module provides commands to translate messages.

- `/tr [language_code]`: Translate a message. Reply to the message you want to translate. Optionally, specify the target language code. If not specified, the target language will be English (en).
- `/langcodes`: Get a list of language codes and their corresponding languages.
"""

from gpytranslate import Translator
from pyrogram import filters

from VIPMUSIC import app

trans = Translator()


@app.on_message(filters.command("tr"))
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("Please reply to a message to translate it!")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = f"Translated from {source} to {dest}:\n{translation.text}"
    await message.reply_text(reply)


@app.on_message(filters.command("langcodes"))
async def language_codes(_, message):
    languages = """
    Language Codes:
    en - English
    es - Spanish
    fr - French
    de - German
    it - Italian
    pt - Portuguese
    ru - Russian
    zh - Chinese
    ar - Arabic
    ja - Japanese
    ko - Korean
    hi - Hindi
    """
    await message.reply_text(languages)
