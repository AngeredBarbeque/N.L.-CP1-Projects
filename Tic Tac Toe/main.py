import random

rowOne = ["", "", ""]
rowTwo = ["", "", ""]
rowThree = ["", "", ""]
board = [rowOne, rowTwo, rowThree]
print("Hello! Welcome to tic-tac-toe! You will be X.")
playing = True
while playing == True:
    playerRow = int(input("Which row would you like to go in?"))
    playerColumn = int(input("Which column would you like to go in?"))
    if playerRow == 1:
        if rowOne[playerColumn - 1] == "":
            rowOne[playerColumn - 1] = "X"
    elif playerRow == 2:
        if rowTwo[playerColumn - 1] == "":
            rowTwo[playerColumn - 1] = "X"
    else:
        if rowThree[playerColumn - 1] == "":
            rowThree[playerColumn - 1] = "X"
    while True:
        compRow = random.randint(1, 3)
        compColumn = random.randint(1, 3)
        if compRow == 1:
            if rowOne[compColumn - 1] == "":
                rowOne[compColumn - 1] = "O"
                break
            else:
                continue
        elif compRow == 2:
            if rowTwo[compColumn - 1] == "":
                rowTwo[compColumn - 1] = "O"
                break
            else:
                continue
        else:
            if rowThree[compColumn - 1] == "":
                rowThree[compColumn - 1] = "O"
                break
            else:
                continue
for item in board:
    for i in item:
        print(i)