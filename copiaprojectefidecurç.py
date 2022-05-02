import arcade
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


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

nuvol(300,350)

#Elipse
arcade.draw_ellipse_filled(160, 130, 200, 90, arcade.csscolor.BLUE, 3)
arcade.draw_ellipse_filled(170, 160, 210, 90, arcade.csscolor.BLUE, 3)
arcade.draw_ellipse_filled(190, 145, 210, 90, arcade.csscolor.BLUE, 3)
arcade.draw_ellipse_filled(140, 145, 210, 90, arcade.csscolor.BLUE, 3)
arcade.draw_ellipse_filled(130, 130, 100, 125, arcade.csscolor.BLUE, 3)


class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

def colisio(a,b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
    print(distancia)
    if distancia <= (a.radius):
        return True
    else:
        return False

class Gel (Ball):
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        
        
        if self.position_y < 0:
            self.position_y = SCREEN_HEIGHT

class Meteorit (Ball):
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1
        
        
        
        if self.position_y < 0:
            self.position_y = SCREEN_HEIGHT      

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)
            

                # Attributes to store where our ball is
        self.ball = Ball(50, 50, 0, -3, 20, arcade.color.WHITE)
        self.ball2 = Gel(150, 50, 0.1, -7, 20, arcade.color.WHITE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        colisio(self.ball,self.ball2)
        self.ball2.update()
        self.ball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()