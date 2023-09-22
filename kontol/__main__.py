from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#from config import *
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

api_id = 9128356
api_hash = "cf219228092173e15047d3fb5a023cfc"
bot_token = "6125694353:AAH8lZhap_unS6wvYbCnBfMmXKv9M_vv_zg"

bot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@bot.on_message(filters.command(["start"]))
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋 Helo {message.from_user.first_name} \n
💭 Welcome to Magic Project Bot.\n There will be interesting things here, just wait bro.</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Repository", url=f"https://github.com/Team-Pesulap/MagicProject"),
                    InlineKeyboardButton(text="Support", url=f"https://t.me/PesulapTelegram"),
                ],
                [
                    InlineKeyboardButton(text="Deploy", url=f"https://dashboard.heroku.com/new?template=https://github.com/Team-Pesulap/MagicProject"),
                ],
		[
                     InlineKeyboardButton(text="Tutup", callback_data="cl_ad"),
                  ],
             ]
        ),
     disable_web_page_preview=True
    )

if __name__ == "__main__":
    app.run()
