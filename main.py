import os
from dotenv import load_dotenv
import telebot
load_dotenv()
token = os.getenv('token')
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.polling()

