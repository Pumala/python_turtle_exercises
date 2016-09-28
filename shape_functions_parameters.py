from turtle import *

#  Equilateral Triangle
def triangle(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    # all_shapes.triangle()
    for i in range(0, 3):
        forward(size)
        left(120)
    end_fill()

#  Square
def square(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    for i in range(0, 4):
        forward(size)
        left(90)
    end_fill()

#  Pentagon
def pentagon(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    for i in range(0, 4):
        forward(size)
        left(72)
    end_fill()

    forward(size)

# Hexagon
def hexagon(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    for i in range(0, 6):
        forward(size)
        left(60)
    end_fill()

    forward(size)

#  Octagon
def octagon(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    for i in range(0, 8):
        forward(size)
        left(45)
    end_fill()

    forward(size)

# Star
def star(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    left(36)
    for i in range(0, 4):
        forward(size)
        left(144)
    end_fill()

    forward(size)

# Star Outline
def star_outline(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    left(36)
    for i in range(0, 5):
        forward(size)
        right(72)
        forward(size)
        left(144)
    end_fill()

# Circle
def circle(size, fill, color):
    if fill:
        fillcolor(color)
        begin_fill()
    for i in range(360):
        left(1)
        forward(size)
    end_fill()

# mainloop()
