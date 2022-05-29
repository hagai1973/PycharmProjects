import time
import turtle
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

screen.listen()
# screen.onkey(paddle.up, "Up")
# screen.onkey(paddle.down, "Left")

right_padle = Paddle(470)
left_padle = Paddle(-470)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5


game_is_on = True
game_speed = 0.1

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    screen.listen()
    screen.onkey(right_padle.go_up, "Up")
    screen.onkey(right_padle.go_down, "Down")

screen.exitonclick()
