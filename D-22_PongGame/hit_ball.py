from turtle import Turtle


class HitBall(Turtle):

    def __init__(self):
        super().__init__()
        self.x_move = 15
        self.y_move = 15
        self.speed('fastest')
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 10
        self.dy = -10
        self.move_spead = 0.1

    def ball_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def ball_bounce_y(self):
        self.y_move *= -1
        self.move_spead *= 0.9

    def ball_bounce_x(self):
        self.x_move *= -1
        self.move_spead *= 0.9

    def ball_reset_location(self):
        self.goto(0, 0)
        self.ball_bounce_x()
        self.move_spead = 0.1

