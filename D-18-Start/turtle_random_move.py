import turtle
import random

t = turtle.Turtle()
direction = ["left", "right"]
angles = [0, 90, 180, 270]
t.shape("circle")
t.pensize(15)
t.speed("fastest")


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    random_color_tuple = (r, g, b)
    return random_color_tuple


def random_distance():
    return random.randint(5, 50)


def random_angle():
    return random.randint(1, 360)


def random_move():
    t.color(random_color())
    t.setheading(random.choice(angles))
    angele = random.choice(angles)
    # if random.choice(direction) == "right":
    #     t.right(angele)
    # else:
    #     t.left(angele)
    # t.forward(random_distance())
    t.forward(30)


for _ in range(100):
    random_move()

screen = turtle.Screen()
screen.exitonclick()
