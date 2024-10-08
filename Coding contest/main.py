#Text adventure
hasTorch = False
def main():
    print("Hello. You are Frindldoodle, a tiny gnome, and knight from the kingdom of Tisboonadon.\n A very peaceful place, Tisboonadon has been a thriving metropolis for years. Until it all went wrong.")
    print("As of last month, the central well has been strange. When gnomes try to pull up water from it, it comes out thick and dark.\n Now normally this wouldn't be a problem, but this is one of the biggest wells in Tisboonadon, and the water being retrieved is now acidic and poisonous.")
    print("In fact, recently one of your neighbors, Mr. Gloomglock, fell into the well, and his agonized screaming was heard for three days as he presumably disolved in some\n of the water.")
    choice = input("Because of this threat, the King has dispatched you to the well to find and fix the problem.\n You stand at the edge of the well.\n Press 1 to run away\n or press 2 to enter the well:")
    if choice == "1":
        print("You, being the noble knight you are, run away from the well with your tail between your legs.\n You continue to run and scream in terror until you arrive at the nearby town of Grandosfern, where you then collapse and die from exaustion.\n Ending 1/3 obtained.")
        exit()
    elif choice == "2":
        print("As you stare into the well, a feeling of dread seeps into your very soul. the well looks like the maw of some giant creature, ready to swallow you whole.\n You enter the well.")
        choice = input("When you reach the bottom of the ladder, you find yourself in a dank, moldy room lit by a single torch.\n The only thing of note is the open doorway leading to a hallway,\n and a few small puddles of black acid.\n Press 1 to take the torch\n or press 2 to enter the hallway.")
        if choice == "1":
            print("You grab the torch.")
            hasTorch = True
        print("You enter the hallway. It's about 3 meters wide, and half of the room is taken up by a river of black sludge.\n As you walk towards the next doorway, part of the sludge begins to bubble.\n A bulge appears, growing larger as though something is trying to escape. The bubble pops, revealing a withered figure. You soon recongnize it as Mr. Gloomglock.")
        print("It groans and stands up straight, dripping goo from its wilted form. The creature wades towards the dry section of the hallway and pulls itself on to dry land.\n It looks at you, and you realize that you aren't getting out of this without a fight.")
        choice = input("You are faster than the creature. What do you do? You can\n press 1 to swing your sword\n press 2 to guard\n or press 3 to attempt to run past it towards the exit.")
        if choice == "1":
            print("You strike the amalgamation with your blade!\n It hits back, singeing your flesh when its foul cloak of acid touches your chest.\n You hit back with another strike, shattering its ribcage.\n It gurgles as it disolves into itself, leaving nothing but a puddle behind.")
            choice = input("You walk into the next room. this room contains nothing of interest, however it splits into two halls.\n Press 1 to go left\n Press 2 to go right.")
            if choice == "2":
                print("You find yourself in another room. this room has fungi growing all over the walls and a locked gate. It seems you will have to go left.")
            choice = input("You find yourself in another dark room. As you stumble around in the darkness, you find two levers.\n Press 1 to pull the right lever\n press 2 to pull the right lever.")
            if choice == "1":
                print("The walls seem to groan as you pull the lever. Before you can react, the ceiling opens, dropping a pile of large rocks onto you, instantly crushing all of your bones.\n You are dead.")
                exit()
            if choice == "2":
                print("As you pull the lever, you hear creaking nearby. When you finish pulling the lever, you walk to the room on the right. There is now a open doorway to the next room.")
                print("As you walk to the next room, you find yourself in a large, circular room. There's a pit of acid in the center, but nothing else of interest. Then, the pit begins to gurgle. This again. A thin, long leg emerges from the pit, followed by 7 more.\n Great. It's a giant spider. What will you do?:\n")
                choice == input("Press 1 to use your sword\n Press 2 to use your shield to guard\n")
                if choice == "1":
                    print("You prepare to strike the creature, but before you can, it raises one leg, and strikes you straight through your chest. As you stumble to the floor, the acid eating away at your internal organs,\n you see the head of the spider lean down towards you, its jaws open before you black out.\n You have died.")
                    exit()
                elif choice == "2":
                    print("In an effort to be safe, you raise your shield. The monster strikes your shield, puncturing it like nothing. Luckily it didn't hit you.\n You raise your sword, and drive the blade into the skull of the creature. The creature shrieks and writhes.\n It screeched in agony as it melted and seeped into the floor. As you prepare to leave, you notice something black and glistening on the ground.\n You feel drawn to it and pick it up. It seems to be the heart of that creature. Before you can admire it further, the ceiling begins to crumble.")
                    if hasTorch == True:
                        choice == input("what do you do?\n Press 1 to run outside\n or press 2 to burn the heart with your torch.")
                        if choice == "1":
                            print("You run towards the ladder, and scamper up as the well collapses. You have escaped and destroyed the creature!\n...\n...\n...\n...\n...\n2 Months Later...\nYou kept the heart of the creature on a trophy rack to prove your victory. But one day, you come home, only to find you have no home.\n The heart has grown and the same dark goo that had absorbed Mr. Gloomglock takes you. You have spread the corruption.\n Ending 2/3.")
                        elif choice == "2":
                            print("You stare at the heart, and know what you must do. You take out your torch, and you drop the heart and the torch to the floor.\n Fire consumes the heart. Then, the ceiling shakes, and everything goes dark. You have truly destroyed the corruption. Ending 3/3.")
                    elif hasTorch == False:
                        choice == input("what do you do?\n Press 1 to run outside")
                        if choice == "1":
                            print("You run towards the ladder, and scamper up as the well collapses. You have escaped and destroyed the creature!\n...\n...\n...\n...\n...\n2 Months Later...\nYou kept the heart of the creature on a trophy rack to prove your victory. But one day, you come home, only to find you have no home.\n The heart has grown and the same dark goo that had absorbed Mr. Gloomglock takes you. You have spread the corruption.\n Ending 2/3.")
                    
        elif choice == "2":
            print("You ready yourself for a strike, but this thing is like nothing you've faced before. When it hits you, your armor is useless, and your flesh is eaten away by the acid. It hits again, this time hitting your head, and shooting pain splits your mind in two.\n You have died.")
            exit()
        elif choice == "3":
            print("You sheath your sword and dash past the creature. Unfortunately, it noticed you and vomits boiling acid on your back when you run past it. The acid is powerful enough that you stumble to the floor before you can reach the exit. You have died.")
    else:
        print("Sorry, you entered something wrong. Try again.")

main()