from turtle import Turtle

# Constant:
ALIGN = "right"
FONT = "Courier"
FONT_SIZE = 14
STYLE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Score:" + str(self.score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write("Final Score:" + str(self.score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
        self.goto(0, 0)
        self.write("Game Over", True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))

