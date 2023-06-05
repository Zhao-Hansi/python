# 编写一个函数，接受用户输入的整数列表，返回其中的最大值和最小值

def return_max_and_min_function():
    lst = input('pls input a integra list').split()

    num_list = [int(num) for num in lst]

    return max(num_list), min(num_list)


if __name__ == '__main__':
    print(return_max_and_min_function())
