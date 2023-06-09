def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y


def calculator():
    while True:
        num1_str = input("请输入第一个数字：")
        op = input("请输入运算符（+、-、*、/）：")
        num2_str = input("请输入第二个数字：")

        try:
            num1 = float(num1_str)
            num2 = float(num2_str)

            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            else:
                print("无效的运算符")
                continue

            print("结果：", result)

        except ValueError:
            print("输入无效，请重新输入")

        choice = input("是否继续计算？（Y/N）")
        if choice.upper() != "Y":
            break


calculator()
