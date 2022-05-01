from turtle import Turtle, Screen, begin_fill, color, end_fill, done, forward, left, pos

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()
turtle.width(4)

turtle.color('coral')
# turtle.forward(100)
# turtle.forward(100)
# turtle.left(45)
# turtle.forward(200)

# use forward by 50 (default = black)
# turtle.forward(50)

# change the color of turtle
for i in range(5):

    turtle.color("yellow")

    # use forward by 50 (color = red)
    # turtle.forward(50)

    # use forward by 100 (default = black)
    turtle.forward(100)

    # change the color of turtle
    turtle.color("red")

    # use forward by 100 in 90 degrees
    # right (color = red)
    turtle.right(90)
    turtle.forward(100)

    # change the color of turtle
    turtle.color('green')

    # use forward by 100 in 90 degrees
    # right (color = blue)
    turtle.right(90)
    turtle.forward(100)

    # change the color of turtle
    turtle.color('orange')

    # use forward by 100 in 90 degrees
    # right (color = green)
    turtle.right(90)
    turtle.forward(100)


# print(screen.canvwidth)
# print(screen.canvheight)

screen.exitonclick()
