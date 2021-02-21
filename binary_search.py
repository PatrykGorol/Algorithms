from typing import Optional


def binary_search(arr: list, item: int) -> Optional[int]:
    '''
    Searches for index of given value on the list.
    Time complexity: O(log n)
    :param arr: SORTED list (ascending)
    :param item: searched value
    :return: item's index on the list
    '''
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == arr[mid]:
            return mid
        if item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recursively(arr: list, item: int) -> Optional[int]:
    if len(arr) == 1:
        return 0 if arr[0] == item else None
    mid = len(arr) // 2
    if arr[mid] == item:
        return mid
    if item > arr[mid]:
        search = binary_search_recursively(arr[mid + 1:], item)
        return mid + 1 + search if search is not None else None
    else:
        return binary_search_recursively(arr[:mid], item)


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9, 12, 13, 19]
    print(my_list)
    print(f'Index of 1: {binary_search(my_list, 1)}')
    print(f'Index of 3: {binary_search(my_list, 3)}')
    print(f'Index of 5: {binary_search(my_list, 5)}')
    print(f'Index of 7: {binary_search(my_list, 7)}')
    print(f'Index of 19: {binary_search(my_list, 19)}')
    print(f'Index of -1: {binary_search(my_list, -1)}')
    print()
    item = 3
    print(f'Binary search recursively (index of {item}): {binary_search_recursively(sorted(my_list), item)}')
