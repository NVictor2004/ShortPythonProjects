import turtle

def F():
    return "F+F--F+F"

axiom = "F"
new = ""
n = 6

for i in range(n):
    for i in axiom:
        if i == "F":
            new = new + F()
        else:
            new = new + i
    axiom = new
    new = ""

# to generate length of snowflake: (3 ** n) * forward

turtle.hideturtle()
turtle.delay(500)
turtle.penup()
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(600)
turtle.right(180)
turtle.pendown()

turtle.delay(0)

forward = 1200 / (3 ** n)
for i in axiom:
    if i == "F":
        turtle.forward(forward)
    elif i == "+":
        turtle.left(60)
    elif i == "-":
        turtle.right(60)
