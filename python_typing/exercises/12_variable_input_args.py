# Add the type annotation
# Test that  `mypy --strict <filename>` passes!
# References:
# https://mypy.readthedocs.io/en/stable/builtin_types.html
# https://mypy.readthedocs.io/en/stable/type_inference_and_annotations.html
# https://mypy.readthedocs.io/en/stable/kinds_of_types.html

def variable_input_args(*args):
    return ",".join(args)


variable_input_args()
variable_input_args("a", "b", "c", "d")
