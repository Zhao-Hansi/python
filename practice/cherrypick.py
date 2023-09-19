# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i * j), end='\t')
#
#     print()
#
# a = [1, 3, 2, 4, 5]
# b = [1, 5, 6]
# for i in b:
#     if i in a:
#         pass
#     else:
#         a.append(i)
# print(a)

# n = input("pls:")
# a = 0
# b = 1
# for _ in range(int(n)+ 1):
#     a, b = [b, a + b]
#     sum1 = abs(a - int(n))
#     max = 1000000000
#     if max < sum1:
#         max = sum1
# print(max)
# def run_length_encoding(s):
#     result = ""
#     count = 1
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             result += str(count) + s[i - 1]
#             count = 1
#     result += str(count) + s[-1]
#     return result
# #
# #
# # if __name__ == '__main__':
# #     print(run_length_encoding('aaabccccccdd'))
#
# def fibonacci(n):
#     a = 1
#     b = 0
#     for _ in range(n):
#         a, b = b, a + b
#         print(a)
#
#
# if __name__ == '__main__':
#     fibonacci(10)

