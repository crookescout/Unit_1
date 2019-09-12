import turtle
turtle.speed(0)

#triangle
for x in range(3):
    turtle.forward(100)
    turtle.left(120)

turtle.penup()
turtle.forward(150)
turtle.pencolor("purple")
turtle.pendown()

#square
for x in range(4):
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.back(300)
turtle.pencolor("blue")
turtle.pendown()

#pentagon
for x in range(5):
    turtle.forward(100)
    turtle.left(72)

turtle.penup()
turtle.back(100)
turtle.pencolor("pink")
turtle.pendown()

turtle.circle(40)

turtle.penup()
turtle.back(150)
turtle.pencolor("orange")
turtle.pendown()

#star
for x in range(5):
    turtle.forward(100)
    turtle.right(144)

turtle.penup()
turtle.left(50)
turtle.forward(300)
turtle.pendown()

#rotating square
for y in range(3):
    for x in range(4):
        turtle.fd(100)
        turtle.left(90)
    turtle.left(20)

turtle.penup()
turtle.right(110)
turtle.forward(150)
turtle.pendown()

#neighborhood of houses
def draw_house():

    #triangle roof of house
    turtle.color("blue")
    turtle.begin_fill()
    for x in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.pendown()

    #square of house
    turtle.color("purple")
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

draw_house()

turtle.penup()
turtle.left(90)
turtle.forward(120)

draw_house()

turtle.penup()
turtle.left(90)
turtle.forward(120)

draw_house()

turtle.penup()
turtle.left(90)
turtle.forward(120)

draw_house()

turtle.exitonclick()