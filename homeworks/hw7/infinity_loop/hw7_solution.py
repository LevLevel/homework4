def infinity_loop(a, b):
    if a < b:
        return (b - a) % 2 != 0
    elif a > b:
        return True
    else:
        return False