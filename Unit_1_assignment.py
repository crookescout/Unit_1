import turtle
turtle.speed(0)

turtle.pencolor("violet")
turtle.pensize(2)

#rotating pink hexagon
def makeAhexagon():
    for x in range(6):
        turtle.forward(100)
        turtle.left(60)

#circle
def makeAoctagon():
    for x in range(8):
        turtle.forward(100)
        turtle.left(45)

for y in range(18):
    makeAhexagon()
    turtle.left(20)

turtle.pencolor("medium slate blue")
turtle.pensize(2)

for z in range(12):
    makeAoctagon()
    turtle.left(30)


turtle.exitonclick()