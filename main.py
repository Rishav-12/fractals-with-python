"""

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

LEVELS = 5
ANGLE = 30
INIT_LENGTH = 70

def draw_tree(levels, angle, length):

    if levels == 0:
        turtle.stamp()
        return
    turtle.right(angle)
    turtle.forward(length)
    draw_tree(levels - 1, angle, length*0.8) # each branch is 0.8 times the length of its parent
    turtle.back(length)
    turtle.left(2*angle)
    turtle.forward(length)
    draw_tree(levels - 1, angle, length*0.8) # each branch is 0.8 times the length of its parent
    turtle.back(length)
    turtle.right(angle)

turtle.speed(7)
turtle.width(4)
turtle.color("green")
turtle.shape("circle")
turtle.hideturtle()
turtle.left(90)
turtle.forward(INIT_LENGTH) # draw the stem
draw_tree(LEVELS, ANGLE, INIT_LENGTH*0.8) # each branch is 0.8 times the length of its parent

turtle.mainloop()