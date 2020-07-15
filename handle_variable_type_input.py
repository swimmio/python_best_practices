from typing import Union


def handle_variable_type_input(str_int: Union[str, int]) -> int:
    """
    This function returns 5 if the input is of type string
    otherwise it returns the value.
    """
    if isinstance(str_int, str):
        return 5
    else:
        return str_int
