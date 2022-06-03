import time
from turtle import Screen, Turtle
from line import Line

from paddle import Paddle
from hit_ball import HitBall
from turtle import *
from scoreboard import Scoreboard
import turtle

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

# screen.listen()
# screen.onkey(paddle.up, "Up")
# screen.onkey(paddle.down, "Left")

# line1 = Line(300)
# line2 = Line(150)
# line3 = Line(0)
# line4 = Line(-150)
# line5 = Line(-300)

Line.centrl_line()
scoreboard = Scoreboard()
screen.update()



right_padle = Paddle(470)
left_padle = Paddle(-480)
hit_ball = HitBall()

game_is_on = True
game_speed = 0.1
screen.onkey(right_padle.go_up, "Up")
screen.onkey(right_padle.go_down, "Down")
screen.onkey(left_padle.go_up, "w")
screen.onkey(left_padle.go_down, "s")

while game_is_on:
    # time.sleep(0.1)
    screen.update()
    hit_ball.ball_move()
    # detect collision with wall
    if hit_ball.ycor() > 280 or hit_ball.ycor() < -280:
        hit_ball.ball_bounce_y()
    # detect collision with right padle
    if hit_ball.distance(right_padle) < 40 and hit_ball.xcor() > 340:
        hit_ball.ball_bounce_x()
    # detect collision with left padle
    if hit_ball.distance(left_padle) < 40 and hit_ball.xcor() < -330:
        hit_ball.ball_bounce_x()
    if hit_ball.xcor() < -500:
        print("point to the rigt side")
        scoreboard.add_score_to_right()
        hit_ball.goto(0, 0)
    if hit_ball.xcor() > 500:
        scoreboard.add_score_to_left()
        hit_ball.goto(0, 0)
    if scoreboard.right_score > 1:
        scoreboard.game_over("right")
        game_is_on = False
    if scoreboard.left_score > 1:
        scoreboard.game_over("left")
        game_is_on = False

    time.sleep(game_speed)
    screen.listen()

screen.exitonclick()
