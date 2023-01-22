from telebot.async_telebot import AsyncTeleBot
from env import BOT_TOKEN
import users

bot = AsyncTeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
async def start_handler(message):
    chat_id = message.chat.id
    users.add_user(chat_id)
    await bot.send_message(chat_id, 'Welcome to the light notifier bot 🔔')


@bot.message_handler(commands=['users_anal'])
async def users_anal_handler(message):
    chat_id = message.chat.id
    active_users = users.read()
    message = f"Users count: {len(active_users)}"
    await bot.send_message(chat_id, message)
