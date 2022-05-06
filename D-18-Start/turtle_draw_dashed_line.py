import turtle
import random

t = turtle.Turtle()
t.shape("circle")
t.color("black")


def draw_dashed():
    for _ in range(15):
        t.forward(6)
        t.penup()
        t.forward(6)
        t.pendown()


def draw_line():
    for _ in range(4):
        t.pendown()
        t.forward(6)


t.penup()
t.goto(-450, 350)

for _ in range(3):
    # t.right(90)
    draw_dashed()
    # draw_line()
screen = turtle.Screen()
screen.exitonclick()
