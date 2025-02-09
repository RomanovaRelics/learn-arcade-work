"""Hello this is a multiline
comment practice"""
#this is a single line comment practice

# Import the "arcade" library
import arcade

#Opens a drawing window.
arcade.open_window(600,600,"Drawing Example")

#Sets background color for drawing window.
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

#Start drawing.
arcade.start_render()

#Makes a rectangle on the bottom half of our window.
arcade.draw_lrbt_rectangle_filled(0, 600, 0, 300, arcade.csscolor.GREEN)

#Tree trunk. Had to switch format to lrbt.
arcade.draw_lrbt_rectangle_filled(100, 120, 290, 350, arcade.csscolor.SIENNA)

#Tree top altered to fit lrbt rectangle from previous step.
arcade.draw_circle_filled(110, 350, 30, arcade.csscolor.DARK_GREEN)

#Another tree with a trunk and ellipse top.
arcade.draw_lrbt_rectangle_filled(200, 220, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(210, 370, 60, 80, arcade.csscolor.DARK_GREEN)

#Another tree with an arc top.
arcade.draw_lrbt_rectangle_filled(300, 320, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_arc_filled(310, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#End drawing.
arcade.finish_render()

#Keeps the window open until someone closes it.
arcade.run()