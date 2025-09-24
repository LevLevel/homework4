def count_char(text):
    result = ""
    count = 1
    for i in range(len(text)):
        if i < len(text) - 1 and text[i] == text[i + 1]:
            count += 1
        else:
            result += text[i] + (str(count) if count > 1 else "")
            count = 1
    return result
