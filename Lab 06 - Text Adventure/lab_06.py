import random

class Room:
    """This class represents the rooms of the house."""
    def __init__(self, description, north, east, south, west):
        """This method sets up the variables in the object."""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():

    room_list = []
    visited = []

    room = Room("You find yourself standing on the sagging porch of the notoriously\n"
                "haunted Maxwell place. Eerie creaking sounds come from deep within the house.\n"
                "Your friends stare at you from the safety of the sidewalk and gesture wildly\n"
                "for you to go inside. You make a mental note to avoid playing truth or dare\n"
                "the night before Halloween.\n"
                "\nYou can go North into the house from here or quit and never hear the end of it.", 1, None, None, None)

    room_list.append(room)
    room = Room("You enter the dark foyer. You whip out your trusty flashlight you\n"
                "affectionately call Ol' Betsy and look around. There is not much to see other\n"
                "than cobwebs and a grand dusty mirror. There are stairs to the second floor\n"
                "however they are damaged beyond repair. Guess you only have this floor to worry about!\n"
                "\nThere is an ominous archway directly in front of you to the North. \nYou can also go back South.\n", 2, None,0, None)

    room_list.append(room)
    room = Room("You enter the Southern end of the main hallway. You swing Ol' Betsy like\n"
                "a sword and jump in fear! Whew! It is just an old portrait hanging on the wall. You remind\n"
                "yourself that ghosts are not real and take in your options of where to go next.\n"
                "\nThere is an archway to the West. \n"
                "There is a dark door to the East. \n"
                "The hallway continues to the North.\n"
                "You can return South.", 3, 7, 1, 4)

    room_list.append(room)
    room = Room("You are now in the Northern end of the main hallway. You hear what sounds like\n"
                "a creature scurrying nearby. You suddenly feel relieved your parents forced you to take \n"
                "that wilderness defense class in middle school. There is a window in front of you draped in\n"
                "heavy black curtains. \n"
                "\nThere is an archway to the West. \n"
                "There is an imposing door to the East.\n"
                "You can return South.", None, 6, 2, 5)

    room_list.append(room)
    room = Room("You pass through the archway to find a room with furniture covered in what were \n"
                "once white cloths now gray with a thick layer of dust. It seems even the furniture here \n"
                "is ghostly. \nThere is nowhere to go from here except back East.", None, 2, None, None)

    room_list.append(room)
    room = Room("You pass through the archway. A pungent smell of decay emanates from the ice-chest. \n"
                "There is a table with some suspiciously fresh food on it. Has someone or some... thing been living here?\n"
                "There are some other things like an old stove and a few half opened cabinets. \n"
                "\nThe only way you can go is back East.", None, 3, None,None)

    room_list.append(room)
    room = Room("You pass through the imposing door to find a small but stately bedroom.\n"
                "A large four poster bed takes up most of the space. There is on old nightgown laid out on the bed waiting\n"
                "to be worn. It looks fresh compared to everything else in the room.\n"
                "\nYou can only go back West from here.", None, None, None,3)

    room_list.append(room)
    room = Room("You go through the dark door to a dingy bathroom. You think to yourself how lucky \n"
                "Ol' Betsy is to not have a sense of smell. You catch a glimpse of yourself in the mirror and \n"
                "swear you see someone behind you. A large spider sits in the broken porcelain sink.\n"
                "\nYou can only go West from here.", None, None, None, 2)
    room_list.append(room)

    current_room = 0

    done = False
    ghost = False
    win = False

    while not done:

        if room_list[current_room] not in visited:
            visited.append(room_list[current_room])

        print()
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
            answer = input("\nWhat direction do you want to go in? ")
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

            else:
                current_room = next_room

        if answer == "E" or answer == "EAST":
            next_room = room_list[current_room].east

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")

            else:
                print()
                print("\nYou went East.")
                current_room = next_room

        if answer == "S" or answer == "SOUTH":
            print()
            print("\nYou went South.")
            next_room = room_list[current_room].south

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")

            else:
                current_room = next_room

        if answer == "W" or answer == "WEST":
            print()
            print("\nYou went West.")
            next_room = room_list[current_room].west

            if next_room is None:
                print("\nSomething tells you that you can't go that way.")

            else:
                current_room = next_room

        if answer == "Q" or answer == "QUIT":
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
