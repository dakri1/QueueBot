import os
from dotenv import load_dotenv
import telebot
from telebot import types
from database import DB

load_dotenv()
token = os.getenv('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    db = DB()
    flag = db.get_user(message.chat.id)
    if flag:
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(callback_data="laba1", text="Laba 1")
        btn2 = types.InlineKeyboardButton(callback_data="laba2", text="Laba 2")
        kb.add(btn1, btn2)
    else:
        kb = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(callback_data="set_name", text="Register")
        kb.add(btn)
    bot.send_message(message.chat.id, "Привет ✌️ ", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def call_handler(call):
    if call.data == "set_name":
        msg = bot.send_message(call.message.chat.id, "Send me your name")
        bot.register_next_step_handler(msg, set_name)
    if call.data == "laba1":
        db = DB()
        db.add_to_laba(user_id=call.message.chat.id, laba="laba1")
    if call.data == "laba2":
        db = DB()
        db.add_to_laba(user_id=call.message.chat.id, laba="laba2")



def set_name(message):
    try:
        db = DB()
        db.add_user(message.chat.id, message.text)
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(callback_data="laba1", text="Laba 1")
        btn2 = types.InlineKeyboardButton(callback_data="laba2", text="Laba 2")
        kb.add(btn1, btn2)
        bot.send_message(message.chat.id, "Success", reply_markup=kb)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "You have already registered")


bot.polling()
