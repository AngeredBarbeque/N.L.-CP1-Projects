#Pig latin
def piggyMode(word):#Pig latin convert
    firstLet = word[0]+ "ay"#adds ay
    word = word[1:]    #takes rest of word
    return(word + firstLet).title()#returnz the pig mode word

print(piggyMode(word=input("What word would you like to convert?"))) #takes the input