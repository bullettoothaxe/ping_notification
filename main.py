from ping import is_online
from bot import bot
import time


def send_notification(status: bool):
    message = 'Light!' if status else 'No Light'
    updates = bot.get_updates()

    for update in updates:
        chat_id = update.message.chat.id
        bot.send_message(chat_id, message)


def main():
    last_status = False
    while True:
        current_status = is_online()
        if current_status != last_status:
            send_notification(current_status)
            last_status = current_status
        time.sleep(30)


if __name__ == '__main__':
    main()
