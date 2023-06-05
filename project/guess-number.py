import random

random_number = random.randint(0, 100)
guess_count = 0

while guess_count < 10:
    guess_number = input("Please guess a number between 0 and 100: ")
    try:
        guess_number = int(guess_number)
    except ValueError:
        print("Invalid input! Please input a number.")
        continue

    if guess_number > random_number:
        print("Your guess is too high.")
    elif guess_number < random_number:
        print("Your guess is too low.")
    else:
        print("Congratulations! You have guessed the number.")
        break

    guess_count += 1

if guess_count >= 10:
    print("You have used up all your chances.")

print("The correct number is {}.".format(random_number))
