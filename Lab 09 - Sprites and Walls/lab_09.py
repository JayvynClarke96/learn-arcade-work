"""
Sprite Move With Walls

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_walls
"""

import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Sprite lists
        self.coin_list = None
        self.wall_list = None
        self.player_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite(":resources:images/animated_characters/zombie/zombie_idle.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        # -- Set up the walls
        # Column 1
        for Column1 in range (200,460,65):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 40
            wall.center_y = Column1
            self.wall_list.append(wall)

        # Column 2
        for Column2 in range (200,460,65):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 170
            wall.center_y = Column2
            self.wall_list.append(wall)

        # Column 3
        for Column3 in range (200,460,65):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 300
            wall.center_y = Column3
            self.wall_list.append(wall)

        # Column 4
        for Column4 in range (200,460,65):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 430
            wall.center_y = Column4
            self.wall_list.append(wall)

        # Column 5
        for Column5 in range (200,460,65):
            wall = arcade.Sprite(":resources:images/tiles/grassCenter.png", SPRITE_SCALING)
            wall.center_x = 560
            wall.center_y = Column5
            self.wall_list.append(wall)

        # Top row

        for toprow in range(40,625,65):
            wall = arcade.Sprite(":resources:images/tiles/brickBrown.png", SPRITE_SCALING)
            wall.center_x = toprow
            wall.center_y = 460
            self.wall_list.append(wall)

        # Borders
        for border1 in range(0,820,65):
            wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
            wall.center_x = border1
            wall.center_y = 590
            self.wall_list.append(wall)

        for border2 in range(0,655,65):
            wall = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png", SPRITE_SCALING)
            wall.center_x = 785
            wall.center_y = border2
            self.wall_list.append(wall)

        #Adding Coins

        coin_position = [[105, 460],
                         ]

        for coin_position in coin_position:
            coin = arcade.Sprite(":resources:images/items/gemBlue.png", SPRITE_SCALING)
            coin.center_x, coin.center_y = coin_position
            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite,
                                                         self.wall_list,
                                                         )

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list.draw()

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
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()