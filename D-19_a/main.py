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


# spiral()

def move_frowards():
    t.forward(50)


def move_backwards():
    t.backward(50)


def move_counter_clockwise():
    t.circle(r, 60)


def move_clockwise():
    t.circle(r, -60)


def clear_screnn():
    t.home()
    t.clear()


def turn_left():
    current_heading = t.heading()
    t.setheading(current_heading + 10)
    t.forward(50)


def turn_right():
    current_heading = t.heading()
    t.setheading(current_heading - 10)
    t.forward(50)



screen = turtle.Screen()
screen.listen()
screen.onkey(key="w", fun=move_frowards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right)
screen.onkey(key="c", fun=clear_screnn)

screen.exitonclick()
