# 编写一个程序，接受用户输入的整数列表，将其中的所有偶数提取出来并输出结果
num_list = input("请输入整数列表，用空格分隔：").split()

num_list = [int(num) for num in num_list]

even_list = [num for num in num_list if num % 2 == 0]

print("输入的整数列表为：", num_list)
print("其中的偶数为：", even_list)