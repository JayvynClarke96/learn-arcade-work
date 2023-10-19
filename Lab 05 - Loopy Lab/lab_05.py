import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    for row in range(30):
        for column in range(30):
            x = 0 + column * 10  # Instead of zero, calculate the proper x location using 'column'
            y = 300 - row * 10  # Instead of zero, calculate the proper y location using 'row'
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    for row in range(30):
        for column in range(30):
            x = 300 + column * 10
            y = 300 - row * 10
            if (row + column) % 2 == 0:
                arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x,y,5,5,arcade.color.BLACK)



def draw_section_3():
    for column in range(30):
        for row in range(30):
            x = 600 + column * 10
            y = 300 - row * 10
            if (row + column) % 3 == 0:
                arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)
            elif (row + column) % 2 == 1:
                arcade.draw_rectangle_filled(x,y,5,5,arcade.color.BLACK)


def draw_section_4():
    # Use the modulus operator and just one 'if' statement to select the color.
    pass


def draw_section_5():
    for row in range(30):
        for column in range(1 + row):
            x = 0 + column * 10
            y = 600 - row * 10
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)

    # Do NOT use 'if' statements to complete 5-8. Manipulate the loops instead.



def draw_section_6():
    for row in range(30):
        for column in range(row - 1):
            x = 300 + column * 10
            y = 600 - row * 10
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)



def draw_section_7():
    for column in range(30):
        for row in range(column + 1):
            x = 600 + column * 10
            y = 600 - row * 10
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)


def draw_section_8():
    for column in range(30):
        for row in range(column - 1):
            x = 900 + column * 10
            y = 600 - row * 10
            arcade.draw_rectangle_filled(x,y,5,5,arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()