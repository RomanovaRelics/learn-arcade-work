"""Import Arcade"""
import arcade

"""Constant values"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

"""Define draw grass function"""
def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)

"""Define draw snow person function"""
def draw_snow_person(x, y):

    #Draw a point at x, y for reference
    #In the future, this point should be in the very middle of the object.
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

"""Define on draw function"""
def on_draw(delta_time):
    """Draw everything"""
    arcade.start_render()

    draw_grass()
    draw_snow_person(450, 180)
    #Changing variables for snow person.
    draw_snow_person(on_draw.snow_person1_x, on_draw.snow_person1_y)

    # Add and subtract numbers below to direct the animation.
    # Negative numbers move left. Positive numbers move right. Larger numbers move faster.
    #This one goes up.
    on_draw.snow_person1_x += 0
    on_draw.snow_person1_y += 2

#Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150
on_draw.snow_person1_y = 140
"""Define main function"""
def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    #Call on_draw function every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


"""Call main function. This will use everything above in the main function."""
main()