def remove_previous_symbol(text):
    while '#' in text:
        index = text.find('#')
        if index > 0:
            text = text[:index - 1] + text[index + 1:]
        else:
            text = text[1:]
    return text
