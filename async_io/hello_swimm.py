import asyncio


async def hello_swimm():
    print("hello")
    await asyncio.sleep(1)
    print("swimm")


def runner():
    """
    >>> runner()
    hello
    swimm
    """
    asyncio.run(hello_swimm())
