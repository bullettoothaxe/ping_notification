import telebot
from env import BOT_TOKEN
import users

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['users_anal'])
def users_anal_handler(message):
    chat_id = message.chat.id
    active_users = users.read()
    message = f"Users count: {len(active_users)}"
    bot.send_message(chat_id, message)


@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    users.add_user(chat_id)
