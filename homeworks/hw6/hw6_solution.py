def level_up(experience: int, threshold: int, reward: int) -> bool:
    return experience + reward >= threshold


def motor_time(n: int) -> int:
    hours = n // 60
    minutes = n % 60
    hour_digit1 = hours // 10
    hour_digit2 = hours % 10
    minute_digit1 = minutes // 10
    minute_digit2 = minutes % 10
    return hour_digit1 + hour_digit2 + minute_digit1 + minute_digit2


def time_converter(time_str: str) -> str:
    time = time_str.split(':')
    hour = int(time[0])
    minute = int(time[1])
    period_index = hour // 12
    period = ["a.m.", "p.m."][period_index]
    hours_12 = hour % 12
    hours_12 = hours_12 + 12 * (hours_12 == 0)
    return f"{hours_12}:{minute:02d} {period}"
