#Nicholas Larsen

plainText = input("What is your phrase?: ")
shift= int(input("How much would you like to shift it?"))
cipherText = ""
def conversion(shift, plainText, cipherText):
    for c in plainText.lower():
        c2 = ord(c) + shift
        cipherText += chr(c2)
    return cipherText
print(plainText)
print(conversion(shift, plainText, cipherText))