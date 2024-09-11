#Nicholas Larsen Skill Practice average grade.

gradeOne=input("What's your first grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeTwo=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeThree=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeFour=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeFive=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeSix=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")
gradeSeven=input("What's your next grade in 4.0 format? A is 4.0 A- is 3.66, B+ is 3.33, B is 3.0 etc.")

gradeOne = float(gradeOne)
gradeTwo = float(gradeTwo)
gradeThree = float(gradeThree)
gradeFour = float(gradeFour)
gradeFive = float(gradeFive)
gradeSix = float(gradeSix)
gradeSeven = float(gradeSeven)

average=((gradeOne + gradeTwo + gradeThree + gradeFour + gradeFive + gradeSix + gradeSeven)/7)
print("Your average grade is", average)
if average < 3:print("You better get your grade up, loser.")
if average > 3:print("Congrats! Keep working hard.")