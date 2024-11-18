userList = []
input("Btw what's your race?")
while True:
    userList.append(int(input("Please enter a number to add to your list.")))
    for index, item in enumerate(userList):
        print(index + 1, end = "")
        for i in range(item):
            print("*", end = "")
        print("")