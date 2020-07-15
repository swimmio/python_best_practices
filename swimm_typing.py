from typing import (
    Union,
    TypeVar,
    List,
    Tuple,
    Optional,
    Sequence,
    Iterable,
    Generator,
    Dict,
    Set,
    Callable, Mapping, TypedDict,
)


def handle_variable_type_input(str_int: Union[str, int]) -> int:
    """
    This function returns 5 if the input is of type string
    otherwise it returns the value.
    """
    if isinstance(str_int, str):
        return 5
    else:
        return str_int


def multiple_ret() -> Tuple[str, int]:
    return "Swimm", 2


def maybe_return() -> Optional[int]:
    if random.random() > 0.5:
        return None
    return 7


T = TypeVar("T", int, str)


def add_int_str(a: T, b: T) -> T:
    return a + b


assert add_int_str(1, 1) == 2
assert add_int_str("Swimm ", "is awesome") == "Swimm is awesome"


def multiply_str(s: str, count: int) -> str:
    return s * count


assert multiply_str("s", 1) == "s"


def squared_list(int_list: List[int]) -> List[int]:
    return [i ** 2 for i in int_list]


squared_list([1, 2, 3])


def variable_size_str_tuple(tup: Tuple[str, ...]) -> str:
    return ",".join(tup)


variable_size_str_tuple(tuple())
variable_size_str_tuple(("a", "b"))


def variable_input_args(*args: str) -> str:
    return ",".join(args)


variable_input_args()
variable_input_args("a", "b", "c", "d")


def get_element_1(members: Sequence[int]) -> Optional[int]:
    if len(members) < 2:
        return None
    return members[1]


get_element_1([1, 2, 3])
get_element_1((1, 2, 3))


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


def my_range(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end):
        yield i


my_range(1, 4)


def get_dict_str_str(d: Dict[str, str]) -> None:
    pass  # The implementation doesn't matter here


get_dict_str_str({"a": "b"})
get_dict_str_str({})


def get_dict_str_int(d: Dict[str, int]) -> None:
    pass  # The implementation doesn't matter here


get_dict_str_int({"a": 1})
get_dict_str_int({})


def get_set_int(s: Set[int]) -> None:
    pass  # The implementation doesn't matter here


get_set_int({1, 2, 3, 4})
get_set_int(set([1, 2, 3, 4]))


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


class A:
    pass  # The implementation doesn't matter here


class B:
    def f(self, a: A) -> None:
        pass  # The implementation doesn't matter here


my_a = A()
my_b = B()
my_b.f(my_a)


def read_only_dictionary(d: Mapping[str, int]) -> None:
    pass  # The implementation doesn't matter here


read_only_dictionary(d={"a": 1})


class D:
    def __init__(self, c: "C") -> None:
        pass  # The implementation doesn't matter here


class C:
    pass  # The implementation doesn't matter here


my_c = C()
my_d = D(my_c)


class MySpecialDict(TypedDict):
    str_field: str
    int_field: int
    float_field: float
    list_field: List[int]
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

TypeAlias = Union[str, Dict[str, List[str]]]


def ret_type_alias() -> TypeAlias:
    """
    return a type alias for the code
    """
    if random.random() > 0.5:
        return {"s": ["1", "2", "3"]}
    return "s"
