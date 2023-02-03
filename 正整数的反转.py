# 将12345变成54321

num = int(input('please input a number:'))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
    print('reversed %d' % reversed_num)
    print('num %d' % num)
print(reversed_num)
