# By Scout Crooke, 9/17/19, this program draws 2 geometrical flowers

import turtle
turtle.speed(0)
turtle.pensize(1)


def make_hexagon(color):
    turtle.color(color)
    for x in range(6):
        turtle.forward(50)
        turtle.left(60)


def make_octagon(size, color):
    turtle.color(color)
    for x in range(8):
        turtle.forward(size)
        turtle.left(45)


def make_square(size, color):
    turtle.color(color)
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)


def goto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# rotating hexagon in a circle
for z in range(18):
    make_hexagon("violet")
    turtle.left(20)

# rotating octagon in a circle
for z in range(18):
    make_octagon(50, "medium slate blue")
    turtle.left(20)

goto(200, 200)

# rotating oxagon in a circle
for z in range(8):
    make_octagon(50, "pink")
    turtle.left(45)

# rotating hexagon in a circle
for z in range(8):
    make_hexagon("light blue")
    turtle.left(45)

goto(-200, 200)

# rotating oxtagon in a circle
for z in range(10):
    make_octagon(50, "sky blue")
    turtle.left(36)

# rotating hexagon in a circle
for z in range(10):
    make_hexagon("royal blue")
    turtle.left(36)

goto(-200, -200)

# rotating square in a circle
for z in range(10):
    make_square(50, "cyan")
    turtle.left(36)

# rotating hexagon in a circle
for z in range(10):
    make_hexagon("powder blue")
    turtle.left(36)

goto(200, -200)

# rotating square in a circle
for z in range(18):
    make_square(80, "misty rose")
    turtle.left(20)

# rotating hexagon in a circle
for z in range(10):
    make_octagon(40, "lavender")
    turtle.left(36)


turtle.exitonclick()