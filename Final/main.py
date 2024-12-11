import random
global playerHP
global playerAtk
global playerDef
global inventory
global equipped

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
                itemChoice = input("\nWhat item would you like to equip?\nChoose:").title()
                if itemChoice in equipped:
                    print("\nSorry, you already have that equipped. Try again!")
                    break
                if itemChoice not in inventory:
                    print("\nSorry, that's not a valid item.")
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
                    print("\nSorry, that's not a valid item. Try again.")
                    break
        elif playerChoice == '2':
            while True:
                itemChoice = input("What would you like to unequip?")
                if itemChoice not in inventory:
                    print("\nYou don't have that item. Try again.")
                    break
                elif itemChoice not in equipped:
                    print("\nThat item isn't equipped!")
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
            print("\nGoodbye!")
            break
        else:
            print("\nWrong number, nincompoop.")
def combat(enemyHP, enemyAtk):
    global playerAtk
    global playerDef
    global inventory
    global playerHP
    while True:
        playerChoice = input('\nWhat would you like to do?\n1:Attack\n2:Defend\n3:Item\nChoose:')
        if playerChoice == '1':
            enemyHP -= playerAtk
        elif playerChoice == '2':
            if enemyCharge == True:
                enemyCharge = False
            continue
        elif playerChoice == '3':
                while True:
                    print("\nYou have:")
                    for item in inventory:
                        print(item)
                    itemChoice = input("\nWhat item do you want to use?\nChoose:").title
                    if itemChoice == 'Healing Potion':
                        inventory.pop(inventory.index(itemChoice))
                        playerHP = 50
                        break
                    elif itemChoice == 'Amulet of Rage':
                        inventory.pop(inventory.index(itemChoice))
                        enraged = 2
                        playerAtk += 3
                        break
                    else:
                        print("\nThat item isn't valid.")
                        continue
        else:
            print("\nWrong number, try again.")
        enemyChoice = random.randint(1,2)
        if enemyChoice == 1:
            if enemyCharge == True:
                playerHP -= (enemyAtk*2)-playerDef
            else:
                playerHP -= enemyAtk-playerDef
        elif enemyChoice == 2:
            enemyCharge = True
        if playerHP == 0:
            return "Failed"
        elif enemyHP == 0:
            return "Won"
        else:
            continue
def death():
    print("\nYou failed your mission and died. D:")
    exit()
def roomOne():
    print("\n!!INSERT STORY INTRO HERE!!")
    print("\n!!INSERT ROOM DESCRIPTION HERE!!")
    while True:
        playerChoice = input("\nWhat would you like to do?\n1:Go straight\n2:Go to the right\n3:Access inventory\nChoose:")
        if playerChoice == '1':
            roomTwo(inventory)
        elif playerChoice == '2':
            pass
            #roomThree()
        elif playerChoice == '3':
            inventoryChoices()
        else:
            print("\nSorry, try again.")
def roomTwo(inventory):
    print("\n!!BATHROOM!!")
    if potionGot == False:
        print("\nBefore you can decide what to do next, you spot a potion in the medicine cabinet!\nHealing Potion obtained!")
        inventory.append('Healing Potion')
        potionGot = True
    playerChoice = input("\nWhat would you like to do?\n1:Go straight\n2:Go right\n3:Access inventory\nChoose:")
    if playerChoice == '1':
        pass
        #roomFour()
    elif playerChoice == '2':
        pass
        #roomFive()
    elif playerChoice == '3':
        inventoryChoices()
    else:
        print("\nSorry, try again.")
def roomThree():
    print("\n!!TICKS!!")
    outcome = combat(25, 10)
    if outcome == 'Failed':
        death()
    elif outcome == 'Won':
        print("\n!!TICKS DEAD!!")
        print("\nYou grab a sword!!!CONTINUE HERE!!!")
roomOne()