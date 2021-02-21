import random
from timeit import timeit
from typing import List, Tuple

from quicksort import quicksort_my_version, quicksort_book_version


def create_random_list(numbers: int, range_: Tuple[int, int], duplicates: bool = True) -> List[int]:
    """
    Generates list of random, unsorted numbers from given range.
    :param numbers: how many numbers do you want?
    :param range_: what is a range you want to generate numbers from; two numbers as the beginning and the end of range
    :param duplicates: do you want duplicates in the result?
    :return: list of numbers
    """
    if duplicates:
        return random.choices(range(range_[0], range_[1] + 1), k=numbers)
    return random.sample(range(range_[0], range_[1] + 1), k=numbers)


def measure_time(test_code: str, setup: str, n: int) -> str:
    """
    Executes test code, measure execution time and prints it out.
    :param test_code: code of function to execute
    :param setup: import function and input list
    :param n: how many times function will be execute
    :return: aggregate time of executing function n times
    """
    return '{:,.0f}'.format(timeit(test_code, setup, number=n) * 1000)


if __name__ == '__main__':
    numbers = 10_000
    range_ = (0, 100_000)
    duplicates = True
    timer_reps = 1_000

    random_list = create_random_list(numbers=numbers, range_=range_, duplicates=duplicates)
    list_copy = random_list.copy()

    print(f'Random list:\n{random_list}')
    print('-' * 100)
    print(f'{numbers:,} numbers from range({range_[0]:,}; {range_[1]:,}) with{"out" * (not duplicates)} duplicates.')
    print('-' * 100)


    print('QUICKSORT')

    test_code = "quicksort_my_version(list_copy, 0, len(list_copy) - 1)"
    setup = "from __main__ import quicksort_my_version, list_copy"
    time = measure_time(test_code, setup, timer_reps)
    print(f'My version: {time} milliseconds.')

    list_copy = random_list.copy()  # my version sorts an array in place, so new assignment has to be done
    test_code = "quicksort_book_version(list_copy)"
    setup = "from __main__ import quicksort_book_version, list_copy"
    time = measure_time(test_code, setup, timer_reps)
    print(f'Book version: {time} milliseconds.')
