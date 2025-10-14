def string_funk(s, n):
    if n <= 0:
        return ""

    first_part = s[:n]
    second_part = first_part[-2::-1]

    return first_part + second_part


ALPHABET = "abcdefghijklmnopqrstuvwxyz"

RESULT1 = string_funk(ALPHABET, 1)
print(f"f(s, 1) => '{RESULT1}'")
assert RESULT1 == "a"

RESULT2 = string_funk(ALPHABET, 2)
print(f"f(s, 2) => '{RESULT2}'")
assert RESULT2 == "aba"

RESULT3 = string_funk(ALPHABET, 3)
print(f"f(s, 3) => '{RESULT3}'")
assert RESULT3 == "abcba"

RESULT4 = string_funk(ALPHABET, 4)
print(f"f(s, 4) => '{RESULT4}'")
assert RESULT4 == "abcdcba"
