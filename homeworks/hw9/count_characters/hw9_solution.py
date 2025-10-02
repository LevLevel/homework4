def count_char(raw_str):
    if not raw_str:
        return ""

    result = ""
    count = 1

    for i, char in enumerate(raw_str):
        if i < len(raw_str) - 1 and char == raw_str[i + 1]:
            count += 1
        else:
            result += char + (str(count) if count > 1 else "")
            count = 1

    return result
