A = "Skoda, simply clever"

FIRST_CHAR = A[0]
assert FIRST_CHAR == "S"
print(f"First char: '{FIRST_CHAR}'")

LAST_CHAR = A[-1]
assert LAST_CHAR == "r"
print(f"Last char: '{LAST_CHAR}'")

THIRD_CHAR = A[2]
assert THIRD_CHAR == "o"
print(f"Third char: '{THIRD_CHAR}'")

THIRD_END_CHAR = A[-3]
assert THIRD_END_CHAR == "v"
print(f"Third end char: '{THIRD_END_CHAR}'")

A_LEN = len(A)
assert A_LEN == 20
print(f"Length of string: '{A_LEN}'")

REVERSED_A = A[::-1]
assert REVERSED_A == "revelc ylpmis ,adokS"
print(f"Reversed string: '{REVERSED_A}'")

EIGHT_CHAR = A[:8]
assert EIGHT_CHAR == "Skoda, s"
print(f"Eight chars: '{EIGHT_CHAR}'")
