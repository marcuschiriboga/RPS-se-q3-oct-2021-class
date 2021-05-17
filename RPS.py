# https://realpython.com/python-rock-paper-scissors/

import random
# pictures
user_action = input("enter a choice (rock, paper, scissors): ")
if user_action not in ["rock", "paper", "scissors"]:
    print("you chose poorly")
    quit()
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\n human: {user_action} | computer: {computer_action}")
