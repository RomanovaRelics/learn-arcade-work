"""
This is an original drawing and animation of some chicks using the Python arcade for Lab 3.
Cluck! cluck!
"""

"""Import the "arcade" library"""
import arcade

"""Constant values"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""Opens window"""
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

"""Set background color. NOT WORKING"""
arcade.set_background_color(arcade.color.SKY_BLUE)

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
    arcade.draw_triangle_filled(x - 15,y - 15,x + 20, y + 15,x + 0,y +15, arcade.color.SELECTIVE_YELLOW)
    """Right foot"""
    arcade.draw_triangle_filled(320, 120, 360, 120, 340, 150, arcade.color.SELECTIVE_YELLOW)
    """Left Eye"""
    arcade.draw_circle_filled(280, 310, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(280, 310, 5, arcade.color.BLACK)
    """Right eye"""
    arcade.draw_circle_filled(320, 310, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(320, 310, 5, arcade.color.BLACK)
    """Beak"""
    arcade.draw_triangle_filled(290, 280, 310, 280, 300, 260, arcade.color.SELECTIVE_YELLOW)

"""Draw Nest"""
def draw_nest(x, y):
    """Nest base"""
    arcade.draw_arc_filled(500, 130, 190, 200, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)
    """Nest hole"""
    arcade.draw_ellipse_filled(500, 130, 190, 60, arcade.color.BISTRE_BROWN)
    """Egg"""
    arcade.draw_ellipse_filled(500, 130, 40, 50, arcade.color.BEIGE)

#Draw a point at x, y for reference
    #In the future, this point should be in the very middle of the object.
    arcade.draw_point(300, 200, arcade.color.RED, 5)

"""Call functions"""
draw_grass()
draw_chick(200, 200)
draw_nest(500, 130)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()