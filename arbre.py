"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)

def arbre (px,py):
        arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.BROWN)
        arcade.draw_circle_filled(25+px, 120+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(0+px, 150+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(35+px, 180+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(40+px, 160+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(50+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 180+py, 30, arcade.csscolor.DARK_GREEN)


arcade.open_window(600, 600, "Drawing Example")

def nuvol (x,y):
        arcade.draw_circle_filled(95, 495, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(130, 500, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(105, 515, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(75, 510, 30, arcade.csscolor.WHITE)

#background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)
arcade.start_render()

#Rectangles
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arbre(150,220)
arbre(350,200)

#Cercles
arcade.draw_circle_filled(500, 500, 50, arcade.csscolor.YELLOW)
nuvol(300,350)

#Elipse
arcade.draw_ellipse_filled(160, 130, 190, 90, arcade.csscolor.BLUE, 3)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()