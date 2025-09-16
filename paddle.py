from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
HEIGHT = 5
WIDTH = 1

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.position = position
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=HEIGHT,stretch_len=WIDTH)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)

