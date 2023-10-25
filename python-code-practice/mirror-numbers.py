# 用python实现该场景，寻找镜像数字，例如1221的镜像数字是22 1221

def find_mirror_numbers(nums):
    number_str = str(nums)
    length = len(number_str)
    mirror_numbers = set()

    for i in range(length):
        for j in range(i + 2, length + 1):
            current_number = int(number_str[i:j])
            current_mirror = int(str(current_number)[::-1])
            if current_mirror == current_number:
                mirror_numbers.add(current_number)

    return list(mirror_numbers)



print(find_mirror_numbers(123321))
