def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


print(is_palindrome(123321))


def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s

    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1

    # 单个字符都是回文
    for i in range(n):
        dp[i][i] = True

    # 遍历长度为2到n的子串
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # 首尾字符相同且去掉首尾后的子串是回文
            if s[i] == s[j]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_len:
                        max_len = length
                        start = i

    return s[start: start + max_len]


# 测试
s = "babad"
print(longestPalindrome(s))  # 输出："bab" 或 "aba"

s = "cbbd"
print(longestPalindrome(s))  # 输出："bb"