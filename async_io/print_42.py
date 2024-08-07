import asyncio


async def return_42():
    return 42


async def print_42():
    print(await return_42())


def runner():
    """
    >>> runner()
    42
    """
    asyncio.run(print_42())
