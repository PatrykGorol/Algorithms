def find_smallest(arr: list) -> int:
    smallest_index = 0
    smallest_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index


def selecion_sort(arr: list) -> list:
    '''
    Time complexity: O(n^2)
    :param arr: list
    :return: sorted list ascending
    '''
    new_arr = []
    while len(arr):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


if __name__ == '__main__':
    arr = [5, 3, 6, 2, 10]
    print(selecion_sort(arr))
