import asyncio
from pytgcalls import idle
from VCRAID import call_py, bot
from config import SUPPORT_GROUP

async def main():
    await call_py.start()
    await bot.join_chat("TG_FRIENDSS")
    await bot.join_chat("VIP_CREATORS")
    await bot.send_message(
            SUPPORT_GROUP,
            "<b>VCRAID UserBot Successfully Deployed And Started!</b>")
    print(
        """
    ------------------
   | Userbot Started! POWERED BY @THE_VIP_BOY |
    ------------------
"""
    )
    await idle()   

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
