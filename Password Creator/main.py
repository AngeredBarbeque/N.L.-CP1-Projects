#Nicholas Larsen
passwordValid = False
eightChars = False
hasNum = False
hasSpec = False
numList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specCharList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "{", "}", "[", "]", "|", ":", ";", "<", ">", ",", ".", "/", "?", "`", "~"]
while passwordValid == False:
    password = input("Please enter a password with 8 characters, 1 number, and 1 special character.")
    if len(password) < 8:
        print("Your password is too short.")
    else:
        eightChars = True
    for char in password:
        if char in numList:
            hasNum = True
    if hasNum == False:
        print("Your password doesn't have a number.")
    for char in password:
        if char in specCharList:
            hasSpec = True
    if hasSpec == False:
        print("Your password doesn't have a special character.")
    
    

