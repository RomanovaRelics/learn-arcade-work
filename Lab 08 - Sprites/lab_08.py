"""Lab 8 - Spooky Guy"""

import random
import arcade
import math

SPRITE_SCALING = 0.9


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Bat(arcade.Sprite):

    def reset_pos(self):

        # Reset the bat to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the bat
        self.center_y -= 1

        # See if the bat has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Ectoplasm(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        """ Update the ball's position. """
        # Calculate a new x, y
        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Load sounds
        self.ghost_sound = arcade.load_sound(":resources:sounds/jump3.wav")
        self.bat_sound = arcade.load_sound(":resources:sounds/hurt1.wav")
        # Sprite lists
        self.player_list = None
        self.ectoplasm_list = None
        self.bat_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ectoplasm_list = arcade.SpriteList()
        self.bat_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

        # Ghost image from kenney.nl
        self.player_sprite = arcade.Sprite("ghost_normal.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        for i in range(50):

            # Create the coin instance
            # Both images from kenney.nl
            ectoplasm = Ectoplasm("spinner_hit.png", SPRITE_SCALING / 3)
            bat = Bat("bat_fly.png",SPRITE_SCALING / 3)

            # Position the center of the circle the ectoplasm will orbit
            ectoplasm.circle_center_x = random.randrange(SCREEN_WIDTH)
            ectoplasm.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Position the bats
            bat.center_x = random.randrange(SCREEN_WIDTH)
            bat.center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            ectoplasm.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            ectoplasm.circle_angle = random.random() * 2 * math.pi

            # Add the ectoplasm and bats to the lists
            self.ectoplasm_list.append(ectoplasm)
            self.bat_list.append(bat)

    def on_draw(self):

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.ectoplasm_list.draw()
        self.player_list.draw()
        self.bat_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.ectoplasm_list.update()
        self.bat_list.update()

        # Generate a list of all sprites that collided with the player.
        ectoplasm_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.ectoplasm_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for ectoplasm in ectoplasm_hit_list:
            self.score += 1
            ectoplasm.remove_from_sprite_lists()
            arcade.play_sound(self.ghost_sound)

            # Generate a list of all sprites that collided with the player.
        bat_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                      self.bat_list, )

        for bat in bat_hit_list:
            self.score -= 1
            bat.remove_from_sprite_lists()
            arcade.play_sound(self.bat_sound)

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()