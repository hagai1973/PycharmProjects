import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
game_speed = 0.5

while game_is_on:
    screen.update()
    time.sleep(game_speed)
    snake.move()
    # Detect collision with food:
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.append_snake()
        if game_speed > 0.2:
            game_speed -= 0.1

    # Detected collision
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    # if head collides with any segment of sanke
    # Game over
    index = 0
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
