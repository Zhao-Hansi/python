# 编写一个程序，接受用户输入的列表和一个元素，统计该元素在列表中出现的次数并输出结果

list_input = input('pls input a list').split()

list_input = [int(num) for num in list_input]

number = input('pls input a number')

number = int(number)

amount_number = 0
for num in list_input:
    if num == number:
        amount_number += 1

print(amount_number)
