#Matthew McKinley Rock Paper Scissors

import random

wins = int(0)
games = int(0)

while True:
    choice = int(input("What weapon would you like to use? (1 for Rock, 2 for Paper, 3 for Scissors)"))
    if choice == 1:
        choice = "Rock"
        print(choice)
    elif choice == 2:
        choice = "Paper"
        print(choice)
    elif choice == 3:
        choice = "Scissors"
        print(choice)
    else:
        print("You did not write 1, 2, or 3")
    comchoice = random.randint(1,3)
    if comchoice == 1:
        comchoice = "Rock"
        print(comchoice)
    if comchoice == 2:
        comchoice = "Paper"
        print(comchoice)
    if comchoice == 3:
        comchoice = "Scissors"
        print(comchoice)
        print("Your score is ", wins, "out of ", games)
    playagain = input("Do you want to play again (Y/N)?")
    if playagain == "Y":
        continue
    elif playagain == "N":
        break
    else:
        print("You typed something wrong")

    def playerwin():
        global games
        global wins
        print("You won!")
        wins = wins + 1
        games = games + 1
        playagain()

    def draw():
        global games
        print("You tied!")
        games = games + 1
        playagain()

    def playerlose():
        global games
        print("You lost!")
        games = games + 1
        playagain()

#tie conditions
    if choice == "Rock" and comchoice == "Rock":
        draw()
    elif choice == "Paper" and comchoice == "Paper":
        draw()
    elif choice == "Scissors" and comchoice == "Scissors":
        draw()
#win conditions
    elif choice == "Rock" and comchoice == "Scissors":
        playerwin()
    elif choice == "Paper" and comchoice == "Rock":
        playerwin()
    elif choice == "Scissors" and comchoice == "Paper":
        playerwin()
#lose conditions
    elif choice == "Scissors" and comchoice == "Rock":
        playerlose()
    elif choice == "Rock" and comchoice == "Paper":
        playerlose()
    elif choice == "Paper" and comchoice == "Scissors":
        playerlose()
    else:
        print("You typed something wrong!")
        playagain()