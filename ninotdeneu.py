import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Snow
    arcade.draw_circle_filled(x, 60 + y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 140 + y, 50, arcade.color.WHITE)
    arcade.draw_circle_filled(x, 200 + y, 40, arcade.color.WHITE)

    # Eyes
    arcade.draw_circle_filled(x - 15, 210 + y, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 15, 210 + y, 5, arcade.color.BLACK)


def arbre (px,py):
        arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.BROWN)
        arcade.draw_circle_filled(25+px, 120+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(0+px, 150+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(35+px, 180+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(40+px, 160+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(50+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 180+py, 30, arcade.csscolor.DARK_GREEN)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

    draw_grass()
    arbre(680,195)
    arbre(350,200)
    arbre(30,190)
    draw_snow_person(150, 130)
    draw_snow_person(450, 140)
    draw_snow_person(320, 95)
    draw_snow_person(580, 120)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()