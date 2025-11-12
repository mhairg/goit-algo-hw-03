# HW_02.py

import random


def get_numbers_ticket(minimum: int, maximum: int, quantity: int) -> list[int]:
    """
    Generate an ordered list of unique numbers in a predefined range
    and of a predefined length.
    :param minimum: Number to be used as a range start value.
    :param maximum: Number to be used as a range end value.
    :param quantity: Number to be used as a list length definer.
    :return: An ordered list of randomly selected unique numbers OR an
    empty list if the range limits don't match the required values.
    """
    if (minimum < 1 or maximum > 1000) or (quantity > (maximum - minimum)):
        return []
    lottery_numbers = random.sample(range(minimum, maximum), k=quantity)
    return sorted(lottery_numbers)


lottery = get_numbers_ticket(1, 49, 6)
print(f'Your lottery numbers: {lottery}')
