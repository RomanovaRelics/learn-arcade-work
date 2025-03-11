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
    room = Room("You are standing on the porch.\n "
                "You hear creaking coming from within the house. \n"
                "Your friends stare at you from the sidewalk and \n"
                "gesture wildly for you to go inside.", 1, None, None, None)
    room_list.append(0)
    room = Room("You enter the foyer. You turn on your flashlight\n"
                "and look around. There is not much ot see besides\n"
                "cobwebs and dusty mirrors. There is an ominous archway\n"
                "in front of you.", 2, None,None, None)
    room_list.append(1)
    room = Room("You enter the South portion of the hallway. ")

main()
