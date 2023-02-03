def gcd(x, y):
    """求最大公约数"""
    """取两个数中比较小的数进行计算，循环较小的数到1， 直到满足同时被整除"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    """两个数相乘除以最大公约数就是最小公倍数"""
    return x * y // gcd(x, y)


if __name__ == '__main__':
    print(gcd(190, 32))
    print(lcm(3, 98))