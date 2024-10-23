#Nicholas Larsen rock paper scissors
import random
score = 0
cpuscore = 0
playing = "Y"
print("Welcome to rock paper scissors!")
while playing == "Y":
    userChoice = input("Rock, Paper, or Scissors?")
    cpuChoice = random.randint(1, 3)
    if cpuChoice == 1:
        cpuChoice = "rock"
    if cpuChoice == 2:
        cpuChoice = "paper"
    if cpuChoice == 3:
        cpuChoice = "scissors"
    print(cpuChoice)
    if cpuChoice == userChoice:
        print("You tied!")
    elif cpuChoice == "rock" and userChoice == "paper":
        print("You won!")
        score += 1
    elif cpuChoice == "rock" and userChoice == "scissors":
        print("You lost.")
        cpuscore += 1
    elif cpuChoice == "paper" and userChoice == "rock":
        print("You lost.")
        cpuscore += 1
    elif cpuChoice == "paper" and userChoice == "scissors":
        print("You won!")
        score += 1
    elif cpuChoice == "scissors" and userChoice == "rock":
        print("You won!")
        score += 1
    elif cpuChoice == "scissors" and userChoice == "paper":
        print("You lost.")
        cpuscore += 1
    else:
        print("Sorry, please renter an input in all lowercase.")
        continue
    print("Your score is", score)
    print("CPU score is", cpuscore)
    playing = input("Play again? Y/N:")


