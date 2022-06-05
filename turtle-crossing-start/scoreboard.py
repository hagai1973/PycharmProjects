from turtle import Turtle

FONT = ("Courier", 10, "normal")
# Constant:
ALIGN = "center"
FONT = "Courier"
FONT_SIZE = 24
STYLE = "bold"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.goto(-10, 260)
        self.hideturtle()
        self.color("black")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: " + str(self.score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Final Score: " + str(self.score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
        self.goto(0, 0)
        self.write(f" Game Over ", True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
