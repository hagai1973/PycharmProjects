import pandas
import csv
import turtle
import time
import datetime

from scoreboard import Scoreboard

data = pandas.read_csv("50_states1.csv")

screen = turtle.Screen()
screen.title("USA states quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle_new = turtle.Turtle()
turtle_new.penup()
turtle_new.hideturtle()
game_on = True
scoreboard = Scoreboard()
scoreboard.create_scoreboard()
is_correct = False
total_possible = 0
guessed_states = []
not_guessed_states = []
all_states = data.state.to_list()

while scoreboard.attempts > 0:

    answer_state = screen.textinput(title=f"{total_possible} / {len(guessed_states)} states correct",
                                    prompt="What is another state name?: ")
    state_data = data[data['state'] == answer_state.title()]

    if answer_state.title() == "Exit":
        for state in all_states:
            if not (state in guessed_states):
                not_guessed_states.append(state)
        df = pandas.DataFrame(not_guessed_states, columns=["state"])
        df.to_csv("not_guessed_states.csv")
        break

    if len(state_data) == 1:
        guessed_states.append(answer_state.capitalize())
        # print(int(state_data.x))
        # print(int(state_data.y))
        # print(answer_state)
        turtle_new.goto(int(state_data.x), int(state_data.y))
        turtle_new.color("black")
        turtle_new.write(f"{answer_state}", font=("Courier", 6, "normal"))
        scoreboard.add_score()
        scoreboard.add_attempts()


    else:
        scoreboard.add_attempts()

    total_possible += 1

# Way to find out x, y
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
