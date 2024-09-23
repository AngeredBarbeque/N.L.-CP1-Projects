#Nicholas Larsen Pig Latin converter.

def piggyMode(word):
    firstLet = word[0]+"ay"
    length = len(word)
    N = length-1
    word = word[length-N:]
    return(word + firstLet)

print(piggyMode(word=input("What word would you like to convert?")))