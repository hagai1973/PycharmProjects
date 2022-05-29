from turtle import Screen
from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.create_paddle(x_cor)

    def create_paddle(self, x_cor):
        # Right paddle
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, 0)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < 280:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y > -250:
            self.goto(self.xcor(), new_y)
