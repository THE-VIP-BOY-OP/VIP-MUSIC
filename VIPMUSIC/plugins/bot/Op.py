#Callback Query

DOCS_MESSAGE = "Let's start reading the docs"

DOCS_BUTTONS = [

[

InlineKeyboardButton('START READING', callback_data="START READING")

)

]

@bot.on_message(filters.command("doc") & filters.private)

def doc(bot, message):

message.reply(

text = DOCS MESSAGE,

reply_markup = InlineKeyboardMarkup(DOCS_BUTTONS)

@bot.on_callback_query()

def callback_query(Client, CallbackQuery):

if CallbackQuery.data == "START READING":

PAGE1 TEXT = "This is

I

CallbackQuery.edit_message_text(
