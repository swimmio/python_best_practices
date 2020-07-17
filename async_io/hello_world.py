import asyncio


async def print_hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def print_hello_world_three_times():
    await asyncio.gather(print_hello_world(), print_hello_world(), print_hello_world())


def swimm_unit():
    """
    >>> swimm_unit()
    Hello
    Hello
    Hello
    World
    World
    World
    """
    asyncio.run(print_hello_world_three_times())

