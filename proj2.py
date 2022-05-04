import arcade
import math

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def cielo ():
        arcade.draw_lrtb_rectangle_filled(0, 650, 700, 0, arcade.csscolor.SKY_BLUE)


def suelo ():
        arcade.draw_lrtb_rectangle_filled(0, 650, 200, 0, arcade.csscolor.GREEN)

def arbre (px,py):
        arcade.draw_lrtb_rectangle_filled(px, 30+px, 120+py, py, arcade.csscolor.BROWN)
        arcade.draw_circle_filled(25+px, 120+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(0+px, 150+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(35+px, 180+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(40+px, 160+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(50+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 130+py, 30, arcade.csscolor.DARK_GREEN)
        arcade.draw_circle_filled(5+px, 180+py, 30, arcade.csscolor.DARK_GREEN)

def nuvol ():
        arcade.draw_circle_filled(95, 395, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(130, 400, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(105, 415, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(75, 410, 30, arcade.csscolor.WHITE)

def nuvol2 ():
        arcade.draw_circle_filled(295, 375, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(330, 380, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(305, 395, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(275, 390, 30, arcade.csscolor.WHITE)

def nuvol3 ():
        arcade.draw_circle_filled(545, 375, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(580, 380, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(545, 395, 30, arcade.csscolor.WHITE)
        arcade.draw_circle_filled(515, 390, 30, arcade.csscolor.WHITE)

def lago ():
        arcade.draw_ellipse_filled(160, 100, 200, 90, arcade.csscolor.BLUE, 3)
        arcade.draw_ellipse_filled(170, 130, 210, 90, arcade.csscolor.BLUE, 3)
        arcade.draw_ellipse_filled(190, 115, 210, 90, arcade.csscolor.BLUE, 3)
        arcade.draw_ellipse_filled(140, 115, 210, 90, arcade.csscolor.BLUE, 3)
        arcade.draw_ellipse_filled(130, 100, 100, 125, arcade.csscolor.BLUE, 3)

def sol ():
        arcade.draw_circle_filled(100, 430, 50, arcade.csscolor.YELLOW)


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
        self.ball = Gel(50, 50, 0, -4, 2, arcade.color.BLUE)
        self.ball2 = Gel(150, 50, 0, -5, 2, arcade.color.BLUE)
        self.ball3 = Gel(20, 50, 0, -4.5, 2, arcade.color.BLUE)
        self.ball4 = Gel(250, 50, 0, -4.6, 2, arcade.color.BLUE)
        self.ball5 = Gel(280, 50, 0, -5.5, 2, arcade.color.BLUE)
        self.ball6 = Gel(310, 50, 0, -6, 2, arcade.color.BLUE)
        self.ball7 = Gel(350, 50, 0, -5.3,2, arcade.color.BLUE)
        self.ball8 = Gel(400, 50, 0, -7, 2, arcade.color.BLUE)
        self.ball9 = Gel(450, 50, 0, -5.2, 2, arcade.color.BLUE)
        self.ball10 = Gel(540, 50, 0, -4.2, 2, arcade.color.BLUE)
        self.ball11 = Gel(590, 50, 0, -6.2, 2, arcade.color.BLUE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        cielo()
        suelo()
        lago ()
        arbre(450,150)
        sol ()
        nuvol()
        nuvol2()
        nuvol3()
        self.ball.draw()
        self.ball2.draw()
        self.ball3.draw()
        self.ball4.draw()
        self.ball5.draw()
        self.ball6.draw()
        self.ball7.draw()
        self.ball8.draw()
        self.ball9.draw()
        self.ball10.draw()
        self.ball11.draw()
        

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        colisio(self.ball,self.ball2)
        self.ball2.update()
        self.ball.update()
        self.ball3.update()
        self.ball4.update()
        self.ball5.update()
        self.ball6.update()
        self.ball7.update()
        self.ball8.update()
        self.ball9.update()
        self.ball10.update()
        self.ball11.update()
        


def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()