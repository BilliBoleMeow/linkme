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
        text="""
A Simple Telegram File To Link Generation Bot.\n""",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('LiquidX Projects', url=f"https://t.me/liquidxprojects")] ]  ))
