""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

"""Draw Nest"""
#I did the y + 30 on purpose to make it look center even though it is not technically the actual center but the visual center.
def draw_nest(x, y):
    """Nest base"""
    arcade.draw_arc_filled(x + 0, y + 30, 190, 200, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)
    """Nest hole"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 190, 60, arcade.color.BISTRE_BROWN)
    """Egg"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 40, 50, arcade.color.BEIGE)

"""Draw Bush"""
def draw_bush(x, y):
    arcade.draw_ellipse_filled(x - 0, y - 50, 20, 160, arcade.color.BROWN)
    arcade.draw_circle_filled(x - 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x + 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_ellipse_filled(x + 0, y + 20, 80, 150, arcade.color.ANDROID_GREEN)

"""Draw chick"""
def draw_chick(x, y):
    """Chick body"""
    arcade.draw_ellipse_filled(x, y,120, 160, arcade.color.DANDELION)
    """Chick head"""
    arcade.draw_circle_filled(x, y + 100,50, arcade.color.CORN)
    """Left Wing"""
    arcade.draw_ellipse_filled(x - 70,y + 30, 40, 100, arcade.color.CORN, 45)
    """Right Wing"""
    arcade.draw_ellipse_filled(x + 70, y + 30, 40, 100, arcade.color.CORN, -45)
    """Left foot"""
    arcade.draw_triangle_filled(x - 50, y - 80, x - 15, y - 80, x - 35, y - 50, arcade.color.SELECTIVE_YELLOW)
    """Right foot"""
    arcade.draw_triangle_filled(x + 50, y - 80,x + 15, y - 80, x + 35,y - 50, arcade.color.SELECTIVE_YELLOW)
    """Left Eye"""
    arcade.draw_circle_filled(x - 20, y + 100,9, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 20, y + 100, 5, arcade.color.BLACK)
    """Right eye"""
    arcade.draw_circle_filled(x + 20, y + 100, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y + 100, 5, arcade.color.BLACK)
    """Beak"""
    arcade.draw_triangle_filled(x - 10, y + 80, x + 0, y + 60, x + 10, y + 80, arcade.color.SELECTIVE_YELLOW)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.chick1 = Chick()
        self.chick2 = Chick()

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BITTER_LIME)

        draw_bush(140, 295)
        draw_bush(650, 290)
        draw_nest(700, 210)
        draw_nest(100, 50)
        draw_bush(400, 250)



class Chick:
    """ This class manages a chick moving on the screen. """

    def __init__(self, x, y, change_x, change_y):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y

    def draw(self):
        """ Draw the chick 1 with the instance variables we have. """
        draw_chick(200, 200)

    def on_update(self, change_x, change_y):
        """ Code to control the chick 1 movement. """

        # Move the ball
        self.y += self.change_y
        self.x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.x < 400:
            self.change_x *= -1

        if self.x > SCREEN_WIDTH - 300:
            self.change_x *= -1

        if self.y < 500:
            self.change_y *= -1

        if self.y > SCREEN_HEIGHT - 200:
            self.change_y *= -1

def main():
    window = MyGame()
    arcade.run()


main()