for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print()


def max_subarray_sum(nums):
    if not nums:
        return 0

    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# 示例使用
sequence = [-1, -2, -3, -10, -4, -7, -2, -5]
result = max_subarray_sum(sequence)
print("最大连续子序列的和为:", result)
