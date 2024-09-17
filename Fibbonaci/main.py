#Nicholas Larsen Fibbonaci

numOne = 0
numTwo = 1
iterations = 1

print(numOne)
print(numTwo)
def findNextNumber():
    global numOne, numTwo, iterations
    numThree = numOne + numTwo
    print(numThree)
    numOne = numTwo
    numTwo = numThree
    iterations += 1

while iterations < 10: findNextNumber()