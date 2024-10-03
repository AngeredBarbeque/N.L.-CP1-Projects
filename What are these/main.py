#Nicholas Larsen

number = float(input("Please input a number: "))
print("Your number with commas to seperate thousands is {:,}.".format(int(number)))
print("Your money with 4 decimal points is {:.4f}.".format(number))
print("Your money as a percentage is {:.0%}.".format(number))
print("Your number as money is ${:.2f}.".format(number))