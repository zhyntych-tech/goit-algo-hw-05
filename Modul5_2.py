import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r' -?\d+[\.,]\d+ | -?\d+ '
    for word in text.split():
        if re.fullmatch(pattern, word):
            yield float(word.replace(',', '.')) # замінюємо ',' на '.' для перетворення у float


def sum_profit(text: str, func: Callable):
    total_sum = 0
    for number in func(text):
        total_sum += number
    return total_sum
