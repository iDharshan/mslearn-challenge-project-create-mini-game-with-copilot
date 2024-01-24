#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random
import sys

def play_again():
    while True:
        user_input = input("Would you like to play again? (Y/N) ").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("Invalid input. Please try again.")

def get_user_choice():
    while True:
        user_input = input("Please choose one of the following: rock, paper, or scissors: ").lower()
        if user_input == "rock":
            return "rock"
        elif user_input == "paper":
            return "paper"
        elif user_input == "scissors":
            return "scissors"
        else:
            print("Invalid input. Please try again.")

def get_computer_choice():
    computer_choice = random.randint(1, 3)
    if computer_choice == 1:
        return "rock"
    elif computer_choice == 2:
        return "paper"
    elif computer_choice == 3:
        return "scissors"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif user_choice == "rock":
        if computer_choice == "paper":
            return "computer"
        elif computer_choice == "scissors":
            return "user"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "user"
        elif computer_choice == "scissors":
            return "computer"
    elif user_choice == "scissors":
        if computer_choice == "rock":
            return "computer"
        elif computer_choice == "paper":
            return "user"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You won!")
            user_score += 1
        elif winner == "computer":
            print("The computer won!")
            computer_score += 1
        elif winner == "tie":
            print("You tied!")
        print(f"Score: You {user_score}, Computer {computer_score}")
        if not play_again():
            break
    print("Thanks for playing!")

play_game()




