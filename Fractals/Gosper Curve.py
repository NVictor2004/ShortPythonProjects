import turtle

def A():
    return "A-B--B+A++AA+B-"

def B():
    return "+A-BB--B-A++A+B"

axiom = "A"
new = ""
n = 5
forward = 4
# 4, forward = 11-12
#3, forward = 30, 315, 10
#2, forward = 90, 315, 175
#1, forward = 360, 315, 450

for i in range(n):
    for i in axiom:
        if i == "A":
            new = new + A()
        elif i == "B":
            new = new + B()
        else:
            new = new + i
    axiom = new
    new = ""
turtle.penup()
turtle.left(90)
turtle.forward(315)
turtle.right(90)
turtle.backward(0)
turtle.pendown()
turtle.delay(0)
turtle.hideturtle()
for i in axiom:
    if i == "A":
        turtle.forward(forward)
    if i == "B":
        turtle.forward(forward)
    if i == "+":
        turtle.left(60)
    if i == "-":
        turtle.right(60)
