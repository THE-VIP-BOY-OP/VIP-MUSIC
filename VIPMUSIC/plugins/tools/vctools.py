from pyrogram import Client, filters
from pyrogram.types import Message
from VIPMUSIC import app
from config import OWNER_ID
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# vc off
@app.on_message(filters.video_chat_ended)
async def brah2(_, msg):
       await msg.reply("**😕ᴠɪᴅᴇᴏ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ💔**")

IS_BROADCASTING = False

# vc on
@app.on_message(filters.video_chat_started)
async def broadcast_vc_start(_, msg):
    global IS_BROADCASTING
    if not IS_BROADCASTING:
        IS_BROADCASTING = True
        try:
            served_chats = await get_served_chats()
            for chat_id in served_chats:
                try:
                    await app.send_message(chat_id, "**😍ᴠɪᴅᴇᴏ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ🥳**")
                except FloodWait as fw:
                    flood_time = int(fw.value)
                    if flood_time > 200:
                        pass
                    await asyncio.sleep(flood_time)
                except Exception as e:
                    print(f"Error sending broadcast to chat {chat_id}: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            IS_BROADCASTING = False

               
# invite members on vc
@app.on_message(filters.video_chat_members_invited)
async def brah3(app: app, message: Message):
    text = f"**➻** {message.from_user.mention}\n\n**๏ ɪɴᴠɪᴛɪɴɢ ɪɴ ᴠᴄ**\n\n**➻ **"
    x = 0
    for user in message.video_chat_members_invited.users:
        try:
            text += f"[{user.first_name}](tg://user?id={user.id}) "
            x += 1
        except Exception:
            pass

    try:
        invite_link = await app.export_chat_invite_link(message.chat.id)
        add_link = f"https://t.me/{app.username}?startgroup=true"
        reply_text = f"{text} 🤭🤭"

        await message.reply(reply_text, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text= "๏ ᴊᴏɪɴ ᴠᴄ ๏", url=invite_link)],
                [InlineKeyboardButton(text= "๏ ᴀᴅᴅ ᴍᴇ ๏", url=add_link)],
            ]))
    except Exception as e:
        print(f"Error: {e}")



####

@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

###
@app.on_message(filters.command("leavegroup")& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"sᴜᴄᴄᴇssғᴜʟʟʏ   ʟᴇғᴛ  !!."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


####


@app.on_message(filters.command(["spg"], ["/", "!", "."]))
async def search(event):
    msg = await event.respond("Searching...")
    async with aiohttp.ClientSession() as session:
        start = 1
        async with session.get(f"https://content-customsearch.googleapis.com/customsearch/v1?cx=ec8db9e1f9e41e65e&q={event.text.split()[1]}&key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM&start={start}", headers={"x-referer": "https://explorer.apis.google.com"}) as r:
            response = await r.json()
            result = ""
            
            if not response.get("items"):
                return await msg.edit("No results found!")
            for item in response["items"]:
                title = item["title"]
                link = item["link"]
                if "/s" in item["link"]:
                    link = item["link"].replace("/s", "")
                elif re.search(r'\/\d', item["link"]):
                    link = re.sub(r'\/\d', "", item["link"])
                if "?" in link:
                    link = link.split("?")[0]
                if link in result:
                    # remove duplicates
                    continue
                result += f"{title}\n{link}\n\n"
            prev_and_next_btns = [Button.inline("▶️Next▶️", data=f"next {start+10} {event.text.split()[1]}")]
            await msg.edit(result, link_preview=False, buttons=prev_and_next_btns)
            await session.close()
