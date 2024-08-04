import random
from typing import Union


def ret_either_str_int() -> Union[str, int]:
    if random.random() > 0.5:
        return "Swimm"
    return 42
