from turtle import Screen
from snake_utils import *
from time import sleep

display_surface = Screen()
display_surface.bgcolor("black")
display_surface.setup(600, 600)
display_surface.title("Snake Game")
display_surface.tracer(False)

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)


def go_up():
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_right():
    snake_head.direction = "right"
def go_left():
    snake_head.direction = "left"


display_surface.listen()
display_surface.onkeypress(go_up, "Up")
display_surface.onkeypress(go_down, "Down")
display_surface.onkeypress(go_right, "Right")
display_surface.onkeypress(go_left, "Left")
display_surface.onkeypress(go_up, "w")
display_surface.onkeypress(go_down, "s")
display_surface.onkeypress(go_right, "d")
display_surface.onkeypress(go_left, "a")

snake_tails = list()

running = True
while running:
    display_surface.update()
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails)-1, 0, -1):
        xpos = snake_tails[i-1].xcor()
        ypos = snake_tails[i-1].ycor()
        snake_tails[i].goto(xpos, ypos)
    if len(snake_tails)>0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    move(snake_head)
    sleep(0.2)
