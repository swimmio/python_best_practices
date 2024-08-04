import random
from typing import Union, Dict, List

TypeAlias = Union[str, Dict[str, List[str]]]


def ret_type_alias() -> TypeAlias:
    """
    return a type alias for the code
    """
    if random.random() > 0.5:
        return {"s": ["1", "2", "3"]}
    return "s"
