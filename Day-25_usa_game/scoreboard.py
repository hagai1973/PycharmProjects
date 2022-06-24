from turtle import Turtle

# Constant:
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.attempts = 11
        # self.get_high_score_from_file()
        self.create_scoreboard()

    def get_high_score_from_file(self):
        with open("data.txt") as file:
            high_score = int(file.read())
            print(f"data: {high_score}")
            self.high_score = high_score

    def set_high_score_from_file(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def create_scoreboard(self):
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.color("black")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}, | Remain Attempts: {self.attempts}",
                   align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def add_attempts(self):
        self.attempts -= 1
        self.update_score()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            self.set_high_score_from_file()

        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.write("Final Score:" + str(self.score), True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
    #     self.goto(0, 0)
    #     self.write("Game Over", True, align=ALIGN, font=(FONT, FONT_SIZE, STYLE))
