# HW_03.py

import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize phone numbers in any arbitrary format, assuming that
    numbers that start with '+380' or '0' are local and are cast
    uniformly according to the Ukrainian phone number standard
    (+380XXXXXXXXX). Otherwise, numbers are processed as foreign
    phone numbers.
    IMPORTANT NOTE. The Ukrainian international phone code is +380,
    not +38. Thus, the presented way of collecting data in the
    format that starts with '0XX' is incorrect.
    :param phone_number: Raw phone number in arbitrary format.
    :return: The list of standardized phone numbers.
    """

    clear = re.sub(r'\D', '', phone_number.strip())
    if clear.startswith('380') or clear.startswith('0'):
       return f'+380{clear[-9:]}'
    return f'+{clear}'


raw_numbers = [
    "+381 11 2345678",
    "+48  000.111.222",
    "48999888777",
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(f'Normalized numbers for SMS campaign: {sanitized_numbers}')
