#Nicholas Larsen Quiz Creation

print("This is a true or false quiz. Please type true or false for each answer. Use no capital letters.")

answerOne = input("A hedgehog is a mammal.")

answerTwo = input("Orange is a color.")

answerThree = input("(3+3/2)+900 = 903.")

answerFour = input("Osteoporosis is the process of removing a persons's bones.")

answerFive = input("In the book Frankenstein by Mary shelley, the main character creates a monster named Frankenstein.")

points = 0

if answerOne == "true": points = points+1 
if answerTwo == "true": points = points+1
if answerThree == "false": points = points+1
if answerFour == "false": points = points+1
if answerFive == "false": points = points+1

print("Your score out of 5 is", points)
if points <= 2: print("Wow, you really suck at this, don't you?")
if points == 5: print("5 out of 5? I think you cheated. Jerk.")