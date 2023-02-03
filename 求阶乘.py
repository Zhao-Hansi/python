import math

m = int(input('m = '))
n = int(input('n = '))
print(math.factorial(m) // math.factorial(n) // math.factorial(m - n))