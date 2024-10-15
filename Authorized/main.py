admin = "Luke"
authorized = ["Barbie", "Shrimp", "Jim", "Mr. Gloomglock", "Liam", "Garette", "Mr. C", "Jorbidanan"]
usrName = input("What is your name?:")
for item in authorized:
    if usrName == admin:
        print('Welcome, Admin.')
        exit()
    elif usrName == item:
        print("Access granted.")
        exit()
print("Access Denied.")
