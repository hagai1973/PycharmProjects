from turtle import Turtle

# Constant:
ALIGN = "right"
FONT = "Courier"
FONT_SIZE = 15
STYLE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200, 270)
        self.write("Left Score:  " + str(self.left_score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
        self.penup()
        self.goto(300, 270)
        self.write("Right Score:  " + str(self.right_score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))

    def add_score_to_right(self):
        self.right_score += 1
        self.update_score()

    def add_score_to_left(self):
        self.left_score += 1
        self.update_score()

    def game_over(self, who_won):
        self.clear()
        # self.goto(-200, 270)
        # self.write(f"Right side:" + str(self.right_score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
        # self.penup()
        # self.goto(300, 270)
        # self.write(f"Left side:" + str(self.left_score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
        self.penup()
        self.goto(-40, 0)
        self.write("Game Over", True, align=ALIGN, font=(FONT, 20, STYLE))
        self.goto(20, -100)
        self.write(f"{who_won} is the winner", True, align=ALIGN, font=(FONT, 20, STYLE))
