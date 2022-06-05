from turtle import Screen
import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.starting = STARTING_MOVE_DISTANCE
        self.goto(random.randint(280, 300), random.randint(-230, 260))
        self.go_forward(screen)

    def go_forward(self, screen):
        if -300 < self.xcor() < 300:
            new_x = self.xcor() - self.starting
            self.goto(new_x, self.ycor())
            self.starting += MOVE_INCREMENT
            screen.update()
            time.sleep(0.09)
        else:
            self.color(random.choice(COLORS))
            self.goto(random.randint(285, 300), random.randint(-220, 260))
            self.starting = STARTING_MOVE_DISTANCE
            time.sleep(0.09)
            screen.update()
