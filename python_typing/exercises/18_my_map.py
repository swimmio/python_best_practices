# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


def cb(a: int) -> int:
    return a


def my_map(it, cb):
    ret = []
    for i in it:
        ret.append(cb(i))
    return ret


my_map(range(4), cb)
my_map([1, 2, 3], cb)
my_map({1, 2, 3}, cb)
