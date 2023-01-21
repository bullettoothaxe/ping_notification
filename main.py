from ping import is_host_up
from bot import bot
import users
import asyncio

has_light_message = "💡😺💡"
no_light_message = "🕯️🙅‍♀️🕯️"


def uniq(items):
    return list(set(items))


def get_subscribers(from_updates):
    saved_users = users.read()
    next_users = saved_users.copy()

    for user in from_updates:
        if user not in next_users:
            next_users.append(user)

    if len(saved_users) != len(next_users):
        users.update(next_users)

    return next_users


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
            next_users = chat_ids.copy()
            next_users.remove(chat_id)
            users.update(next_users)


async def main():
    last_status = True
    while True:
        current_status = is_host_up()
        if current_status != last_status:
            send_notification(current_status)
            last_status = current_status
        await asyncio.sleep(30)


if __name__ == '__main__':
    bot.infinity_polling()
    print('Started')
    asyncio.run(main())
