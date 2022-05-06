from math import *
import turtle
import random

t = turtle.Turtle()
direction = ["left", "right"]
angles = [0, 90, 180, 270]
t.shape("circle")
t.pensize(1)
t.speed(0)
ANGLE = 8
r = 100


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    random_color_tuple = (r, g, b)
    return random_color_tuple


def draw_circle():
    t.color(random_color())
    t.circle(r)


def spiral():
    t.speed("fastest")
    for _ in range(360 // ANGLE):
        t.color(random_color())
        turtle.circle(r)
        current_heading = turtle.heading()
        # turtle.left(ANGLE)
        turtle.setheading(current_heading + ANGLE)


spiral()

screen = turtle.Screen()
screen.exitonclick()
