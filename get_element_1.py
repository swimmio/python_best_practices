from typing import (Sequence, Optional)


def get_element_1(members: Sequence[int]) -> Optional[int]:
    if len(members) < 2:
        return None
    return members[1]


get_element_1([1, 2, 3])
get_element_1((1, 2, 3))
