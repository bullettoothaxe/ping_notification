import telebot
from env import BOT_TOKEN
import users

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['users_anal'])
def schedule_handler(message):
    chat_id = message.chat.id
    active_users = users.read()
    message = f"Users count: {len(active_users)}"
    bot.send_message(chat_id, message)
