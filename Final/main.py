global playerAtk
global playerDef
global inventory
global equipped

playerHP = 50
playerDef = 3
playerAtk = 5
inventory = ['Steel Shortsword', 'Tin Helmet']
equipped = ['Steel Shortsword', 'Tin Helmet']

def inventory():
    global playerAtk
    global playerDef
    global inventory
    global equipped
    while True:
        print("You have:")
        for item in inventory:
            print(item)
        print('Your equipped items are:')
        for item in equipped:
            print(item)
        playerChoice = input("Welcome to your inventory!\n1:Equip new items(You can have multiple armor pieces, but only one weapon at a time.)\n2:Unequip items\n3:Exit")
        if playerChoice == '1':
            while True:
                itemChoice = input("What item would you like to equip?")
                if itemChoice in equipped:
                    print("Sorry, you already have that equipped. Try again!")
                    continue
                elif itemChoice == 'Steel Shortsword':
                    playerAtk = 5
                    try: 
                        inventory.pop(inventory.index('Tick-Slaying Blade'))
                    except:
                        pass
                    try:
                        inventory.pop(inventory.index('Blade of Angst'))
                    except:
                        pass
                    break
                elif itemChoice == 'Tick-Slaying Blade':
                    playerAtk = 7
                    try: 
                        inventory.pop(inventory.index('Steel Shortsword'))
                    except:
                        pass
                    try:
                        inventory.pop(inventory.index('Blade of Angst'))
                    except:
                        pass
                    break
                elif itemChoice == 'Blade of Angst':
                    playerAtk = 10
                    try: 
                        inventory.pop(inventory.index('Tick-Slaying Blade'))
                    except:
                        pass
                    try:
                        inventory.pop(inventory.index('Steel Shortsword'))
                    except:
                        pass
                    break
                elif itemChoice == 'Tin Helmet' or itemChoice == 'Radical Boots' or itemChoice == 'Lemon Rind Chestplate':
                    playerDef += 5
                    break
                else:
                    print("Sorry, that's not a valid item. Try again.")
                    continue
        elif playerChoice == '2':
            while True:
                itemChoice = input("What would you like to unequip?")
                if itemChoice not in inventory:
                    print("You don't have that item. Try again")
                    continue
