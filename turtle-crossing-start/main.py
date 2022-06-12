import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

START_NUMBER_OF_CARS = 6
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Game")
scoreboard = Scoreboard()
scoreboard.update_score()
player = Player()
screen.onkey(player.turtle_move, "Up")
index = 0
screen.update()
game_is_on = True

cars_1 = list()
cars_2 = list()

for x in range(START_NUMBER_OF_CARS):
    cars_1.append(CarManager(screen))

while game_is_on:
    screen.listen()
    for car in cars_1:
        cars_1[random.randint(0, len(cars_1) - 1)].go_forward(screen)
        if player.distance(car) < 30:
            player.turtle_reset()
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > player.finish_line - 5:
        player.turtle_reset()
        scoreboard.add_score()
        cars_1.append(CarManager(screen))
        scoreboard.update_score()

    screen.update()

screen.exitonclick()
