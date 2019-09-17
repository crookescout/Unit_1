# By Scout Crooke, 9/17/19, this program draws 2 geometrical flowers

import turtle
turtle.speed(0)
turtle.pensize(1)

def makeAhexagon(color):
    turtle.color(color)
    for x in range(6):
        turtle.forward(50)
        turtle.left(60)

def makeAoctagon(size, color):
    turtle.color(color)
    for x in range(8):
        turtle.forward(size)
        turtle.left(45)

def makeAsquare(size, color):
    turtle.color(color)
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)

# rotating hexagon in a circle
for y in range(18):
    makeAhexagon("violet")
    turtle.left(20)

# rotating octagon in a circle
for z in range(18):
    makeAoctagon(50, "medium slate blue")
    turtle.left(20)

turtle.penup()
turtle.goto(200, 200)
turtle.pendown()

# rotating oxagon in a circle
for y in range(8):
    makeAoctagon(50, "pink")
    turtle.left(45)

# rotating hexagon in a circle
for z in range(8):
    makeAhexagon("light blue")
    turtle.left(45)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()

# rotating oxtagon in a circle
for y in range(10):
    makeAoctagon(50, "sky blue")
    turtle.left(36)

# rotating hexagon in a circle
for z in range(10):
    makeAhexagon("royal blue")
    turtle.left(36)

turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()

# rotating square in a circle
for y in range(10):
    makeAsquare(50, "cyan")
    turtle.left(36)

# rotating hexagon in a circle
for z in range(10):
    makeAhexagon("powder blue")
    turtle.left(36)

turtle.penup()
turtle.goto(200, -200)
turtle.pendown()

# rotating square in a circle
for y in range(18):
    makeAsquare(80, "misty rose")
    turtle.left(20)

# rotating hexagon in a circle
for z in range(10):
    makeAoctagon(40, "lavender")
    turtle.left(36)


turtle.exitonclick()