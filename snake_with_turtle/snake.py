from turtle import Screen
from snake_utils import *
from time import sleep


score = 0
high_score = 0

display_surface = Screen()
display_surface.bgcolor("black")
display_surface.setup(600, 600)
display_surface.title("Snake Game")
display_surface.tracer(False)

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position(snake_food)

score_board = create_turtle("square", "white")
score_board.ht()
score_board.goto(0, 260)
score_board.write(
    f"Score: {score}, HighScore:{high_score}", align="center", font=("arial", 22))
draw = create_turtle("turtle", "white")
draw.goto(-300, 230)
draw.pendown()
draw.forward(600)


def go_up():
    if (snake_head.direction != "down" and snake_tails) or (not snake_tails):
        snake_head.direction = "up"


def go_down():
    if (snake_head.direction != "up" and snake_tails) or (not snake_tails):
        snake_head.direction = "down"


def go_right():
    if (snake_head.direction != "left" and snake_tails) or (not snake_tails):
        snake_head.direction = "right"


def go_left():
    if (snake_head.direction != "right" and snake_tails) or (not snake_tails):
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


def reset():
    snake_head.home()
    snake_head.direction = ""
    for tail in snake_tails:
        tail.ht()
    snake_tails.clear()


def on_close():
    global running
    running = False


root = display_surface._root
root.protocol("WM_DELETE_WINDOW", on_close)
root.resizable(False, False)

running = True
while running:
    display_surface.update()
    score_board.clear()
    score_board.write(
        f"Score: {score}, HighScore:{high_score}", align="center", font=("arial", 22))
    if snake_head.distance(snake_food) < 20:
        change_position(snake_food)
        new_tail = create_turtle("square", "green")
        snake_tails.append(new_tail)
        score += 1
        if score > high_score:
            high_score = score

    for i in range(len(snake_tails)-1, 0, -1):
        xpos = snake_tails[i-1].xcor()
        ypos = snake_tails[i-1].ycor()
        snake_tails[i].goto(xpos, ypos)
    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())

    if snake_head.xcor() < -290 or snake_head.xcor()snake_head.ycor() > 210 or snake_head.ycor() < -290:
        reset()
        score = 0

    move(snake_head)

    for tail in snake_tails:
        if tail.distance(snake_head) < 20:
            reset()
            score = 0

    sleep(0.2)
