# 编写一个函数，接受一个字符串作为输入参数，将其转换为整数并返回结果。如果无法转换字符串为整数，则引发ValueError异常

def valueErrorFunction(string_a):
    try:
        num = int(string_a)
    except ValueError:
        print('transform failed')

    return num


# 编写一个函数，接受一个列表和一个整数作为输入参数，返回列表中指定索引的元素。如果索引超出列表范围，则引发IndexError异常

def indexErrorFunction(list_a, number):
    try:
        print(list_a[number])
    except IndexError:
        print('Index out of range')


if __name__ == '__main__':
    indexErrorFunction([1, 2, 3], 5)
