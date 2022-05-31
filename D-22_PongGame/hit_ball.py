from turtle import Screen
from turtle import Turtle
import time

MOVE_DISTANCE = 20


class HitBall(Turtle):

    def __init__(self):
        super().__init__()
        self.is_bounce_up = False
        self.is_bounce_bottom = True
        self.is_bounce_right = False
        self.is_bounce_left = False
        self.x_move = 10
        self.y_move = 10
        self.speed(40)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = -10

    def ball_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def ball_bounce_y(self):
        self.y_move *= -1

    def ball_bounce_x(self):
        self.x_move *= -1
