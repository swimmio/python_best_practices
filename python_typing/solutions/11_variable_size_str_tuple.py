from typing import Tuple


def variable_size_str_tuple(tup: Tuple[str, ...]) -> str:
    return ",".join(tup)


variable_size_str_tuple(tuple())
variable_size_str_tuple(("a", "b"))
