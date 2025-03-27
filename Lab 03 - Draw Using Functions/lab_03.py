"""
This is an original drawing and animation of some chicks using the Python arcade for Lab 3.
Cluck! cluck!
"""

"""Import the "arcade" library"""
import arcade

"""Constant values"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""Draw ground"""
def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BITTER_LIME)

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

"""Draw Nest"""
#I did the y + 30 on purpose to make it look center even though it is not technically the actual center but the visual center.
def draw_nest(x, y):
    """Nest base"""
    arcade.draw_arc_filled(x + 0, y + 30, 190, 200, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)
    """Nest hole"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 190, 60, arcade.color.BISTRE_BROWN)
    """Egg"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 40, 50, arcade.color.BEIGE)

"""Draw bush"""
#I did the y-50 and y+20s on purpose to make it look like the visual center.
def draw_bush(x, y):
    arcade.draw_ellipse_filled(x - 0, y - 50, 20, 160, arcade.color.BROWN)
    arcade.draw_circle_filled(x - 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x + 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_ellipse_filled(x + 0, y + 20, 80, 150, arcade.color.ANDROID_GREEN)


#Draw a point at x, y for reference
    #In the future, this point should be in the very middle of the object.
    arcade.draw_point(200, 200, arcade.color.RED, 5)
    arcade.draw_point(100, 50, arcade.color.RED, 5)
    arcade.draw_point(400, 220, arcade.color.RED, 5)

"""Define main function"""
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.SKY_BLUE)
    arcade.start_render()
    draw_grass()
    draw_bush(140, 295)
    draw_bush(650, 290)
    draw_chick(200, 200)
    draw_nest(700, 210)
    draw_chick(600, 160)
    draw_nest(100, 50)
    draw_bush(400, 250)
    arcade.finish_render()
    arcade.run()

"""Call main function"""
main()

