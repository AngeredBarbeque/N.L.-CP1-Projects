#Nicholas Larsen rock paper scissors
import random
score = 0
CPUscore = 0
playing = "Y"
print("Welcome to rock paper scissors!")
while playing == "Y":
    userChoice = input("Rock, Paper, or Scissors?")
    CPUChoice = random.randint(1, 3)
    if CPUChoice == 1:
        CPUChoice = "rock"
    if CPUChoice == 2:
        CPUChoice = "paper"
    if CPUChoice == 3:
        CPUChoice = "scissors"
    print(CPUChoice)
    if CPUChoice == userChoice:
        print("You tied!")
    elif CPUChoice == "rock" and userChoice == "paper":
        print("You won!")
    elif CPUChoice == "rock" and userChoice == "scissors":
        print("You lost.")
    elif CPUChoice == "paper" and userChoice == "rock":
        print("You lost.")
    elif CPUChoice == "paper" and userChoice == "scissors":
        print("You won!")
    elif CPUChoice == "scissors" and userChoice == "rock":
        print("You won!")
    elif CPUChoice == "scissors" and userChoice == "paper":
        print("You lost.")
    else:
        print("Sorry, please renter an input in all lowercase.")
        continue
    playing = input("Play again? Y/N:")


