def sum_numbers(n):
    result = 0
    for i in range(1, n + 1):
        result += n
    print(f"Sum to {n} = {result}")
    return result


assert sum_numbers(1) == 1
assert sum_numbers(2) == 3
assert sum_numbers(8) == 36
assert sum_numbers(22) == 253
assert sum_numbers(100) == 5050
