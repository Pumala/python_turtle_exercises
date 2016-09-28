from turtle import *

#  Equilateral Triangle
def triangle():
    for i in range(0, 3):
        forward(100)
        left(120)

#  Square
def square():
    for i in range(0, 4):
        forward(100)
        left(90)

#  Pentagon
def pentagon():
    for i in range(0, 4):
        forward(100)
        left(72)

    forward(100)

# Hexagon
def hexagon():
    for i in range(0, 6):
        forward(100)
        left(60)

    forward(100)

#  Octagon
def octagon():
    for i in range(0, 8):
        forward(100)
        left(45)

        forward(100)

# Star
def star():
    left(36)
    for i in range(0, 4):
        forward(300)
        left(144)

    forward(300)

# Circle
def circle():
    for i in range(360):
        left(1)
        forward(1)

# mainloop()
