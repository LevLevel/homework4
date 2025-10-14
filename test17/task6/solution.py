def analyze_file(filename):
    try:
        pass
    finally:
        with open('test.txt', 'w', encoding='utf-8') as f:
            f.write("""Volksvagen Das Auto
            Audi Truth in Engineering
            Porsche Driven by dreams
            Skoda Simply clever""")

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    lines_counter = len(content.splitlines())
    words_count = len(content.split())
    letters_count = sum(c.isalpha() for c in content)

    result = f"Строки: {lines_counter}\nСлова: {words_count}\nБуквы: {letters_count}"

    print(result)

    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write("\n" + result)

    return lines_counter, words_count, letters_count


lines_counter, words_count, letters_count = analyze_file('test.txt')

print("Содержимое файла:")
print("=" * 30)
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("=" * 30)

assert lines_counter == 4
assert words_count == 14
assert letters_count == 77
