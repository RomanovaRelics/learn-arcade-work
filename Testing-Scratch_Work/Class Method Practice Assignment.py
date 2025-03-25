#import arcade.color

#class Cat():
    #def __init__(self):
        #self.name = "cat"
        #self.color = " "
        #self.weight = int

    #def meow(self):
        #print(self.name + " says" + " " + "\"Meow\"" + "!")

#cat_1 = Cat()

#cat_1.name = "Gregory"
#cat_1.color = arcade.color.PEAR
#cat_1.weight = 10

#cat_1.meow()

class Monster():
    def __init__(self):
        self.name = "monster"
        self.health = 12

    def decrease_health(self):
        self.health -= 2
        print("The monster's health decreases by 2.")
        print("The monsters health is now",monster_1.health)
        if self.health <= 0:
            print("The monster has been slain!")

monster_1 = Monster()

monster_1.name = "Morgus"
monster_1.health = 12

monster_1.decrease_health()
monster_1.decrease_health()
monster_1.decrease_health()
