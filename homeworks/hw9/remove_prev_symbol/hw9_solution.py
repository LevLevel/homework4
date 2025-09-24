def remove_previous_symbol(text):
    while '#' in text:
        i = text.find('#')
        if i > 0:
            text = text[:i - 1] + text[i + 1:]
        else:
            text = text[1:]
    return text
