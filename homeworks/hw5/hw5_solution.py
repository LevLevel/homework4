def add_ing(s: str) -> str:
    s += "ing"
    return s


def change_symbol(s: str) -> str:
    s = s.replace('#', '/')
    return s


def change_order(s: str) -> str:
    words = s.split()
    s = f"{words[1]} {words[0]}"
    return s


def clean_string(s: str) -> str:
    s = s.strip()
    return s


def to_capitalize(s: str) -> str:
    s = s.capitalize()
    return s


def to_list(s: str) -> list:
    result = s.split()
    return result


def formatting(array: list, s1: str, s2: str) -> str:
    name = ' '.join(array)
    return f"Hello, {name}! {s1} to {s2}"


def to_string(array: list) -> str:
    return ' '.join(array)


def insert_to_list(array: list, item: int | str, indx: int) -> list:
    result = array.copy()
    result.insert(indx, item)
    return result


def delete_from_list(array: list, indx: int) -> list:
    result = array.copy()
    del result[indx]
    return result
