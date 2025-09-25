def remove_previous_symbol(text):
    result = ""
    for char in text:
        if char == '#':
            result = result[:-1]
        else:
            result += char
    return result
