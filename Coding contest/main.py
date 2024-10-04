#Text adventure
hasTorch = False
playing = True
def main():
    print("Hello. You are Frindldoodle, a tiny gnome, and knight from the kingdom of Tisboonadon.\n A very peaceful place, Tisboonadon has been a thriving metropolis for years. Until it all went wrong.")
    print("As of last month, the central well has been strange. When gnomes try to pull up water from it, it comes out thick and dark.\n Now normally this wouldn't be a problem, but this is one of the biggest wells in Tisboonadon, and the water being retrieved is now acidic and poisonous.")
    print("In fact, recently one of your neighbors, Mr. Gloomglock, fell into the well, and his agonized screaming was heard for three days as he presumably disolved in some\n of the water.")
    choice = input("Because of this threat, the King has dispatched you to the well to find and fix the problem.\n You stand at the edge of the well.\n Press 1 to run away\n or press 2 to enter the well:")
    if choice == "1":
        print("You, being the noble knight you are, run away from the well with your tail between your legs.\n You continue to run and scream in terror until you arrive at the nearby town of Grandosfern, where you then collapse and die from exaustion.\n Ending 1/4 obtained.")
        exit()
    elif choice == "2":
        print("As you stare into the well, a feling of dread seeps into your very soul. the well looks like the maw of some giant creature, ready to swallow you whole.\n You enter the well.")
        choice = input("When you reach the bottom of the ladder, you find yourself in a dank, moldy room lit by a single torch.\n The only thing of note is the open doorway leading to a hallway,\n and a few small puddles of black acid.\n Press 1 to take the torch\n or press 2 to enter the hallway.")
        if choice == "1":
            print("You grab the torch.")
            hasTorch = True
        print("You enter the hallway. It's about 3 meters wide, and half of the room is taken up by a river of black sludge.\n As you walk towards the next doorway, part of the sludge begins to bubble.\n A bulge appears, growing larger as though something is trying to escape. the bubble pops, revealing a withered figure. You soon recongnize it as Mr. Gloomglock.\n")
        print("It groans and stands up straight, dripping goo from its wilted form. The creature wades towards the dry section of the hallway and pulls itslef on.\n It looks at you, and you realize that you aren't getting out of this without a fight.")
        choice = input("You are faster than the creature. What do you do? You can\n press 1 to swing your sword\n press 2 to guard\n or press 3 to attempt to run past it towards the exit.")
        if choice == "1":
            print("You strike the amalgamation with your blade!\n It hits back, singeing your flesh when it's foul cloak of acid touches your chest.\n You hit back with another strike, shattering its ribcage.\n It gurgles as it disolves into itself, leaving nothing but a puddle behind.")
        elif choice == "2":
            print("You ready yourself for a strike, but this thing is like nothing you've faced before. When it hits you, your armor is useless, and you flesh is eaten away by the acid. It hits again, this time hitting you in your head, and shooting pain")
            
        elif choice == "3":
    else:
        print("Sorry, you entered something wrong. Try again.")

main()