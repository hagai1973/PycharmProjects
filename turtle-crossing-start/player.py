from turtle import Screen
from turtle import Turtle

STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed(0)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.y_move = 10
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def turtle_move(self):
        y_cor = self.ycor() + self.y_move
        self.goto(0, y_cor)
        # if self.ycor() > FINISH_LINE_Y:
        #     self.turtle_reset()

    def turtle_reset(self):
        self.goto(STARTING_POSITION)
