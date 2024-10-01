#Nicholas Larsen Pig Latin converter.

def piggyMode(word):
    firstLet = word[0]+ "ay"
    word = word[1:]
    return(word + firstLet).title()

print(piggyMode(word=input("What word would you like to convert?")))

