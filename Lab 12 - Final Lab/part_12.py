import arcade
import random

PLAYER_SCALING = 0.4
SPRITE_SCALING_CAR1 = 3
SPRITE_SCALING_CAR2 = 3
SPRITE_SCALING_CAR3 = 3
SPRITE_SCALING_CAR4 = 1.5
SPRITE_SCALING_GEM = 0.6

CAR_COUNT = 10
GEM_COUNT = 30
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_TITLE = "Traffic Game"
MOVEMENT_SPEED = 8
PLAYER_SPEED = 4


class Gems(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0


class Car1(arcade.Sprite):
    def update(self):
        self.center_y -= MOVEMENT_SPEED

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT + 100


class Car2(arcade.Sprite):
    def update(self):
        self.center_y -= MOVEMENT_SPEED

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT + 100


class Car3(arcade.Sprite):
    def update(self):
        self.center_y += MOVEMENT_SPEED

        if self.center_y > 1000:
            self.center_y = SCREEN_HEIGHT - 1100


class Car4(arcade.Sprite):
    def update(self):
        self.center_y += MOVEMENT_SPEED

        if self.center_y > 1000:
            self.center_y = SCREEN_HEIGHT - 1100


class Car5(arcade.Sprite):
    def update(self):
        self.center_y += MOVEMENT_SPEED

        if self.center_y > 1000:
            self.center_y = SCREEN_HEIGHT - 1100


class Car6(arcade.Sprite):
    def update(self):
        self.center_y -= MOVEMENT_SPEED

        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT + 100


class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.background = None

        self.car_list = None
        self.player_list = None
        self.gem_list = None

        self.car1_sprite = None
        self.car2_sprite = None
        self.car3_sprite = None
        self.car4_sprite = None
        self.car5_sprite = None
        self.car6_sprite = None

        self.player_sprite = None
        self.physics_engine = None

        self.score = 0

        self.crash_sound = arcade.load_sound("crash.wav")
        self.car_sound = arcade.load_sound("car.wav")
        self.pickup_sound = arcade.load_sound("Picked Coin Echo 2.wav")

        arcade.set_background_color(arcade.color.GOLD)

    def setup(self):

        # Background Image
        self.background = arcade.load_texture("highway2.jpeg")

        self.car_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        self.score = 0
        self.player_lives = 3

        self.player_sprite = arcade.Sprite(":resources:images/alien/alienBlue_walk1.png", PLAYER_SCALING)
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 130
        self.player_list.append(self.player_sprite)

        for e in range(GEM_COUNT):
            gem = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING_GEM)
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)
            self.gem_list.append(gem)

        for j in range(CAR_COUNT):
            car1 = Car1("car1.png", SPRITE_SCALING_CAR1)
            car1.center_x = 100
            car1.center_y = 900
            self.car_list.append(car1)

        for i in range(CAR_COUNT):
            car2 = Car2("car2.png", SPRITE_SCALING_CAR2)
            car2.center_x = 400
            car2.center_y = 900
            self.car_list.append(car2)

        for l in range(CAR_COUNT):
            car3 = Car3("car3.jpeg", SPRITE_SCALING_CAR3)
            car3.center_x = 230
            car3.center_y = 100
            self.car_list.append(car3)

        for k in range(CAR_COUNT):
            car4 = Car4("car4.png", SPRITE_SCALING_CAR4)

            car4.center_x = 570
            car4.center_y = 530
            self.car_list.append(car4)

        for P in range(CAR_COUNT):
            car5 = Car5("car3.jpeg", SPRITE_SCALING_CAR3)
            car5.center_x = 780
            car5.center_y = 530
            self.car_list.append(car5)

        for U in range(CAR_COUNT):
            car6 = Car6("car1.png", SPRITE_SCALING_CAR1)
            car6.center_x = 900
            car6.center_y = 530
            self.car_list.append(car6)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,self.car_list)

    def on_draw(self):
        arcade.start_render()

        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.gem_list.draw()
        self.player_list.draw()
        self.car_list.draw()

        gems_collected = f"Score: {self.score}"
        arcade.draw_text(gems_collected, 875, 950, arcade.color.WHITE, 20)
        player_lives = f"lives: {self.player_lives}"
        arcade.draw_text(player_lives, 880, 930, arcade.color.WHITE, 20)

    def on_update(self, delta_time):

        self.physics_engine.update()

        self.car_list.update()
        self.player_list.update()

        gem_collection_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)
        crash_list = arcade.check_for_collision_with_list(self.player_sprite, self.car_list)
        for gem_pickup in gem_collection_list:
            arcade.play_sound(self.pickup_sound)
            self.score += 1
            gem_pickup.remove_from_sprite_lists()
        for player_hit in crash_list:
            arcade.play_sound(self.crash_sound)
            self.player_lives -= 1

        if self.score > 29:
            arcade.draw_text("YOU WIN :)", 500, 500, arcade.color.BLACK, 50)
        elif self.player_lives < 1:
            arcade.draw_text("YOU LOSE :(", 500, 500, arcade.color.BLACK, 50)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.D or key == arcade.key.A:
            self.player_sprite.change_x = 0


def main():

    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()




