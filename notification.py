import asyncio

from bot import bot
import users
from ping import is_host_up

has_light_message = "💡😺💡"
no_light_message = "🕯️🙅‍♀️🕯️"


async def send_notification(status: bool):
    message = has_light_message if status else no_light_message
    chat_ids = users.read().copy()
    print(chat_ids)

    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id, message)
        except:
            users.remove_user(chat_id)


async def connectivity_notification_loop():
    print('Started connectivity notification loop')
    last_status = is_host_up()
    while True:
        current_status = is_host_up()
        if current_status != last_status:
            await send_notification(current_status)
            last_status = current_status
        await asyncio.sleep(30)
