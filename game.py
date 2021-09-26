print("Rock, Paper, Scissors, Shoot!")
import random

print("Welcome Player One! Lets play rock, paper, scissors, shoot!")

user_choice = input("choose 'rock' or 'paper' or 'scissors': ")
if user_choice in ["rock","paper","scissors"]:
    print("user chose:") 
    print(user_choice)
else:
    print("You choice is not valid. Try typing somehting else, and let's keep it lowercase!")
    print("Try again")
    exit()

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