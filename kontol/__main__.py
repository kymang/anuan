from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *

api_id = 9128356
api_hash = "cf219228092173e15047d3fb5a023cfc"
bot_token = "6125694353:AAH8lZhap_unS6wvYbCnBfMmXKv9M_vv_zg"

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)



@app.on_message()
def start_command(client, message):
    if message.text == "/start":
        # Membuat tombol-tombol untuk inline keyboard
        button1 = InlineKeyboardButton("Lihat Produk", callback_data="view_products")
        button2 = InlineKeyboardButton("Keranjang Belanja", callback_data="view_cart")
        button3 = InlineKeyboardButton("Selesai Belanja", callback_data="checkout")

        # Membuat markup inline keyboard
        inline_markup = InlineKeyboardMarkup(
            [[button1], [button2], [button3]]
        )

        # Mengirim pesan dengan inline keyboard
        message.reply_text("Selamat datang di Telegram Shop. Silakan pilih tindakan di bawah ini:", reply_markup=inline_markup)


@app.on_callback_query()
def handle_callback(client, query):
    if query.data == "view_products":
        # Tanggapan untuk tombol "Lihat Produk"
        client.answer_callback_query(query.id, text="Anda akan melihat produk.")
    elif query.data == "view_cart":
        # Tanggapan untuk tombol "Keranjang Belanja"
        client.answer_callback_query(query.id, text="Anda akan melihat keranjang belanja.")
    elif query.data == "checkout":
        # Tanggapan untuk tombol "Selesai Belanja"
        client.answer_callback_query(query.id, text="Anda akan menyelesaikan belanja.")

if __name__ == "__main__":
    app.run()
