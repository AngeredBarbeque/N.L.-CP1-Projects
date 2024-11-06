score = 0
print("Hello, welcome to a quiz!")
print("What color are flamingos at birth?")
print("A: Pink")
print("B: Brown")
print("C: White")
print("D: Green")
answer = input("")
if answer == "C":
    score += 1
    print("Which of the following is the study of disease?")
    print("A: Epdibegolgogy")
    print("B: Pathology")
    print("C: Diseasology")
    print("D: Biology")
    answerTwo = input("")
else:
    print("Which United States of America unit of currency is worth 5 cents?")
    print("A: Penny")
    print("B: Nickel")
    print("C: Dime")
    print("D: Dollar")
    answerTwo = input("")
if answerTwo == "B":
    score +=1
    print("What year was the sodium lamp invented?")
    print("A: 18889")
    print("B: 1889")
    print("C: 1920")
    print("D: 1930")
    answerThree = input("")
else:
    print("What color are jeans?")
    print("A: Green")
    print("B: Orange")
    print("C: Blue")
    print("D: Red")
    answerThree = input("")
if answerThree == "C":
    score +=1
    print("Cemetaries contain:")
    print("A: Greaves")
    print("B: Churches")
    print("C: Cranberries")
    print("D: Graves")
    answerFour = input("")
else:
    print("What color are bananas when ripe?")
    print("A: Green")
    print("B: Blue")
    print("C: Red")
    print("D: Yellow")
    answerFour = input("")
if answerFour == "D":
    score +=1
    print("Which of the following characters is not in super smash bros?")
    print("A: Yoshi")
    print("B: Mewtwo")
    print("C: Steve")
    print("D: Walugi")
    answerFive = input("")
else:
    print("About how many bones are in the human body?")
    print("A: 1234")
    print("B: 140")
    print("C: 367")
    print("D: 200")
    answerFive = input("")
if answerFive == "D":
    score +=1
print("Your score was:", score)
if answer == "C":
    if answerTwo == "B":
        if answerThree == "C":
            if answerFour == "D":
                if answerFive == "D":
                    print("You got everything correct!")
if answer != "C":
    print("You got question 1 wrong.")
if answerTwo != "B":
    print("You got question 2 wrong.")
if answerThree != "C":
    print("You got question 3 wrong.")
if answerFour != "D":
    print("You got question 4 wrong.")
if answerFive != "D":
    print("You got question 5 wrong.")