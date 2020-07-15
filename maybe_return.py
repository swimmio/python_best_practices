import random
from typing import Optional


def maybe_return() -> Optional[int]:
    if random.random() > 0.5:
        return None
    return 7
