from turtle import Screen
import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.sleep_time = 0.05
        self.speed(0)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.starting = STARTING_MOVE_DISTANCE
        self.goto(random.randint(280, 300), random.randint(1, 30) * 19 - 300)
        self.go_forward(screen)

    def go_forward(self, screen):
        if -300 < self.xcor() < 300:
            new_x = self.xcor() - self.starting
            self.goto(new_x, self.ycor())
            screen.update()
            time.sleep(self.sleep_time)
        else:  # Begin again the car ride
            self.color(random.choice(COLORS))
            self.goto(random.randint(285, 300), random.randint(-220, 260))
            self.starting *= 1.5
            # self.starting = STARTING_MOVE_DISTANCE
            # self.sleep_time -= 0.01
            screen.update()
