#Nicholas Larsen
shopList = []
while True:
    choice = input("This is your shopping list manager.\n What would you like to do?\n Press 1 to add an item\n Press 2 to remove an item\n Press 3 to leave")
    if choice == "1":
        item = input("What item would you like to add to your list?")
        shopList.append(item)
    elif choice == "2":
        item = input("What item would you like to remove from your list?")
        shopList.remove(item)
    elif choice == "3":
        print("Goodbye!")
        break
    print("This is your list\n", shopList)