def string_funk(s, n):
    if n <= 0:
        return ""

    first_part = s[:n]
    second_part = first_part[-2::-1]

    return first_part + second_part


alphabet = "abcdefghijklmnopqrstuvwxyz"

result1 = string_funk(alphabet, 1)
print(f"f(s, 1) => '{result1}'")
assert result1 == "a"

result2 = string_funk(alphabet, 2)
print(f"f(s, 2) => '{result2}'")
assert result2 == "aba"

result3 = string_funk(alphabet, 3)
print(f"f(s, 3) => '{result3}'")
assert result3 == "abcba"

result4 = string_funk(alphabet, 4)
print(f"f(s, 4) => '{result4}'")
assert result4 == "abcdcba"
