import arcade.color
#class Dog():
#    def __init__(self):
#        self.age = 0
#        self.name = " "
#        self.weight = 0

#def bark(self):
        #print("\"Woof!\" says", self.name + ".")
###instantiate object or instance of class through variables
#my_dog = Dog()

#my_dog.name = "Sputnik"
#my_dog.weight = 20
#my_dog.age = 3

#my_dog.bark()

class Ball():
    def __init__(self):
        ###Class attributes
        ###Ball position
        self.x = 0
        self.y = 0

        ###Ball vector how far move horizontally in a certain amount of time
        self.change_x = 0
        self.change_y = 0

        ###Ball size
        self.size = 10

        ###Ball color
        self.color = arcade.color.BOYSENBERRY

    ###Class methods
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)