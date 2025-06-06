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
                color = arcade.color.BRIGHT_LILAC
                if self.grid[row][column] == 1:
                    color = arcade.color.RED
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """

        if arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            column = x // (WIDTH + MARGIN)
            row = y // (HEIGHT + MARGIN)
            print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
            self.grid[row][column] = (self.grid[row][column] + 1) % 2

        #Inspect grid and print how many cells are selected
        selected_squares = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    selected_squares += 1
        print(f'Total of {selected_squares} are selected.')

        #Print how many cells are selected in each row

        for row in range(ROW_COUNT):
            cell_per_row = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    cell_per_row += 1
            print(f'Row {row} has {cell_per_row} cells selected.')

        #Print how many cells are in each column

        for column in range(COLUMN_COUNT):
            cell_per_column = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    cell_per_column += 1
            print(f'Column {column} has {cell_per_column} cells selected.')

        #Print continuous squares in row
        for row in range(ROW_COUNT):
            continuous_row_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    continuous_row_count +=1
                else:
                    if continuous_row_count > 1:
                        print(f'There are {continuous_row_count} continuous cells selected on row {row}.')
                    continuous_row_count = 0
            if continuous_row_count > 1:
                print(f'There are {continuous_row_count} continuous cells selected on row {row}.')

                # Print continuous squares in column
                for column in range(COLUMN_COUNT):
                    continuous_column_count = 0
                    for row in range(ROW_COUNT):
                        if self.grid[row][column] == 1:
                            continuous_column_count += 1
                        else:
                            if continuous_column_count > 1:
                                print(f'There are {continuous_column_count} continuous cells selected on column. {column}.')
                            continuous_column_count = 0
                    if continuous_column_count > 1:
                        print(f'There are {continuous_column_count} continuous cells selected on column. {column}.')

        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()