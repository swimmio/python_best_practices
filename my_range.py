from typing import Generator


def my_range(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end):
        yield i


my_range(1, 4)
