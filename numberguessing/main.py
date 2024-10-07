#Random allows us to chose a random number for later.
import random

#.randrange allows us to pick a number in a range.
num = random.randrange(1, 11)
#allows the progeram to loop infinitely if the player never guesses the right number.
while True:
    #Asks for user's number.
    userNum = int(input("Pick a number between 1 and 10."))
    #Checks if user was right
    if userNum == num:
        print("Correct!")
        #Stops the program
        break
    elif userNum > num:
        #If you guess to high tells  you.
        print("Too high.")
    else:
        #If you guess to low, tells you.
        print("Too low.")