import turtle
import time

#to generate length of variable code: (4 ** level) - 1
#to generate side length of square: (2 ** level) - 1

code = "RR"
level = 7
forward = 3


def letter_swap(code):
    new_code = ""
    for i in code:
        if i == "R":
            new_code = new_code + "L"
        if i == "L":
            new_code = new_code + "R"
        if i == "S":
            new_code = new_code + "S"
    return new_code

if level % 2 == 0:
    turtle.left(90)



turtle.delay(500)
turtle.hideturtle()

for i in range(2,level + 1):
    if not i % 2 == 0:
        code = letter_swap(code) + "SR" + code + "SS" + code + "RS" + letter_swap(code)
    if i % 2 == 0:
        code = letter_swap(code) + "RS" + code + "LL" + code + "SR" + letter_swap(code)

side_length = 2 ** level - 1
side_length = side_length * forward

if level % 2 == 0:
    turtle.penup()
    turtle.right(90)
    turtle.forward(side_length / 2)
    turtle.right(90)
    turtle.forward(side_length / 2)
    turtle.right(180)
    turtle.pendown()
else:
    turtle.penup()
    turtle.forward(side_length / 2)
    turtle.left(90)
    turtle.forward(side_length / 2)
    turtle.right(180)
    turtle.pendown()

turtle.delay(0)

for i in code:
    turtle.forward(forward)
    if i == "R":
        turtle.right(90)
    elif i == "L":
        turtle.right(-90)
turtle.forward(forward)
