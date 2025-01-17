""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
GEM_COUNT = 50
BEE_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5


class Gems(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        # Move the gems
        self.center_x += self.change_x
        self.center_y += self.change_y

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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Score
        self.score = 0

        # Setting up Sound
        self.good_sound = arcade.load_sound("711187__1love__magic-bass-hit-1.wav")
        self.bad_sound = arcade.load_sound("623411__nlux__yp-plague-databurst-014.wav")

        # My Sprite List
        self.good_sprites_list = None
        self.bad_sprites_list = None
        self.player_list = None

        # Setting up my player
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):

        self.player_list = arcade.SpriteList()
        self.good_sprites_list = arcade.SpriteList()
        self.bad_sprites_list = arcade.SpriteList()

        # Drawing My player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/male_person/malePerson_idle.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 60
        self.player_list.append(self.player_sprite)

        # Drawing Good Sprite
        for i in range(GEM_COUNT):
            gem = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING_COIN)
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)
            self.good_sprites_list.append(gem)

        # Drawing Bad Sprite
        for e in range(BEE_COUNT):
            bee = arcade.Sprite(":resources:images/enemies/bee.png", SPRITE_SCALING_COIN)
            bee.center_x = random.randrange(SCREEN_WIDTH)
            bee.center_y = random.randrange(SCREEN_HEIGHT)
            self.bad_sprites_list.append(bee)

        # Background color
        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):
        arcade.start_render()

        self.clear()
        self.player_sprite.draw()
        self.good_sprites_list.draw()
        self.bad_sprites_list.draw()

        # Drawing the Score
        gems_collected = f"Score: {self.score}"
        arcade.draw_text(gems_collected, 10, 20, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        for good in self.good_sprites_list:
            good.center_x += 3
            if good.center_x > SCREEN_WIDTH:
                good.center_x = 0

        for bad in self.bad_sprites_list:
            bad.center_x -= 3
            if bad.center_x < 0:
                bad.center_x = SCREEN_WIDTH

        good_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_sprites_list)
        bad_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_sprites_list)
        for good_sprite in good_hit_list:
            arcade.play_sound(self.good_sound)
            self.score += 1
            good_sprite.remove_from_sprite_lists()
        for bad_sprite in bad_hit_list:
            arcade.play_sound(self.bad_sound)
            self.score -= 1
            bad_sprite.remove_from_sprite_lists()

        self.player_list.update()


def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
