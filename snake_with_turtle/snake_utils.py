from turtle import Turtle
from random import randint


def create_turtle(tshape, tcolor):
    my_turtle = Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    my_turtle.speed("fastest")
    return my_turtle


def change_position(object):
    xpos = randint(-270, 270)
    ypos = randint(-270, 210)
    object.goto(xpos, ypos)


def move(snake_head):
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        ypos += 20
        snake_head.sety(ypos)

    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        ypos -= 20
        snake_head.sety(ypos)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        xpos += 20
        snake_head.setx(xpos)

    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        xpos -= 20
        snake_head.setx(xpos)
