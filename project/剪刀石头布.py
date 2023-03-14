import random

print("Welcome to the rock-paper-scissors game!")
while True:
    player_choice = input("Please choose rock, paper, or scissors (or 'q' to quit): ")
    if player_choice == 'q':
        print("Thanks for playing!")
        break

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print("You chose", player_choice)
    print("The computer chose", computer_choice)

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("You win!")
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You win!")
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You win!")
    else:
        print("You lose!")
