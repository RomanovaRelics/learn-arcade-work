###LAB 12###

import random

class Room:
    """This class represents the rooms of the house."""
    def __init__(self, description, north, east, south, west, up, down):
        """This method sets up the variables in the object."""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down


class Item:
    """This class represents interactable items within the house."""
    def __init__(self, description, in_room, object_name):
        self.description = description
        self.in_room = in_room
        self.object_name = object_name

def main():

    room_list = []
    visited = []

    item_list = []


    item = Item("An old steamer chest sits in the corner. It has faded travel stickers from across the world dating\n"
                "from what seems like throughout the 1800s. It has a big heavy brass lock keeping the veritable\n"
                "time capsule treasure trove inside safe from the relentless wear of external years. You sense\n"
                "there is something important inside. Maybe you should look for a matching key.", 12, "chest")
    item_list.append(item)


    item = Item(" A red ball sits on the floor. It looks fun to play with but since there is a massive rat in the way,\n"
                "you don't try to use it. Maybe you could reach it if you find something to distract the rat.", 4, "ball")
    item_list.append(item)

    item = Item("Ol' Betsy catches on something shiny and metallic stuck in the sink drain. Unfortunately, that shiny item\n"
                "is being guarded by a spider. It doesn't seem mean per say but you have an aversion to it anyway.\n"
                "Maybe you could find something to move the spider out of the way. Preferably something long.", 7, "key")
    item_list.append(item)

    item = Item("There is a table with some suspiciously fresh cheese on it. You feel your stomach rumble\n"
                "involuntarily but you probably shouldn't eat it. Besides you have plenty of candy awaiting\n"
                "you in the coming days.\n"
                "Do you want to grab the cheese?", 5, "cheese")
    item_list.append(item)

    item = Item("You find a long thin spatula sitting alone in a jar on the rundown counter top. You think to\n"
                "yourself that it might be useful if you come across anything you want to keep at a distance.\n"
                "Do you want to grab the spatula?", 5, "spatula")
    item_list.append(item)

    item = Item("A beautiful doll sits at a small tea party set for three. You wonder if she knows\n"
                "the other party attendants will never arrive. You feel a sense of loneliness coming from the doll.\n"
                "A brief vision flashes in front of you. You recognize the doll dressed in tea party finery. She is being\n"
                "pushed in a delicate pram around the room by a happy little girl. You feel a sense of longing to be\n"
                "reunited with the small girl and take another promenade around in her pram. Your vision clears but the\n"
                "feeling of deep longing sticks with you. You can't help but want to ease the pain.", 9, "doll")
    item_list.append(item)

    item = Item(" A delicate pram sits by the foot of the pink bed. It seems sad such a beautiful pram should\n"
                "not have a passenger. You wonder what you could do about it.", 10, "pram")
    item_list.append(item)

    item = Item(" A gleaming pearl necklace catches your eye. You see a vision of an older woman clearly ill lying in a stately bed.\n"
                "You see her slowly take the necklace off of her delicate pale neck. Her thin hands tremble as she folds it into the\n"
                "hand of a young lady. You get a feeling that the old woman did not live for too long after this moment. You feel\n"
                "a sense of sadness overtake you. Did this young woman have to take care of the younger children\n"
                "after the death of the elder? She was barely a teenager. You see another flash of the young woman locking away the\n"
                "necklace in the attic as she looks out the small window bitterly looking at her old friends and the life she could\n"
                "have had. You feel the key was dropped somewhere dark and wet and regret loomed large after hiding away the necklace.\n"
                " Maybe you could help ease the regret of an old rash decision made in a moment of anger and help these feelings move on.", 12, "necklace")
    item_list.append(item)

    item = Item("You find an intricate jewelry box made of inlaid wood. The letters M A are carved into the top corner with a crude\n"
                "but delicate hand. Inside, you find a few assortments of earrings, rings and the like but there seems to be an\n"
                "empty space. You wonder what belonged here and why it was no longer in its comfortable velvet home.", 6, "box")
    item_list.append(item)

    item = Item("You see a worn photograph sitting in a plain frame on a long sidetable. It shows three children. One, taller\n"
                "than the others with dark brown hair. She looks old beyond her years like a child forced to grow up too soon.\n"
                "She wears a plain blue dress but what stands out the most is a simple but elegant string of pearls around her neck.\n"
                "She looks conflicted about wearing it as one hand gently reaches to touch them. You follow her other arm down to see\n"
                "a little girl smiling sadly up at you holding in the hand not holding the elder child's, an antique doll with all her might. \n"
                "You are a tad surprised the doll didn't break with how white the child's knuckles are. To her left is a small boy perhaps 6 years\n"
                "of age. He confidently wears a much too small sailors suit. In his hand is a shiny red ball. With the mischief glinting\n"
                "in his eyes, you have no doubt he and that ball caused many a ruckus.",1, "photograph")
    item_list.append(item)



    room = Room("You find yourself standing on the sagging porch of the notoriously\n"
                "haunted Maxwell place. Eerie creaking sounds come from deep within the house.\n"
                "Your friends stare at you from the safety of the sidewalk and gesture wildly\n"
                "for you to go inside. You make a mental note to avoid playing truth or dare\n"
                "the night before Halloween.\n"
                "\nYou can go North into the house from here or quit and never hear the end of it.", 1, None, None, None, None, None)
    room_list.append(room)


    room = Room("You enter the dark foyer. You whip out your trusty flashlight you\n"
                "affectionately call Ol' Betsy and look around. There is not much to see other\n"
                "than cobwebs and a grand dusty mirror. There are stairs to the second floor\n"
                "however they are damaged beyond repair. Guess you only have this floor to worry about!\n"
                "\nThere is an ominous archway directly in front of you to the North. \nYou can also go back South.\n", 2, None,0, None, None, None)
    room_list.append(room)


    room = Room("You enter the Southern end of the main hallway. You swing Ol' Betsy like\n"
                "a sword and jump in fear! Whew! It is just an old portrait hanging on the wall. You remind\n"
                "yourself that ghosts are not real and take in your options of where to go next.\n"
                "\nThere is an archway to the West. \n"
                "There is a dark door to the East. \n"
                "The hallway continues to the North.\n"
                "You can return South.", 3, 7, 1, 4, 8, None)
    room_list.append(room)


    room = Room("You are now in the Northern end of the main hallway. You hear what sounds like\n"
                "a creature scurrying nearby. You suddenly feel relieved your parents forced you to take \n"
                "that wilderness defense class in middle school. There is a window in front of you draped in\n"
                "heavy black curtains. \n"
                "\nThere is an archway to the West. \n"
                "There is an imposing door to the East.\n"
                "You can return South.", None, 6, 2, 5, None, None)
    room_list.append(room)


    room = Room("You pass through the archway to find a room with furniture covered in what were \n"
                "once white cloths now gray with a thick layer of dust. It seems even the furniture here \n"
                "is ghostly. \nThere is nowhere to go from here except back East.", None, 2, None, None, None, None)
    room_list.append(room)


    room = Room("You pass through the archway. A pungent smell of decay emanates from the ice-chest. \n"
                "There are some other things like an old stove and a few half opened cabinets. \n"
                "\nYou can go back East.\n"
                "You can go down to the basement.", None, 3, None,None, None, 8)
    room_list.append(room)


    room = Room("You pass through the imposing door to find a small but stately bedroom.\n"
                "A large four poster bed takes up most of the space. There is on old nightgown laid out on the bed waiting\n"
                "to be worn. It looks fresh compared to everything else in the room.\n"
                "\nYou can only go back West from here.", None, None, None,3, None, None)
    room_list.append(room)


    room = Room("You go through the dark door to a dingy bathroom. You think to yourself how lucky \n"
                "Ol' Betsy is to not have a sense of smell. You catch a glimpse of yourself in the mirror and \n"
                "swear you see someone behind you. A large spider sits in the broken porcelain sink.\n"
                "\nYou can only go West from here.", None, None, None, 2, None, None)
    room_list.append(room)


    room = Room("You enter a dim area with a worn concrete floor. There is a singular lightbulb\n"
                "hanging from the center of a cracked and creaking ceiling. Plain oak paneling surrounds the walls\n"
                "all the way up to your hip.\n"
                "You can go back upstairs to the south hall.\n"
                "You can venture through an archway to the East.\n"
                "You can walk through the archway to the South.", None, 9, 10, None, 2, None)
    room_list.append(room)


    room = Room("You enter the Eastern archway. The room has the same concrete floor as the stairwell room but noticeably dirtier.\n"
                "There are boxes and toys strewn about in large piles. There seems to be some method to the madness\n"
                "although not one you can easily discern. It almost seems like things were in the process of being sorted but\n"
                "the organizing party took a break for lunch and never came back.\n"
                "You can only go back West from here.", None, None, None, 8, None, None)
    room_list.append(room)


    room = Room("You enter dark room that clearly shows signs of being frequently used. There are two small beds on the far end of the room.\n"
                "One has a pink bedspread dulled only by the cacophony of dolls strewn across it. The other had\n"
                "a blue bedspread and was covered in model airplanes and various sports balls. Most of the room\n"
                "was taken up by the beds and the twin desks across from the door. Beautiful drawings covered both desks\n"
                "even falling to the floor in their avalanche of progress.\n"
                "You can go back North to the stairwell.\n"
                "You can go East through a small door between the two beds.", 8, 11, None, None, None, None)
    room_list.append(room)


    room = Room("A large rusty furnace takes up almost the entirety of the small room. For looking like it has not been used in\n"
                "decades, the room is as warm as if it were functioning on full power. You wonder how this could be as the\n"
                "rest of the house is cold with some small pockets seeming almost freezing.\n"
                "The only way you can go from here is back West.", 10, None, None, None, None, None)
    room_list.append(room)


    room = Room(" The attic is as dusty as you would except given the state of the rest fo the house. There are many\n"
                "things you can only describe as being 'attic-y' like old boxes, a dress form, a manikin head.\n"
                "You ponder quietly to yourself about why manikin heads always seem to turn up in creepy\n"
                "old attics where they don't belong.\n"
                "You cna only go back down from here.", None, None, None, None, None, 5)
    room_list.append(room)


    current_room = 0

    done = False
    ghost = False
    win = False

    moved = True
    found = False

    inventory = []


    while not done:

        if room_list[current_room] not in visited:
            visited.append(room_list[current_room])

        print()
        if moved == True:
            print(room_list[current_room].description)

        visit_check = len(visited)

        if visit_check >= 8:
            print("\nYou sense you have visited all the rooms on this floor of the house.\n")

        if ghost == False:
            ghost_chance = random.randint(1,10)

        else:
            ghost_chance = 10
            ghost = False

        if ghost_chance == 1 and room_list[current_room] != room_list[0]:
            print("\nYou see a full-bodied apparition in the middle of the room. It wears a long\n"
            "white dress. It seems unaware of your presence. You can try and engage it in conversation (c),\n"
            ",quietly leave it to its affairs (l), or run away screaming and never come back (r).")
            ghost = True

        else:
            ghost = False

        if ghost == False:
            answer = input("\nWhat do you want to do? You can move using a cardinal direction \"east\" etc. or \"up\" and \"down\".\n "
"You can look for items. Check inventory. Or quit.")
            answer = answer.upper()

        else:
            answer = input("\nWhat do you want to do?")
            answer = answer.upper()

        if answer == "N" or answer == "NORTH":
            print()
            print("\nYou went North.")
            next_room = room_list[current_room].north

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True


        if answer == "E" or answer == "EAST":
            print()
            print("\nYou went East.")
            next_room = room_list[current_room].east

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True

        if answer == "S" or answer == "SOUTH":
            print()
            print("\nYou went South.")
            next_room = room_list[current_room].south

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True

        if answer == "W" or answer == "WEST":
            print()
            print("\nYou went West.")
            next_room = room_list[current_room].west

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True

        if answer == "U" or answer == "UP":
            print()
            print("\nYou went up the ladder.")
            next_room = room_list[current_room].up

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True

        if answer == "D" or answer == "DOWN":
            print()
            print("\nYou went down the stairs.")
            next_room = room_list[current_room].down

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")
                moved = False

            else:
                current_room = next_room
                moved = True

        if answer == "LOOK":
            moved = False
            found = False
            print()
            print("You look around for anything of interest...")
            for i in item_list:
                if i.in_room == current_room:
                    found = True
                    print("FOUND: ",i.object_name.upper())
                    print(i.description)
                    print()
                    inventory.append(i)
            if found == False:
                print("You find nothing.")

        if answer == "I" or answer == "INVENTORY":
            moved = False
            print()
            print("INVENTORY:")
            for i in inventory:
                print("• ", i.object_name)

        if answer == "USE":
            moved = False
            print()
            answer = input("Use what?")
            answer = answer.upper()
            if answer == "BALL":
                #work in progress
                if current_room == 10:
                    print("You roll the ball between your feet in the children's bedroom. You accidentally kick it too far\n"
                          "and it disappears into a dark corner. After a long moment, the ball reappears rolling back at you\n"
                          "at an unusual angle. You never even heard the ball hit the wall.\n"
                          "You hear some excited giggling coming from somewhere in the corner of the room.\n"
                          "You feel a sense of happiness and thankfulness wash over you. You feel like you have done\n"
                          "the right thing.")
                else:
                    print("You can't use that here.")

            if answer == "KEY":
                if current_room == 12:
                    print("You slide the key into the bronze lock on the old chest. Turning it gingerly, you hear a small\n"
                          "click. The lid pops open and you lift it up to reveal some old papers, photographs, and a light\n"
                          "coating of dust. You notice a lump in the corner underneath some faded newspaper. You, curious\n"
                          "as ever, investigate the bump and find a pearl necklace. You can tell it is old but you can see\n"
                          "your face gleaming in the cream colored pearls. A wash of pain and regret washes over you as you\n"
                          "hold the necklace in your hands. You feel like you can do something with this necklace that will\n"
                          "relieve some of this anguish. You take it with you.")
                else:
                    print("You can't use that here.")

            if answer == "FOOD":
                if current_room == 4:
                    print("You place the food on the ground a few feet away from the ball. The rat that was guarding\n"
                          "it excitedly breaks out into a run for the stinky morsel. Looks like you can get the ball now.")
                else:
                    print("You can't use that here.")

            if answer == "SPATULA":
                if current_room == 7:
                    print("You slowly extend the spatula towards the spider guarding the shiny object. You want to close\n"
                          "your eyes but you think it would probably be best to keep an eye on the enemy. With a little\n"
                          "encouragement, the spider crawls onto the spatula and you put the whole thing in the tub and close\n"
                          "the curtain. You tell yourself it is just because you are giving the spider privacy but it helps\n"
                          "to have an extra barrier between you. You fish a key out of the sink. This could be useful.")
                else:
                    print("You can't use that here.")

            if answer == "DOLL":
                if current_room == 10:
                    print(" You place the doll in the stroller. You feel a happy sensation overcome you. You hear joyous mumbling\n"
                          "and you step back suddenly as the stroller moves slightly back and forth. You feel a small tug on your jeans\n"
                          "and look down to see a little tea party hat fit for a lovely doll. You pick it up (probably against your\n"
                          "better judgement) and place it on the head of the doll in the stroller. You feel lighter like you helped\n"
                          "someone.")
                else:
                    print("You can't use that here.")

            if answer == "NECKLACE":
                if current_room == 6:
                    print("You take the necklace out of your pocket. You feel like you should ")

        if answer == "Q" or answer == "QUIT":
            moved = False
            print()
            answer = input("\nAre you sure you want to leave? You will be forever known as the scaredy-cat.")
            answer = answer.upper()

            if answer == "Y" or answer == "YES":
                done = True
                win = False

            else:
                done = False

        if answer == "C" and ghost == True:
            print()
            print("\nYou talk to the ghost. It turns to look at you before vanishing.")

        elif answer == "R" and ghost == True:
            print()
            print("\nYou run away.")
            done = True
            win = False

        elif ghost == True:
            print()
            print("\nYou decide you are not being paid enough to deal with an ACTUAL ghost. Come to think of it, you\n"
                  "aren't getting paid at all... Maybe truth or dare needs to up its stakes and maybe you should just\n"
                  "pretend you don't see it.")

        if room_list[current_room] == room_list[0] and visit_check >= 8:
            done = True
            win = True

        elif room_list[current_room] == room_list[0] and visit_check < 8:
            print("\nYou have not investigated every room of the house. If you quit now you will leave\n"
                  "nooks and crannies shrouded in mystery.")

    if win == True:
        print()
        print("\nYou managed to survive exploring the old Maxwell place. Your friends will\n"
              "always remember your bravery. \" Don't forget I helped too.\" you hear coming from\n"
              "Ol' Betsy. Maybe you should get that checked out. Your friends chant your name\n"
              "and sing your praises as you saunter away from the decrepit house.")

    else:
        print("\nYou run outside screaming and your friends point and laugh. You will\n"
        "NEVER live this down. You get used to the verbal and physical pokes\n"
        "from your friends as you all walk down the road. At least Ol' Betsy\n"
        "understands. \"Wimp\" you hear quietly from your palm. You look around\n"
        "guess no-one else heard that. Maybe you ARE a scaredy-cat. All you know is\n"
        "you never want to go to the Old Maxwell place again... And maybe you should get Ol'\n"
        "Betsy checked for spirits.")

main()
