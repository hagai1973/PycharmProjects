from turtle import Turtle

# Constant:
LOCATION_START = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.move_speed = 0
        self.create_snake()
        self.head = self.segments[0]
        self.last = self.segments[-1]

    def create_snake(self):
        for postion in LOCATION_START:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(postion)
            new_segment.speed(0)
            self.segments.append(new_segment)

    def append_snake(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.last.position())
        self.segments.append(new_segment)

    def move(self):
        for item in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[item - 1].xcor()
            new_y = self.segments[item - 1].ycor()
            self.segments[item].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
