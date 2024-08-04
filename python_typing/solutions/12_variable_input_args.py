def variable_input_args(*args: str) -> str:
    return ",".join(args)


variable_input_args()
variable_input_args("a", "b", "c", "d")
