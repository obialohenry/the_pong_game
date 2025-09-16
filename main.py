from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(800,600)
screen.bgcolor('black')
screen.title('The Pong Game')
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()