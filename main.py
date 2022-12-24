from ping import is_host_up
from bot import bot
import time

has_light_message = "💡😺💡"
no_light_message = "🕯️🙅‍♀️🕯️"

users = []


def uniq(items):
    return list(set(items))


def get_subscribers(from_updates):
    global users

    for user in from_updates:
        if user not in users:
            users.append(user)

    return users


def send_notification(status: bool):
    message = has_light_message if status else no_light_message
    updates = bot.get_updates()

    from_updates = []

    for update in updates:
        if update.message is not None:
            from_updates.append(update.message.chat.id)

    chat_ids = get_subscribers(from_updates)
    print(chat_ids)

    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id, message)
        except:
            users.remove(chat_id)


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
