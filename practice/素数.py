import math


def is_prime(num):
    """判断一个数是不是素数"""
    for factor in range(2, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


print(is_prime(123))