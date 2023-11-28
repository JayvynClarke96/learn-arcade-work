""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def on_draw(self):
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class Block:

    def __init__(self, center_x, center_y, color, height, width):
        self.center_x = center_x
        self.center_y = center_y
        self.height = height
        self.color = color
        self.width = width
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,
                                     self.center_y,
                                     self.width,
                                     self.height,
                                     self.color)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        self.ball_sound = arcade.load_sound("712628__robinhood76__12287-oriental-magic-transformation.wav")
        self.block_sound = arcade.load_sound("712560__shangasdfguy123__scpsea-scp-xqy18-blowing.wav")

        self.block_list = None

        # Background Color
        arcade.set_background_color(arcade.color.BABY_PINK)

        self.ball = Ball(50, 50, 5, arcade.color.RED)
        self.block = Block(30, 30, arcade.color.RED, 5, 10)

    def on_draw(self):
        arcade.start_render()
        self.ball.on_draw()
        self.block.draw()

    def on_update(self, delta_time):
        self.block.update()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        arcade.play_sound(self.ball_sound)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.block.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.block.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.block.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.block.change_x = MOVEMENT_SPEED

        if self.block.change_x < SCREEN_WIDTH:
            arcade.play_sound(self.block_sound)
        if self.block.change_y < SCREEN_HEIGHT:
            arcade.play_sound(self.block_sound)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.block.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.block.change_x = 0

def main():
    window = MyGame()
    arcade.run()


main()
