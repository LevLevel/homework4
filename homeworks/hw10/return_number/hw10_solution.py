def validate_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError("Arguments should be a number")
        return result

    return wrapper


@validate_return_type
def concat_str(*args, **kwargs):
    return "".join(str(arg) for arg in args) + "".join(str(val) for val in kwargs.values())


@validate_return_type
def arguments_summary(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
