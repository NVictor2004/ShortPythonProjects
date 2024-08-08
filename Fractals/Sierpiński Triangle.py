import turtle

def triangle(points):
    turtle.penup()
    turtle.goto(points[0][0], points[0][1])
    turtle.pendown()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])

def midpoint(points):
    new = []
    x = (points[0][0] + points[1][0]) / 2
    y = (points[0][1] + points[1][1]) / 2
    new.append([x, y])
    x = (points[0][0] + points[2][0]) / 2
    y = (points[0][1] + points[2][1]) / 2
    new.append([x, y])
    x = (points[1][0] + points[2][0]) / 2
    y = (points[1][1] + points[2][1]) / 2
    new.append([x, y])
    return new

def sierpinski(points):
    new = midpoint(points)
    turtle.begin_fill()
    triangle(new)
    turtle.end_fill()
    return new

def sierpinski_set(points, num):
    new = sierpinski(points)
    if num > 0:
        sierpinski_set([points[0], new[0], new[1]], num - 1)
        sierpinski_set([points[1], new[0], new[2]], num - 1)
        sierpinski_set([points[2], new[1], new[2]], num - 1)


points = [[-350,-300],[0,300],[350,-300]]
detail = 6
turtle.hideturtle()

turtle.delay(500)
turtle.penup()
turtle.forward(100)
turtle.back(100)
turtle.forward(100)
turtle.back(100)
turtle.pendown()

turtle.delay(0)
turtle.fillcolor("black")
turtle.begin_fill()
triangle(points)
turtle.end_fill()
turtle.fillcolor("white")
sierpinski_set(points, detail)
