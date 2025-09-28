from functools import reduce


def typed(type_):
    def decorator(func):
        def wrapper(*args):
            converted_args = [type_(arg) for arg in args]
            return func(*converted_args)

        return wrapper

    return decorator


@typed(type_=str)
def add_str(*args):
    return "".join(str(arg) for arg in args)


@typed(type_=int)
def add_int(*args):
    return sum(args)


@typed(type_=float)
def add_float(*args):
    return reduce(lambda x, y: x + y, args, 0.0)
