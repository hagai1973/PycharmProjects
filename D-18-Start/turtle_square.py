import turtle
import random

import heroes as heroes
import villains

print(heroes.gen())
print(villains.gen())
t = turtle.Turtle()
t.shape("circle")

# t.color('navy')
COLORS = ['red', 'orange', 'yellow', 'green', 'blue']





for i in range(4):
    # R = random.random()
    # B = random.random()
    # G = random.random()
    t.color(random_color())
    t.right(270)
    t.forward(100)

# t.left(90)
# t.forward(300)

# for i in range(3):
#     t.color(random.choice(COLORS))
#     t.right(270)
#     t.forward(100)

screen = turtle.Screen()
screen.exitonclick()
