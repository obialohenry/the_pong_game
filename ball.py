from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self._x_move = 10
        self._y_move = 10

    def move(self):
        new_x = self.xcor() + self._x_move
        new_y = self.ycor() + self._y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self._y_move *= -1
