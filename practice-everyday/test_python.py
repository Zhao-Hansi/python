a = 1000
b = 1000

print(a is b)  # False，因为a和b的内存地址不同

a = "hello"
b = "hello"

print(a is b)  # True，因为a和b的内存地址相同