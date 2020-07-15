from typing import List


def squared_list(int_list: List[int]) -> List[int]:
    return [i ** 2 for i in int_list]


squared_list([1, 2, 3])
