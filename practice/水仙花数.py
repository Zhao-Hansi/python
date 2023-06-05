# 水仙花数是一个三位数，同时满足每位数的立方和等于本身

for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    # print(low, mid,high)
    if i == low ** 3 + mid ** 3 + high ** 3:
        print(i)