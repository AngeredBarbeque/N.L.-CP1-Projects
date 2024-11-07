hp = 10
dex = 2
str = 2
int = 2
print("Welcome to a character creator!")
race = input('Please choose a race.\nA:Orc\nB:Snake\nC:Inflatable Punching Bag\nD:Humanoid Bird\nE:Average Human\n')
if race == 'A':
    str += 2
    hp += 10
    int -=1
    raceName = 'Orcs'
if race == 'B':
    dex += 2
    int += 1
    str -=1
    raceName = 'Snakes'
if race == 'C':
    hp += 20
    dex -=1
    str +=1
    raceName = 'Inflatable Punching Bags'
if race == 'D':
    int += 2
    dex += 1
    hp -= 5
    raceName = 'Humanoid Birds'
if race == 'E':
    hp += 5
    dex += 1
    str += 1
    int += 1
    raceName = 'Average Humans'
clss = input('Please choose a class\nA:Barbarian\nB:Rogue\nC:Knight\nD:Wizard\nE:Bard\n')
if clss == 'A':
    str += 2
    hp += 5
    int -=1
    className = 'Barbarian'
if clss == 'B':
    dex +=2
    int += 1
    str -= 1
    className = 'Rogue'
if clss== 'C':
    hp += 20
    str += 1
    dex -= 1
    className = 'Knight'
if clss == 'D':
    int += 3
    className = 'Wizard'
if clss == 'E':
    dex += 1
    str += 1
    int += 1
    className = 'Bard'
name = input("Please enter a character name:")
print('You are', name, 'of the', raceName + '. You are a', className + '.')
print('You have', dex, 'dexterity,', str, 'strength,', int, 'intelligence, and', hp, 'health points.')