def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]


result1 = is_palindrome(121)
print(f"121 -> {result1}")
assert result1 == True

result2 = is_palindrome(-121)
print(f"-121 -> {result2}")
assert result2 == False

result3 = is_palindrome(10)
print(f"10 -> {result3}")
assert result3 == False

result4 = is_palindrome(0)
print(f"0 -> {result4}")
assert result4 == True

result5 = is_palindrome(100)
print(f"100 -> {result5}")
assert result5 == False