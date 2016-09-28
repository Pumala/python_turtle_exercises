from turtle import *
from all_shapes import *
import random

speed(0)
bgcolor("black")

for i in range(200):
    height = window_height()
    width = window_width()
    random_spot = random.randint(50, 300)
    random_size = random.randint(25, 100)
    random_left = random.randint(10, 180)
    random_right = random.randint(10, 180)
    star_outline(random_size, True, "yellow")
    print position()
    if abs(position()[1] * 2) > window_height or abs(position()[0]) > window_width:
        home()
    up()
    forward(random_spot)
    left(random_left)
    right(random_right)
    down()

mainloop()
