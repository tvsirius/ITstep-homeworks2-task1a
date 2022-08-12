from countdown import async_countdown,async_show_info_infinitly
import asyncio


async def main():
    t1 = asyncio.create_task(async_countdown(5,True))
    t2 = asyncio.create_task(async_countdown(15,True))
    t3 = asyncio.create_task(async_countdown(2,True))
    t4 = asyncio.create_task(async_countdown(3,True))
    t5 = asyncio.create_task(async_countdown(11,True))
    t99= asyncio.create_task(async_show_info_infinitly(1))

    await t1
    await t2
    await t3
    await t4
    await t5
    # await t99

loop = asyncio.get_event_loop()

loop.run_until_complete(main())

