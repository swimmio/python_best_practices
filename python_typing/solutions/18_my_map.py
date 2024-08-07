from typing import Iterable, Callable, List


def cb(a: int) -> int:
    return a


def my_map(it: Iterable[int], cb: Callable[[int], int]) -> List[int]:
    ret = []
    for i in it:
        ret.append(cb(i))
    return ret


my_map(range(4), cb)
my_map([1, 2, 3], cb)
my_map({1, 2, 3}, cb)
