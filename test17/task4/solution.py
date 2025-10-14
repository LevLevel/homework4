def plus_one(number):
    digits = [int(digit) for digit in str(number)]

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits


result1 = plus_one(9)
print(f"9 -> {result1}")
assert result1 == [1, 0]

result2 = plus_one(123)
print(f"123 -> {result2}")
assert result2 == [1, 2, 4]

result3 = plus_one(119)
print(f"119 -> {result3}")
assert result3 == [1, 2, 0]

result4 = plus_one(999)
print(f"999 -> {result4}")
assert result4 == [1, 0, 0, 0]
