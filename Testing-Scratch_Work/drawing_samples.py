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

#Another tree with a triangle top.
arcade.draw_lrbt_rectangle_filled(400, 420, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(410, 400, 370, 320, 450, 320, arcade.csscolor.DARK_GREEN)

#Another tree with a polygon top (list of points)
arcade.draw_lrbt_rectangle_filled(500, 520, 290, 350, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((510,400), (490,360), (480, 320), (540, 320), (530, 360)), arcade.csscolor.DARK_GREEN)

#Sun.
arcade.draw_circle_filled(500, 550, 40, arcade.csscolor.YELLOW)

#Rays left, right, up, and down.
arcade.draw_line(500, 550, 400, 550, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 600, 550, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 500, 450, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 500, 650, arcade.csscolor.YELLOW)

#Diagonal rays.
arcade.draw_line(500, 550, 550, 600, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 550, 500, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 450, 600, arcade.csscolor.YELLOW)
arcade.draw_line(500, 550, 450, 500, arcade.csscolor.YELLOW)

#Draw text.
arcade.draw_text("Arbor Day - Plant a Tree!", 150, 230, arcade.csscolor.BLACK, 24)
#End drawing.
arcade.finish_render()

#Keeps the window open until someone closes it.
arcade.run()