#Nicholas Larsen

number = float(input("Please input a number: "))
print("Your number is {:,}".format(int(number)))
print("or {:.4f}".format(number))
print("or {:.0%}".format(number))
print("or ${:.2f}".format(number))