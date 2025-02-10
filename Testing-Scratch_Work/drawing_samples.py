"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

#Open up a window.
#From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600,600,"Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 600
# Bottom of 0, top of 300
arcade.draw_lrbt_rectangle_filled(0, 600, 0, 300, arcade.csscolor.GREEN)

#Tree trunk.
#Had to switch format to lrbt.
arcade.draw_lrbt_rectangle_filled(100, 120, 290, 350, arcade.csscolor.SIENNA)

#Tree top
#altered to fit lrbt rectangle from previous step.
arcade.draw_circle_filled(110, 350, 30, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and ellipse for top
arcade.draw_lrbt_rectangle_filled(200, 220, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(210, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# Another tree, with a trunk and arc for top
# Arc is centered at (310, 340) with a width of 60 and height of 100.
# The starting angle is 0, and ending angle is 180.
arcade.draw_lrbt_rectangle_filled(300, 320, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(310, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

# Another tree, with a trunk and triangle for top
# Triangle is made of these three points:
# (410, 400), (370, 320), (450, 320)
arcade.draw_lrbt_rectangle_filled(400, 420, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(410, 400, 370, 320, 450, 320, arcade.csscolor.DARK_GREEN)

# Draw a tree using a polygon with a list of points
arcade.draw_lrbt_rectangle_filled(500, 520, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((510,400), (490,360), (480, 320), (540, 320), (530, 360)), arcade.csscolor.DARK_GREEN)

# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)

# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 600, 550, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 500, 450, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 500, 650, arcade.csscolor.YELLOW)

#Diagonal rays
arcade.draw_line(500, 550, 550, 600, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 550, 500, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 450, 600, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 450, 500, arcade.csscolor.YELLOW)

# Draw text at (150, 230) with a font size of 24 pts.
"""
PerformanceWarning: draw_text is an extremely slow function for displaying text. Consider using Text objects instead.
warnings.warn(message, warning_type), comes up with use of arcade.draw_text()
"""
arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.csscolor.BLACK, 24)

# Finish drawing.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()