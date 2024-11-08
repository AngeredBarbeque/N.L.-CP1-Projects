while True:
    choice = input("What operation do you want? Type 1 for addition, 2 for subraction, 3 for multiplication, 4 for division, 5 for modulo, 6 for exponents, or 7 for rounded division.")
    number = input("Which is the first of the numbers thee shalt be preforming thine operations upon?")
    numberTwo = input("Which is the second of the numbers thee shalt be preforming thine operations upon?")
    try:
        choice = float(choice)
    except:
        print("Sorry, please use a number as your input.")
        continue
    try:
        number = float(number)
    except:
        print("Sorry, please use a number as your input.")
        continue
    try:
        numberTwo = float(numberTwo)
    except:
        print("Sorry, please use a number as your input.")
        continue
    if choice == 4:
        if numberTwo == 0:
            print("Sorry, you can't divide by zero.")
            continue
    break

answer = 0
if choice == 1:
    answer = number + numberTwo
elif choice == 2:
    answer = number - numberTwo
elif choice == 3:
    answer = number * numberTwo
elif choice == 4:
    answer = number / numberTwo
elif choice == 5:
    answer = number % numberTwo
elif choice == 6:
    answer = number ** numberTwo
elif choice == 7:
    answer = number // numberTwo
print("The answer is", answer, "why couldn't you do that yourself?")
