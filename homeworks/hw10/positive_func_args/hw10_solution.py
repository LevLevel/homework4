def validate_arguments(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"{arg} is not a positive")
        return func(*args, **kwargs)

    return wrapper


@validate_arguments
def sum_positive(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
