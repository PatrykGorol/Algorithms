from random import choice
from itertools import chain


def quicksort_my_version(arr: list, left: int, right: int):
    '''

    :param arr: list of integers (duplicates are acceptable)
    :param left: starting index of range to sort
    :param right: last index of range to sort
    :return: None
    '''
    if left >= right:
        return None
    random = choice(range(left, right + 1))
    arr[random], arr[right] = arr[right], arr[random]
    pivot = arr[right]
    border = left - 1
    i = left
    while i < right:
        if arr[i] < pivot:
            border += 1
            if i != border:
                arr[border], arr[i] = arr[i], arr[border]
        i += 1

    border += 1
    if right != border:
        arr[border], arr[right] = arr[right], arr[border]

    # Conditions for minimising stack height
    if border - left < right - border:
        quicksort_my_version(arr, left, border - 1)
        quicksort_my_version(arr, border + 1, right)
    else:
        quicksort_my_version(arr, border + 1, right)
        quicksort_my_version(arr, left, border - 1)
    return None


def quicksort_book_version(arr: list) -> list:
    '''
    Implementation according to book description.
    :param arr: list of integers (duplicates are acceptable)
    :return: sorted array
    '''
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        return arr if arr[0] <= arr[1] else reversed(arr)
    pivot = choice(arr)
    lower = [i for i in arr if i < pivot]
    equal = [i for i in arr if i == pivot]
    greater = [i for i in arr if i > pivot]
    return list(chain(quicksort_book_version(lower), equal, quicksort_book_version(greater)))


if __name__ == '__main__':
    arr = [5, 7, 2, 12, 8, 9, 5, 17, 2, 34, 27, 1]
    print(arr)
    arr_copy = arr.copy()
    quicksort_my_version(arr_copy, 0, len(arr) - 1)
    print(arr_copy)

    print(quicksort_book_version(arr))
