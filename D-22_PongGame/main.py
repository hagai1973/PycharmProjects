import time
from line import Line

from paddle import Paddle
from hit_ball import HitBall
from turtle import *
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")

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
    if hit_ball.distance(right_padle) < 50 and hit_ball.xcor() > 365:
        hit_ball.ball_bounce_x()

    # detect collision with left padle
    if hit_ball.distance(left_padle) < 50 and hit_ball.xcor() < -325:
        hit_ball.ball_bounce_x()
    # ball pass left border
    if hit_ball.xcor() < -500:
        scoreboard.add_score_to_right()
        hit_ball.ball_reset_location()
        game_speed = 0.1
    if hit_ball.xcor() > 500:
        scoreboard.add_score_to_left()
        hit_ball.ball_reset_location()
        game_speed = 0.1
    if scoreboard.right_score > 2:
        game_is_on = False
        scoreboard.game_over("right")
    if scoreboard.left_score > 2:
        game_is_on = False
        scoreboard.game_over("left")

    time.sleep(game_speed)
    screen.listen()

screen.exitonclick()
