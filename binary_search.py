from typing import Optional


def binary_search(list_, item) -> Optional[int, None]:
    '''
    Searches for index of given value on the list.
    Time complexity: O(log n)
    :param list_: SORTED list (ascending)
    :param item: searched value
    :return: item's index on the list
    '''
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == list_[mid]:
            return mid
        if item > list_[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 1))
    print(binary_search(my_list, 3))
    print(binary_search(my_list, 5))
    print(binary_search(my_list, 7))
    print(binary_search(my_list, 9))
    print(binary_search(my_list, -1))
