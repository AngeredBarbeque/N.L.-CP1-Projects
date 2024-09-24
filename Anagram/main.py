#nicholas larsen anagram creator

import random
num = 0
inputWord = input("What would you like to mix up?: ")
def mixUp(word):
    listWord = list(word.lower())
    random.shuffle(listWord)
    anagram = "".join(listWord).title()
    return anagram
print(inputWord.title())
while num <5:
    print(mixUp(inputWord))
    num += 1

