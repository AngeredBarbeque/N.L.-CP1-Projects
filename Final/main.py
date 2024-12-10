global playerHP
global playerAtk
global playerDef
global inventory
global equipped
global enemyHP
global enemyAtk
playerHP = 50
playerDef = 5
playerAtk = 5
inventory = ['Steel Shortsword', 'Tin Helmet', 'Blade Of Angst']
equipped = ['Steel Shortsword', 'Tin Helmet']

def inventoryChoices():
    global playerAtk
    global playerDef
    global inventory
    global equipped
    while True:
        print("\nYou have:")
        for item in inventory:
            print(item)
        print('\nYour equipped items are:')
        for item in equipped:
            print(item)
        playerChoice = input("\nWelcome to your inventory!\n1:Equip new items(You can have multiple armor pieces, but only one weapon at a time.)\n2:Unequip items\n3:Exit\nChoose:")
        if playerChoice == '1':
            while True:
                itemChoice = input("What item would you like to equip?").title()
                if itemChoice in equipped:
                    print("Sorry, you already have that equipped. Try again!")
                    break
                if itemChoice not in inventory:
                    print("Sorry, that's not a valid item.")
                    break
                elif itemChoice == 'Steel Shortsword':
                    playerAtk = 5
                    try: 
                        equipped.pop(equipped.index('Tick Slaying Blade'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Blade Of Angst'))
                    except:
                        pass
                    equipped.append("Steel Shortsword")
                    break
                elif itemChoice == 'Tick Slaying Blade':
                    playerAtk = 7
                    try: 
                        equipped.pop(equipped.index('Steel Shortsword'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Blade Of Angst'))
                    except:
                        pass
                    equipped.append("Tick Slaying Blade")
                    break
                elif itemChoice == 'Blade Of Angst':
                    playerAtk = 10
                    try: 
                        equipped.pop(equipped.index('Tick Slaying Blade'))
                    except:
                        pass
                    try:
                        equipped.pop(equipped.index('Steel Shortsword'))
                    except:
                        pass
                    equipped.append("Blade Of Angst")
                    break
                elif itemChoice == 'Tin Helmet' or itemChoice == 'Radical Boots' or itemChoice == 'Lemon Rind Chestplate':
                    playerDef += 5
                    equipped.append(itemChoice)
                    break
                else:
                    print("Sorry, that's not a valid item. Try again.")
                    break
        elif playerChoice == '2':
            while True:
                itemChoice = input("What would you like to unequip?")
                if itemChoice not in inventory:
                    print("You don't have that item. Try again")
                    break
                elif itemChoice not in equipped:
                    print("that item isn't equipped!")
                    break
                elif itemChoice == 'Steel Shortsword':
                    playerAtk -= 4
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Tick Slaying Blade':
                    playerAtk -= 6
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Blade Of Angst':
                    playerAtk -= 9
                    equipped.pop(equipped.index(itemChoice))
                    break
                elif itemChoice == 'Tin Helmet' or itemChoice == 'Radical Boots' or itemChoice == 'Lemon Rind Chestplate':
                    playerDef -= 5
                    equipped.pop(equipped.index(itemChoice))
                    break
        elif playerChoice == '3':
            print("Goodbye!")
            break
        else:
            print("Wrong number, nincompoop.")
def combat():
    global playerAtk
    global playerDef
    global inventory
    global playerHP
    while True:
        playerChoice = input('What would you like to do?\n1:Attack\n2:Defend\n3:Item')
        if playerChoice == '1':
            enemyHP - playerAtk
        elif playerChoice == '2':
            if enemyCharge == True:
                enemyCharge = False
            continue
        elif playerChoice == '3':
                while True:
                    itemChoice = input("CONTINUE CODE FROM HERE!!!")