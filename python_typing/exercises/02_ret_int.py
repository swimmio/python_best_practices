# Fix the type annotation
# Test that  `mypy --strict <filename>` passes!
# Reference:
# https://mypy.readthedocs.io/en/stable/builtin_types.html

def ret_int() -> str:
    return 42
