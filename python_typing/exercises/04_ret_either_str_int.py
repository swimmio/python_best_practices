# Fix the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html

import random


def ret_either_str_int() -> str:
    if random.random() > 0.5:
        return "Swimm"
    return 42
