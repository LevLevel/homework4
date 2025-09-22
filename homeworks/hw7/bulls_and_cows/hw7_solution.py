import random


def check_guess(bulls, cows):
    secret = bulls
    guess = cows
    bulls_count = 0
    cows_count = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls_count += 1
        elif guess[i] in secret:
            cows_count += 1

    return bulls_count, cows_count


def generate_secret_number():
    digits = list(range(10))
    random.shuffle(digits)
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(map(str, digits[:4]))
