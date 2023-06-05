# 编写一个程序，接受用户输入的整数列表，将其中的所有元素按照大小重新排列并输出结果

Integer_list = input('pls input a Integer List').split()

Integer_list = [int(num) for num in Integer_list]

print(sorted(Integer_list))