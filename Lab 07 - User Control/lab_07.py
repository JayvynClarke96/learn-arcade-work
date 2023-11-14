""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3

def draw_grass():
    # Ground
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3,0, arcade.color.AIR_SUPERIORITY_BLUE)

def draw_snow_person(x, y):

    arcade.draw_point(x, y, arcade.color.RED,5)
    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)


    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)

def on_draw(delta_time):
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(on_draw.snow_person2_x, 140)
    draw_snow_person(on_draw.snow_person3_x, y=140)

    on_draw.snow_person1_x += 1
    on_draw.snow_person2_x += 1
    on_draw.snow_person3_x += 1

on_draw.snow_person1_x = 150
on_draw.snow_person2_x = 350
on_draw.snow_person3_x = 500

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_ellipse_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)


    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

        draw_grass()
        draw_snow_person(on_draw.snow_person1_x, 140)
        draw_snow_person(on_draw.snow_person2_x, 140)
        draw_snow_person(on_draw.snow_person3_x, y=140)

        on_draw.snow_person1_x += 1
        on_draw.snow_person2_x += 1
        on_draw.snow_person3_x += 1

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y




def main():
    window = MyGame()
    arcade.run()


main()