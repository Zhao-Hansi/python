def addition_method(number_a, number_b):
    return number_b + number_a


def subtraction_method(number_a, number_b):
    return number_a - number_b


def multiplication_method(number_a, number_b):
    return number_a * number_b


def division_method(number_a, number_b):
    return number_a / number_b


if __name__ == '__main__':
    while True:
        number1 = input('pls input the first number you want to calculate:')
        calculate_type = input('pls input the calculate type:')
        number2 = input('pls input the second number you want to calculate:')
        try:
            number1 = float(number1)
            number2 = float(number2)
            if calculate_type == '+':
                print(addition_method(number1, number2))
            elif calculate_type == '-':
                print(subtraction_method(number1, number2))
            elif calculate_type == '*':
                print(multiplication_method(number1, number2))
            elif calculate_type == '/':
                print(division_method(number1, number2))
        except ValueError:
            print('pls check your input ensurance your input type is correct!')

        choice = input("Continue calculate？（Y/N）")
        if choice.upper() != "Y":
            break

