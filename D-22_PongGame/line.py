from turtle import Screen
from turtle import Turtle

MOVE_DISTANCE = 20


class Line(Turtle):

    def __init__(self, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.penup()
        self.goto(0, y_cor)

    @staticmethod
    def centrl_line():
        line1 = Line(300)
        line2 = Line(150)
        line3 = Line(0)
        line4 = Line(-150)
        line5 = Line(-300)
