# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        text="A Simple Telegram File To Link Generation Bot."
             (reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('LiquidX', url=f"https://t.me/liquidxprojects"))
 )
