# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        text="(<a href='https://telegram.dog/liquidxprojects'> LiquidX Projects </a>)\n),
         quote=True,
         parse_mode=ParseMode.HTML"
 )
