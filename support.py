import aioschedule as schedule
import asyncio
from bot import bot
import users
from env import SUPPORT_MESSAGE


async def send_support_message():
    chat_ids = users.read().copy()

    for chat_id in chat_ids:
        try:
            await bot.send_message(chat_id, SUPPORT_MESSAGE, parse_mode='HTML', disable_web_page_preview=True)
        except:
            print(f'Support message failed for {chat_id}')


async def run_support_scheduler():
    schedule.every().friday.at("16:05").do(send_support_message)
    # schedule.every(5).seconds.do(send_support_message)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(20)
