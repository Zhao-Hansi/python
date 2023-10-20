import random


def random_n_and_sum():
    sum_result = 0
    random_n = random.randint(0, 200)
    print("random n is " + str(random_n))
    for i in range(0, random_n + 1):
        sum_result += i

    return sum_result


if __name__ == '__main__':
    print(random_n_and_sum())