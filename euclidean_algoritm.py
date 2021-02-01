import functools


def euclidean_algorithm(a: int, b: int) -> int:
    '''
    Finds greatest common divisor of two numbers.
    :param a: integer number
    :param b: integer number
    :return: gcd(a, b)
    '''
    while b:
        a, b = b, a % b
    return a


def print_gcd(*nums: int) -> None:
    d = functools.reduce(lambda a, b: euclidean_algorithm(a, b), nums)
    print(f'gcd({", ".join(str(num) for num in nums)}) = {d}')
    return None


if __name__ == '__main__':
    print_gcd(15, 12)
    print_gcd(12, 15)
    print_gcd(12, 12)
    print_gcd(15, 0)
    print_gcd(0, 0)
    print_gcd(1989, 867)
    print_gcd(576, 171, 63)
    print_gcd(14, 147, 21)
