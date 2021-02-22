# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Creating a window screen
window = turtle.Screen()
window.title("Snake Game 2.0")
window.bgcolor("red")

# the width and height
window.setup(width=600, height=600)
window.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
colors = random.choice(['black'])
shapes = random.choice(['triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score : 0 High Score : 0", align="center", font=("black", 24, "bold"))


# assigning key directions
def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


window.listen()
window.onkey(up, "w")
window.onkey(down, "s")
window.onkey(left, "a")
window.onkey(right, "d")

segments = []

# Gameplay
while True:
    window.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['blue'])
        shapes = random.choice(['circle'])
        for segment in segments:
            segment.goto(999, 999)
        segments[:] = []
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("SCORE : {} HIGH SCORE : {} ".format(
            score, high_score), align="center", font=("black", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")  # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("SCORE : {} HIGH SCORE : {} ".format(
            score, high_score), align="center", font=("black", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['blue'])
            shapes = random.choice(['circle'])
            for segment in segments:
                segment.goto(999, 999)
            segment.clear()

            score = 0
            delay = 0.1
            pen.clear()
            pen.write("SCORE : {} HIGH SCORE : {} ".format(
                score, high_score), align="center", font=("black", 24, "bold"))
    time.sleep(delay)

windown.mainloop()

