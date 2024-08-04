from typing import TypeVar

T = TypeVar("T", int, str)


def add_int_str(a: T, b: T) -> T:
    return a + b


assert add_int_str(1, 1) == 2
assert add_int_str("Swimm ", "is awesome") == "Swimm is awesome"
