"""
This is an original drawing of a chick using the Python arcade.
Cluck! cluck!
"""

# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(600, 600, "Lab 2 Drawing")

# Set the background color
arcade.set_background_color(arcade.color.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the grass
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.BITTER_LIME)

#Chick body
arcade.draw_ellipse_filled(300, 200, 120, 160, arcade.color.DANDELION)

#Chick head
arcade.draw_circle_filled( 300, 300, 50, arcade.color.CORN)

#Left wing
arcade.draw_ellipse_filled( 230, 230, 40, 100, arcade.color.CORN, 45)

#Right wing
arcade.draw_ellipse_filled( 370, 230, 40, 100, arcade.color.CORN, -45)

#Left foot
arcade.draw_triangle_filled( 250, 120, 285, 120, 265, 150, arcade.color.SELECTIVE_YELLOW)

#Right foot
arcade.draw_triangle_filled( 320, 120, 360, 120, 340, 150, arcade.color.SELECTIVE_YELLOW)

#Left eye
arcade.draw_circle_filled( 280, 310, 9, arcade.color.WHITE)
arcade.draw_circle_filled( 280, 310, 5, arcade.color.BLACK)

#Right eye
arcade.draw_circle_filled( 320, 310, 9, arcade.color.WHITE)
arcade.draw_circle_filled( 320, 310, 5, arcade.color.BLACK)

#Beak
arcade.draw_triangle_filled( 290, 280, 310, 280, 300, 260, arcade.color.SELECTIVE_YELLOW)

#Nest
arcade.draw_arc_filled( 500, 130, 180, 100, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()