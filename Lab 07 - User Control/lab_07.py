
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

"""Draw Nest"""
def draw_nest(x, y):
    """Nest base"""
    arcade.draw_arc_filled(x + 0, y + 30, 190, 200, arcade.color.UNIVERSITY_OF_CALIFORNIA_GOLD, 180, 360)
    """Nest hole"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 190, 60, arcade.color.BISTRE_BROWN)
    """Egg"""
    arcade.draw_ellipse_filled(x + 0, y + 30, 40, 50, arcade.color.BEIGE)

"""Draw Bush"""
def draw_bush(x, y):
    arcade.draw_ellipse_filled(x - 0, y - 50, 20, 160, arcade.color.BROWN)
    arcade.draw_circle_filled(x - 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_circle_filled(x + 40, y + 20, 60, arcade.color.APPLE_GREEN)
    arcade.draw_ellipse_filled(x + 0, y + 20, 80, 150, arcade.color.ANDROID_GREEN)

"""Draw chick"""
def draw_chick(x, y):
    """Chick body"""
    arcade.draw_ellipse_filled(x, y,120, 160, arcade.color.DANDELION)
    """Chick head"""
    arcade.draw_circle_filled(x, y + 100,50, arcade.color.CORN)
    """Left Wing"""
    arcade.draw_ellipse_filled(x - 70,y + 30, 40, 100, arcade.color.CORN, 45)
    """Right Wing"""
    arcade.draw_ellipse_filled(x + 70, y + 30, 40, 100, arcade.color.CORN, -45)
    """Left foot"""
    arcade.draw_triangle_filled(x - 50, y - 80, x - 15, y - 80, x - 35, y - 50, arcade.color.SELECTIVE_YELLOW)
    """Right foot"""
    arcade.draw_triangle_filled(x + 50, y - 80,x + 15, y - 80, x + 35,y - 50, arcade.color.SELECTIVE_YELLOW)
    """Left Eye"""
    arcade.draw_circle_filled(x - 20, y + 100,9, arcade.color.WHITE)
    arcade.draw_circle_filled(x - 20, y + 100, 5, arcade.color.BLACK)
    """Right eye"""
    arcade.draw_circle_filled(x + 20, y + 100, 9, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 20, y + 100, 5, arcade.color.BLACK)
    """Beak"""
    arcade.draw_triangle_filled(x - 10, y + 80, x + 0, y + 60, x + 10, y + 80, arcade.color.SELECTIVE_YELLOW)

class Chick:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

    change_x = 0
    change_y = 0

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        draw_chick(self.position_x, self.position_y,)

    def update(self):
        # Move the chick
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < 80:
            self.position_x = 80

        if self.position_x > SCREEN_WIDTH - 70:
            self.position_x = SCREEN_WIDTH - 70

        if self.position_y < 80:
            self.position_y = 80

        if self.position_y > SCREEN_HEIGHT - 150:
            self.position_y = SCREEN_HEIGHT - 150


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        self.chick_sound = arcade.load_sound("chirp.wav")
        self.edge_sound = arcade.load_sound("hurt3.wav")

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create our ball
        self.chick1 = Chick(200, 200)
        self.chick2 = Chick(400, 400)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()

        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.BITTER_LIME)

        draw_bush(140, 295)
        draw_bush(650, 290)
        draw_nest(700, 210)
        draw_nest(100, 50)
        draw_bush(400, 250)

        self.chick1.draw()
        self.chick2.draw()

    def update(self, delta_time):
        self.chick1.update()
        self.chick2.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.chick1.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.chick1.change_x = MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.chick1.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.chick1.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            arcade.play_sound(self.chick_sound)

        if self.position_x < 80:
            self.position_x = 80
            arcade.play_sound(self.edge_sound)
        if self.position_x > SCREEN_WIDTH - 70:
            self.position_x = SCREEN_WIDTH - 70
            arcade.play_sound(self.edge_sound)
        if self.position_y < 80:
            self.position_y = 80
            arcade.play_sound(self.edge_sound)
        if self.position_y > SCREEN_HEIGHT - 150:
            self.position_y = SCREEN_HEIGHT - 150
            arcade.play_sound(self.edge_sound)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A or key == arcade.key.D:
            self.chick1.change_x = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.chick1.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.chick2.position_x = x
        self.chick2.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.chick_sound)

def main():
    window = MyGame(800, 600, "Lab 7")
    arcade.run()


main()