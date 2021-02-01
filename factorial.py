def factorial_recursively(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial_recursively(num - 1)


if __name__ == '__main__':
    print(factorial_recursively(5))
