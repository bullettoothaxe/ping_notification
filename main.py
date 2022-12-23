from ping import is_host_up
from bot import bot
import time


def send_notification(status: bool):
    message = 'Light!' if status else 'No Light'
    updates = bot.get_updates()
    chat_ids = list(set([update.message.chat.id for update in updates]))
    print(chat_ids)

    for chat_id in chat_ids:
        bot.send_message(chat_id, message)


def main():
    last_status = False
    while True:
        current_status = is_host_up()
        if current_status != last_status:
            send_notification(current_status)
            last_status = current_status
        time.sleep(30)


if __name__ == '__main__':
    main()
