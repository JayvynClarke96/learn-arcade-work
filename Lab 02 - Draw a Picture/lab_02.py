import arcade

arcade.open_window(800,600, "Drawing Example")

#Background Color
arcade.set_background_color(arcade.color.BRIGHT_NAVY_BLUE)

arcade.start_render()

#Draw Buildings
arcade.draw_rectangle_filled(600,20,100,700, arcade.color.COOL_GREY)
arcade.draw_rectangle_filled(400,60,100,800, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(300,80,100,700, arcade.color.DAVY_GREY)
arcade.draw_rectangle_filled(50,20,100,900, arcade.color.COOL_GREY)
arcade.draw_rectangle_filled(100,20,100,1000, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(800,20,100,900, arcade.color.DAVY_GREY)
arcade.draw_rectangle_filled(200,20,100,725, arcade.color.COOL_GREY)
arcade.draw_rectangle_filled(700,20,100,825, arcade.color.LAVENDER_GRAY)
arcade.draw_rectangle_filled(500,20,100,1000, arcade.color.DAVY_GREY)

#Draw Moon
arcade.draw_circle_filled(250,575,80, arcade.color.OLD_LACE)

#Draw Stars
arcade.draw_circle_filled(25,550,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(100,555,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(165,520,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(190,425,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(250,460,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(290,510,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(340,520,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(390,575,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(450,590,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(550,575,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(500,560,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(590,495,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(630,455,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650,475,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(700,555,2, arcade.color.OLD_LACE)
arcade.draw_circle_filled(770,565,2, arcade.color.OLD_LACE)




arcade.finish_render()
arcade.run()