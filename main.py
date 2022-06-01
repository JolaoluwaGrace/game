from ast import Break
from pickle import TRUE
import random

possible_actions = ["R", "P", "S"]
game = {"R":"Rock", "P":"Paper", "S":"Scissors"}

while True:
    
    user_action = input("pick an option (R, P, S):")
    
    user_action = user_action.strip().upper()
    if not user_action in possible_actions:
        print("Invalid input!")
        continue

    computer_action = random.choice (possible_actions)
    print(f"\nPlayer ({game[user_action]}) : CPU ({game[computer_action]}).\n")
    if user_action == computer_action:
        print(f"Both players selected {game[user_action]}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")