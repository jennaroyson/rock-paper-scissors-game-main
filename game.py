import random

import os
from dotenv import load_dotenv

load_dotenv()

x = os.getenv("PLAYER_NAME")
print("Welcome ",x,"! Lets play rock, paper, scissors, shoot!")


#PROMPT USER FOR INPUT

#x = input("choose 'rock' or 'paper' or 'scissors'")
user_choice = input("choose 'rock' or 'paper' or 'scissors': ")

# adpated from code shared by Dominic Parente
if user_choice in ["rock","paper","scissors"]:
    print("user chose:") 
    print(user_choice)
else:
    print("Your choice is not valid. Try typing something else, and let's keep it lowercase!")
    print("Try again")
    exit()

# COMPUTER CHOICE (AT RANDOM)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("computer chose:")
print(computer_choice)

if(user_choice == "rock" and computer_choice == "scissors"):
    print("WOOHOO! You win!")
elif(user_choice == "rock" and computer_choice == "paper"):
    print("Oh no! The computer beat you!")
elif(user_choice == "paper" and computer_choice == "scissors"):
    print("Oh no! The computer beat you!")
elif(user_choice == "paper" and computer_choice == "rock"):
    print("WOOHOO! You win!")
elif(user_choice == "scissors" and computer_choice == "rock"):
    print("Oh no! The computer beat you!")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print("WOOHOO! You win!")
else: print("Tie! Looks like you picked the same choice!")


print("Thanks for playing! Lets go again!")



