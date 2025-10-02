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
