def square_number(number):
    result = number ** 2
    print(f"Sqare is {number} = {result}")
    return result


def even_or_odd(number):
    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"
    print(f"Number {number} is {result}")
    return result


assert square_number(5) == 25
assert square_number(0) == 0
assert square_number(-4) == 16

assert even_or_odd(10) == "even"
assert even_or_odd(-3) == "odd"
assert even_or_odd(7) == "odd"
