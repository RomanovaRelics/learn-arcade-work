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
    room = Room("You are standing on the porch.\n"
                "You hear creaking coming from within the house.\n"
                "Your friends stare at you from the sidewalk and\n"
                "gesture wildly for you to go inside.\n"
                " \n"
                "You can go North into the house from here.", 1, None, None, None)
    room_list.append(room)
    room = Room("You enter the foyer. You turn on your flashlight\n"
                "and look around. There is not much to see besides\n"
                "cobwebs and dusty mirrors. There is an ominous archway\n"
                "in front of you.", 2, None,None, None)
    room_list.append(room)
    room = Room("You enter the Southern end of the main hallway. \n"
                "You move your flashlight and you jump in fear. \n"
                "It is just an old portrait hanging on the wall. \n"
                "There is an archway to the West. \n"
                "There is a dark door to the East. \n"
                "The hallway continues to the North.", 3, 7, 1, 4)
    room_list.append(room)
    room = Room("You are now in the Northern end of the main hallway. \n"
                "You hear a small creature scurrying nearby. \n"
                "There seems to be a window in front of you draped in heavy \n"
                "black curtains. There is an archway to the West. \n"
                "There is an imposing door to the East.", None, 6, 2, 5)
    room_list.append(room)
    room = Room("You pass through the archway to find a room with furniture \n"
                "covered in dusty white cloths. It seems even the furniture \n"
                "has died. There is nowhere to go from here except back East.", None, 2, None, None)
    room_list.append(room)
    room = Room("You pass through the archway. There is a table with some suspiciously \n"
                "fresh food on it. Has someone or some... thing been living here? \n"
                "There are some other things like an old stove and many half opened \n"
                "cabinets. The only way you can go is back East.", None, 3, None,None)
    room_list.append(room)
    room = Room("You pass through the imposing door to find a small but \n"
                "stately bedroom. A large four poster bed takes up most \n"
                "of the space. There are clothes laid out on the bed waiting \n"
                "to be worn. You can only go back West from here.", None, None, None,3)
    room_list.append(room)
    room = Room("You go through the dark door to a dingy bathroom. \n"
                "You catch a glimpse of yourself in the mirror and swear \n"
                "you see someone behind you. A large spider sits in the \n"
                "broken porcelain sink. You can only go West from here.", None, None, None, 2)
    room_list.append(room)

    current_room = 0

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        answer = input("What direction do you want to go in? ")
        answer = answer.upper()

        if answer == "N" or "NORTH":
            print()
            print("You went North.")
            done = True
            next_room = room_list[current_room].north
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room


        if answer == "E" or "EAST":
            done = True
            print()
            print("You went East.")
            next_room = room_list[current_room].east
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room

        if answer == "S" or "SOUTH":
            done = True
            print()
            print("You went South.")
            next_room = room_list[current_room].south
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room

        if answer == "W" or "WEST":
            done = True
            print()
            print("You went West.")
            next_room = room_list[current_room].west
            if next_room is None:
                print("Something tells you that you can't go that way.")
            else:
                current_room = next_room
main()
