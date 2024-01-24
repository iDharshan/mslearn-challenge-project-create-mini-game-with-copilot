#Program a Rock, Paper, Scissors game where it is the player vs the computer.
#The computer’s answer will be randomly generated, while the program will ask the user for their input.
#This project will better your understanding of while loops and if statements.
#At the end of your game, ask your users if they want to play again.
#At the end of the game display the score of the player and computer.

import random
import sys

def game():
    print("Welcome to Rock, Paper, Scissors game")
    print("Please choose one of the following: ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    user = int(input("Enter your choice: "))
    computer = random.randint(1,3)
    if user == 1:
        if computer == 1:
            print("It's a tie")
        elif computer == 2:
            print("You lose")
        else:
            print("You win")
    elif user == 2:
        if computer == 1:
            print("You win")
        elif computer == 2:
            print("It's a tie")
        else:
            print("You lose")
    elif user == 3:
        if computer == 1:
            print("You lose")
        elif computer == 2:
            print("You win")
        else:
            print("It's a tie")
    elif user == 4:
        sys.exit()
    else:
        print("Invalid input")
    game()




