import arcade

WIDTH = 20
HEIGHT = 20
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = (ROW_COUNT * WIDTH) + MARGIN * (ROW_COUNT + 1)
SCREEN_HEIGHT = (COLUMN_COUNT * HEIGHT) + MARGIN * (COLUMN_COUNT + 1)


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # --- Create grid of numbers
        # Create an empty grid list
        self.grid = []
        # Loop for each row
        for row in range(ROW_COUNT):
            # For each row, create a list that will
            # represent an entire row
            self.grid.append([])
            # Loop for each column
            for column in range(COLUMN_COUNT):
                # Add  the number zero to the current row
                self.grid[row].append(0)


    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        for column in range(ROW_COUNT):
            x = column * WIDTH + WIDTH /2 + (column + 1) * MARGIN
            for row in range(COLUMN_COUNT):
                y = row * HEIGHT + HEIGHT /2 + (row + 1) * MARGIN
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, arcade.color.BRIGHT_LILAC)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """

        if arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()