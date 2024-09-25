#Nicholas Larsen

what = input("would you like to convert, or unconvert?")
plainText = input("What is your phrase?: ")
shift= int(input("How much would you like to shift it?"))

cipherText = ""
def conversion(shift, plainText, cipherText):
    for c in plainText.lower():
        c2 = ord(c) + shift
        cipherText += chr(c2)
    return cipherText

def unconversion(shift, cipherText, plainText):
    for c in cipherText.lower():
        c2 = ord(c) - shift
        plainText += chr(c2)
    return plainText

print(plainText)
if what == "convert":
    print(conversion(shift, plainText, cipherText))
if what == "unconvert":
    print(unconversion(shift, plainText, cipherText))