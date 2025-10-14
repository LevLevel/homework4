def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


RESULT1 = is_palindrome(121)
print(f"121 -> {RESULT1}")
assert RESULT1

RESULT2 = is_palindrome(-121)
print(f"-121 -> {RESULT2}")
assert not RESULT2

RESULT3 = is_palindrome(10)
print(f"10 -> {RESULT3}")
assert not RESULT3

RESULT4 = is_palindrome(0)
print(f"0 -> {RESULT4}")
assert RESULT4

RESULT5 = is_palindrome(100)
print(f"100 -> {RESULT5}")
assert RESULT5
