import random

answer = random.randint(1, 100)
count: int = 0
while True:
    count += 1
    number = int(input("please input a number which in 1 - 100:"))
    if number > answer:
        print("it is over answer")
    elif number < answer:
        print("it is smaller answer")
    else:
        print("congratulation! you got correct answer")
        break
count = int(count)
print('you have totally guesses %d' % count)
if count > 3:
    print("you are stupid!")
