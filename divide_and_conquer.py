def sum_recursively(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    return arr[-1] + sum_recursively(arr[:-1])


def count_recursively(arr: list) -> int:
    if len(arr) == 1:
        return 1
    return 1 + count_recursively(arr[:-1])


def max_recursively(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    num2 = max_recursively(arr[:-1])
    return arr[-1] if arr[-1] > num2 else num2


if __name__ == '__main__':
    my_arr = [1, 12, 3, 4, 7, 13, 9, 2]
    print(f'Sum: {sum_recursively(my_arr)}')
    print(f'Count: {count_recursively(my_arr)}')
    print(f'Max: {max_recursively(my_arr)}')
