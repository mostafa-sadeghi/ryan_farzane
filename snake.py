from turtle import Screen
from snake_utils import change_position, create_turtle, move
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


display_surface.listen()
display_surface.onkeypress(go_up, "Up")

running = True
while running:
    display_surface.update()
    move(snake_head)
    sleep(0.2)
