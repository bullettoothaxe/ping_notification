from bot import bot
import asyncio
from support import run_support_scheduler
from notification import connectivity_notification_loop


async def main():
    tasks = [
        connectivity_notification_loop(),
        bot.infinity_polling(),
        # run_support_scheduler(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
