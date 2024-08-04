from typing import TypedDict, List, Optional, Any


class MySpecialDict(TypedDict):
    str_field: str
    int_field: int
    float_field: float
    list_field: List[Any]
    optional_str_field: Optional[str]


def ret_typed_dict() -> MySpecialDict:
    return {
        "str_field": "str",
        "int_field": 0,
        "float_field": 0.0,
        "list_field": [1, 2, 3],
        "optional_str_field": None
    }


_: MySpecialDict = ret_typed_dict()
