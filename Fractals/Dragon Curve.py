import turtle
import time

turns = [90]
addition = []
forward = 3

for i in range(1, 15):#creates L and R sequence
    print(i, "calculations Done")
    for i in range(len(turns), 0, -1): # what to add on
        if turns[i - 1] == 90:
            addition.append(-90)
        else:
            addition.append(90)
    turns = turns + [90] + addition
    addition = []


print("L/R Sequence created with", len(turns), "sides")
print("Creating Dragon...")

turtle.hideturtle()

turtle.penup()
turtle.delay(300)
turtle.forward(130)
turtle.right(90)
turtle.back(195)
turtle.right(90)
turtle.pendown()

turtle.delay(0)

for i in turns:
    turtle.forward(3)
    turtle.right(i)
turtle.forward(3)
print("Done!")
