"""LAB 8"""

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_ECTOPLASM = 0.2
ECTOPLASM_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Ectoplasm(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self, delta_time: float = 1 / 60) -> None:

        # Move the ectoplasm
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Spooky Guy")

        self.ghost_sound = arcade.load_sound("ghost_sound.wav")

        # Variables that will hold sprite lists
        self.player_list = None
        self.ectoplasm_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.ectoplasm_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(ECTOPLASM_COUNT):

            # Create the ectoplasm instance
            # Ectoplasm image from kenney.nl
            ectoplasm = Ectoplasm("spinner_hit.png", SPRITE_SCALING_ECTOPLASM)

            # Position the coin
            ectoplasm.center_x = random.randrange(SCREEN_WIDTH)
            ectoplasm.center_y = random.randrange(SCREEN_HEIGHT)
            ectoplasm.change_x = random.randrange(-3, 4)
            ectoplasm.change_y = random.randrange(-3, 4)

            # Add the coin to the lists
            self.ectoplasm_list.append(ectoplasm)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.ectoplasm_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.ectoplasm_list.update()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.ectoplasm_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for ectoplasm in hit_list:
            ectoplasm.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.ghost_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()