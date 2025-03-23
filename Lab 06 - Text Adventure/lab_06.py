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
    room = Room("You find yourself standing on the sagging porch of the notoriously"
                "haunted Maxwell place. Eerie creaking sounds come from deep within the house.\n"
                "Your friends stare at you from the safety of the sidewalk and gesture wildly\n"
                "for you to go inside. You make a mental note to avoid playing truth or dare\n"
                "the night before Halloween.\n"
                "You can go North into the house from here or quit and never hear the end of it.", 1, None, None, None)
    room_list.append(room)
    room = Room("You enter the dark foyer. You whip out your trusty flashlight you\n"
                "affectionately call Ol' Betsy and look around. There is not much to see other\n"
                "than cobwebs and a grand dusty mirror. There are stairs to the second floor\n"
                "however they are damaged beyond repair. Guess you only have this floor to worry about!\n"
                "There is an ominous archway directly in front of you to the North.\n", 2, None,None, None)
    room_list.append(room)
    room = Room("You enter the Southern end of the main hallway. You swing Ol' Betsy like\n"
                "a sword and jump in fear! Whew! It is just an old portrait hanging on the wall. You remind\n"
                "yourself that ghosts are not real and take in your options of where to go next.\n"
                "There is an archway to the West. \n"
                "There is a dark door to the East. \n"
                "The hallway continues to the North.", 3, 7, 1, 4)
    room_list.append(room)
    room = Room("You are now in the Northern end of the main hallway. You hear what sounds like\n"
                "a creature scurrying nearby. You suddenly feel relieved your parents forced you to take \n"
                "that wilderness defense class in middle school. There is a window in front of you draped in\n"
                "heavy black curtains. \n"
                "There is an archway to the West. \n"
                "There is an imposing door to the East.", None, 6, 2, 5)
    room_list.append(room)
    room = Room("You pass through the archway to find a room with furniture covered in what were \n"
                "once white cloths now gray with a thick layer of dust. It seems even the furniture here \n"
                "is ghostly. There is nowhere to go from here except back East.", None, 2, None, None)
    room_list.append(room)
    room = Room("You pass through the archway. A pungent smell of decay emanates from the ice-chest. \n"
                "There is a table with some suspiciously fresh food on it. Has someone or some... thing been living here?\n"
                "There are some other things like an old stove and a few half opened cabinets. \n"
                "The only way you can go is back East.", None, 3, None,None)
    room_list.append(room)
    room = Room("You pass through the imposing door to find a small but stately bedroom.\n"
                "A large four poster bed takes up most of the space. There is on old nightgown laid out on the bed waiting\n"
                "to be worn. It looks fresh compared to everything else in the room.\n"
                "You can only go back West from here.", None, None, None,3)
    room_list.append(room)
    room = Room("You go through the dark door to a dingy bathroom. You think to yourself how lucky \n"
                "Ol' Betsy is to not have a sense of smell. You catch a glimpse of yourself in the mirror and \n"
                "swear you see someone behind you. A large spider sits in the broken porcelain sink.\n"
                "You can only go West from here.", None, None, None, 2)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        answer = input("What direction do you want to go in? ")
        answer = answer.upper()

        if answer == "N" or answer == "NORTH":
            print()
            print("You went North.")
            next_room = room_list[current_room].north
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room

        if answer == "E" or answer == "EAST":
            next_room = room_list[current_room].east
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                print()
                print("You went East.")
                current_room = next_room

        if answer == "S" or answer == "SOUTH":
            print()
            print("You went South.")
            next_room = room_list[current_room].south
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room

        if answer == "W" or answer == "WEST":
            print()
            print("You went West.")
            next_room = room_list[current_room].west
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room
main()
