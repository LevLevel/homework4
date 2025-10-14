a = "Skoda, simply clever"

first_char = a[0]
assert first_char == "S"
print(f"First char: '{first_char}'")

last_char = a[-1]
assert last_char == "r"
print(f"Last char: '{last_char}'")

third_char = a[2]
assert third_char == "o"
print(f"Third char: '{third_char}'")

third_end_char = a[-3]
assert third_end_char == "v"
print(f"Third end char: '{third_end_char}'")

a_len = len(a)
assert a_len == 20
print(f"Length of string: '{a_len}'")

reversed_a = a[::-1]
assert reversed_a == "revelc ylpmis ,adokS"
print(f"Reversed string: '{reversed_a}'")

eight_chars = a[:8]
assert eight_chars == "Skoda, s"
print(f"Eight chars: '{eight_chars}'")
