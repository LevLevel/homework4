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

    lines = len(content.splitlines())
    words = len(content.split())
    letters = sum(c.isalpha() for c in content)

    result = f"Строки: {lines}\nСлова: {words}\nБуквы: {letters}"

    print(result)

    with open('test.txt', 'a', encoding='utf-8') as f:
        f.write("\n" + result)

    return lines, words, letters


lines, words, letters = analyze_file('test.txt')

print("Содержимое файла:")
print("=" * 30)
with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read())
print("=" * 30)

assert lines == 4
assert words == 14
assert letters == 77
