# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html


def ret_type_alias():
    """
    return a type alias for the code
    """
    if random.random() > 0.5:
        return {"s": ["1", "2", "3"]}
    return "s"
