import colorgram
import turtle
import random

# colors = colorgram.extract('image.jpg', 30)
#
# first_color = colors[0]
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = r, g, b
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)
colors = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83),
          (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47),
          (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186),
          (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82),
          (46, 73, 62), (47, 66, 82)]

t = turtle.Turtle()


def dots():
    for _ in range(17):
        t.dot(20, random.choice(colors))
        t.penup()
        t.forward(50)

t.speed("fastest")
t.shape("turtle")
number_of_lines = 15
t.hideturtle()
t.penup()
i = -350
for dot in range(number_of_lines):
    t.setposition(-400, i)
    dots()
    i += 50




screen = turtle.Screen()
screen.exitonclick()
