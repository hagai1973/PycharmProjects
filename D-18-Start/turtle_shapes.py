import turtle
import random


def random_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return [R, G, B]


t = turtle.Turtle()
t.shape("circle")

t.color(random_color())


def go_to_base():
    t.penup()
    t.position(0)
    t.pendown()


def draw_triangel():
    # base
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)


def draw_square():
    for i in range(4):
        t.color(random_color())
        t.right(270)
        t.forward(100)


def draw_pentagon():
    for i in range(5):
        t.color(random_color())
        t.left(72)
        t.forward(100)


def draw_hexagon():
    for i in range(6):
        t.color(random_color())
        t.left(60)
        t.forward(100)


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        t.color(random_color())
        t.left(angle)
        t.forward(100)


for i in range(3, 11):
    draw_shape(i)

screen = turtle.Screen()
screen.exitonclick()
