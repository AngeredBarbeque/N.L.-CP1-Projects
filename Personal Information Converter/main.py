#Nick Larsen Personal information converter

name = input("Please enter your name: ")
age = input("Please enter your age: ")
height = input("What is your height in meters, please enter in decimal form: ")
favNum = input("What is your favorite number?: ")

print(name, "age", age, height, "meters tall", favNum)

age = int(age)
height = float(height)
favNum = int(favNum)
print(name, "age", age, height, "meters tall", favNum)