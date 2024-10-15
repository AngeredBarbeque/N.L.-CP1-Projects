#Nicholas Larsen what is my grade

gradePer = int(input("What is your grade in percent form?"))

if gradePer >= 94:
    print("Your grade is an A!")
elif gradePer >= 90:
    print("Your grade is an A-!")
elif gradePer >= 87:
    print("Your grade is a B+!")
elif gradePer >= 84:
    print("Your grade is a B!")
elif gradePer >= 80:
    print("Your grade is a B-!")
elif gradePer >=77:
    print("Your grade is a C+!")
elif gradePer >= 74:
    print("Your grade is a C.")
elif gradePer >=70:
    print("Your grade is a C-.")
elif gradePer >= 67:
    print("Your grade is a D+.")
elif gradePer >= 64:
    print("Your grade is a D.")
elif gradePer >= 60:
    print("Your grade is a D-.")
else:
    print("Your grade is an F. Yikes.")
