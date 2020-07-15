from typing import Iterable


def sum_members(members: Iterable[int]) -> int:
    sm = 0
    for mem in members:
        sm += mem
    return sm


sum_members([1, 2, 3])
sum_members((1, 2, 3))
sum_members({1, 2, 3})
sum_members({1: 1, 2: 2, 3: 3})
sum_members(range(1, 4))
