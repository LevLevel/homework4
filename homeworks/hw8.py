def ascending_sequence(arr):
    def is_increasing(seq):
        for i in range(len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return False
        return True

    if is_increasing(arr):
        return True

    for i in range(len(arr)):
        temp = arr[:i] + arr[i + 1:]
        if is_increasing(temp):
            return True

    return False


def number_opposite(n, first_number):
    return (first_number + n // 2) % n


def is_card_number_valid(number):
    if number is None:
        return False
    if not str(number).isdigit():
        return False

    digits = [int(d) for d in str(number)]
    total = 0

    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit

    return total % 10 == 0
