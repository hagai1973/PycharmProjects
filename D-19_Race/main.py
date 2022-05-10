from math import *
import turtle
import random


def move_frowards():
    t.forward(50)


def move_frowards_random(t=turtle):
    t.forward(random.randint(1, 10))


def clear_screnn(t):
    t.home()
    t.clear()


screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.setup(width=500, height=400)

colors = ["red", "orange", "green", "yellow", "blue", "purple"]
turtles = []
first_location = -70

for i in range(6):
    t_name = "t_" + str(i)
    t_name = turtle.Turtle()
    t_name.shape("turtle")
    t_name.pensize(1)
    t_name.speed('slow')
    t_name.color(colors[i])
    t_name.penup()
    first_location += 30
    t_name.goto(x=-240, y=first_location)
    turtles.append(t_name)

user_bet = screen.textinput(title="Your bet", prompt="Which color you bet on: ")
print(f"your bet is: {user_bet}")
winner = ""

while True:
    rand_turtel = random.randint(0, 5)
    t = random.choice(turtles)
    move_frowards_random(t)
    t_position = t.position()[0]
    winner = t.color()
    if int(t_position) > 230:
        winner = t.color()
        break

if winner[0].lower() == user_bet.lower():
    print(f"Your guess was right: {winner[0]} just win")
else:
    print(f"Your guess was false: {winner[0]} just win, but you bet for {user_bet}")

screen.exitonclick()
