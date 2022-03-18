'''DIBUIXANT ELEMENTS
La llibreria arcade disposa d'unes primitives (funcions de dibuix) que ens permeten dibuixar:'''
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

#Rectangles: 
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
arcade.draw_lrtb_rectangle_filled(90, 110, 350, 280, arcade.csscolor.BROWN)
arcade.draw_lrtb_rectangle_filled(290, 310, 380, 270, arcade.csscolor.BROWN)
arcade.draw_lrtb_rectangle_filled(395, 410, 350, 250, arcade.csscolor.BROWN)
arcade.draw_lrtb_rectangle_filled(490, 510, 350, 290, arcade.csscolor.BROWN)

#Cercles: 
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(120, 370, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(80, 360, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(95, 385, 30, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(500, 500, 50, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(95, 495, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(130, 500, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(105, 515, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(75, 510, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(330, 460, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(360, 470, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(335, 485, 30, arcade.csscolor.WHITE)
arcade.draw_circle_filled(305, 480, 30, arcade.csscolor.WHITE)

#Arcs: 
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)

#Triangles: 
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.GREEN)

#Polígons: 
arcade.draw_polygon_filled(((500, 400),
(480, 360),
(470, 320),
(530, 320),
(520, 360)
),
arcade.csscolor.DARK_GREEN)

# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()