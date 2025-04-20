import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = ((ROW_COUNT * 20) + 55)
SCREEN_HEIGHT = ((COLUMN_COUNT * 20) + 55)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        for i in range(10):
            column = i + 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        arcade.draw_rectangle_filled(15, 15,20, 20, arcade.color.BRIGHT_LILAC)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()