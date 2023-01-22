import asyncio


async def one():
    while True:
        print("one")
        await asyncio.sleep(1)


async def two():
    while True:
        print("two")
        await asyncio.sleep(2)


async def main():
    await asyncio.gather(one(), two())


asyncio.run(main())
