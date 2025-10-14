def analyze_file(filename):
    try:
        pass
    finally:
        with open('test.txt', 'w', encoding='utf-8') as file_output:
            file_output.write("""Volksvagen Das Auto
            Audi Truth in Engineering
            Porsche Driven by dreams
            Skoda Simply clever""")

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    lines_num = len(content.splitlines())
    words_num = len(content.split())
    letters_num = sum(c.isalpha() for c in content)

    result = f"Строки: {lines_num}\nСлова: {words_num}\nБуквы: {letters_num}"

    print(result)

    with open('test.txt', 'a', encoding='utf-8') as file_append:
        file_append.write("\n" + result)

    return lines_num, words_num, letters_num


lines_count, words_count, letters_count = analyze_file('test.txt')

print("Содержимое файла:")
print("=" * 30)
with open('test.txt', 'r', encoding='utf-8') as file_in:
    print(file_in.read())
print("=" * 30)

assert lines_count == 4
assert words_count == 14
assert letters_count == 77
