#Nicholas Larsen Area Calculator
def rectArea ():
    dimensionOne = float(input("What is the length of your rectangle/square?"))
    dimensionTwo = float(input("What is the width of your rectangle/square?"))
    area = dimensionOne*dimensionTwo
    print("Your area is", area)

def triArea ():
    dimensionOne = float(input("What is the base of your triangle?"))
    dimensionTwo = float(input("What is the height of your triangle?"))
    area = dimensionOne*dimensionTwo/2
    print("Your area is", area)

def cirArea ():
    dimensionOne = float(input("What is the radius of your circle?"))
    area = dimensionOne**2*3.14159265358979
    print("Your area is", area)

def trapArea():
    dimensionOne = float(input("What is the first base of your trapezoid?"))
    dimensionTwo = float(input("What is the second base of your trapezoid?"))
    dimensionThree = float(input("What is the height of your trapezoid?"))
    area = ((dimensionOne+dimensionTwo)/2)*dimensionThree
    print("Your area is", area)

choice = int(input("This is an area claculator.\n press 1 for rectangle/square\n press 2 for triangle\n press 3 for circle\n press 4 for trapezoid:"))
if choice == 1:
    rectArea()
elif choice == 2:
    triArea()
elif choice == 3:
    cirArea()
elif choice == 4:
    trapArea()
else:
    print("We're sorry, but you typed a wrong number. Buffoon.")
