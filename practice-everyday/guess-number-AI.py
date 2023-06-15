"""
3. 猜数字的AI
和猜数字一样，不过这次是设计一个能猜数字的AI

功能描述： 用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
"""


def guess_number():
    target = int(input("请输入一个单位以内的数字："))
    low = 0
    high = 100
    guess = (low + high) // 2
    num_guesses = 1

    while guess != target:
        if guess > target:
            high = guess
        else:
            low = guess + 1
        guess = (low + high) // 2
        num_guesses += 1

    print("猜中了！数字是", target, "，猜测次数为", num_guesses)


guess_number()