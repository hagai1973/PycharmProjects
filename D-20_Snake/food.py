from turtle import Turtle
from random import random, randint

# Constant:
LOCATION_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()



    def create_food(self):
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5, 0)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def random_location(self):
        w = randint(-280, 280)
        h = randint(-280, 280)
        return w, h

    def refresh(self):
        self.goto(self.random_location())
