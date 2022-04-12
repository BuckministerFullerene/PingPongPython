import turtle
import winsound

# create a window and name it wn
wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("#731C12")
wn.setup(width=800, height=600)
# prevents window from refreshing
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
# animation refresh speed, set to max speed
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# stretch the paddle size (5*20) px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# prevent it drawing lines
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
# animation refresh speed, set to max speed
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# stretch the paddle size (5*20) px
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# prevent it drawing lines
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
# animation refresh speed, set to max speed
ball.speed(0)
ball.shape("circle")
ball.color("white")
# prevent it drawing lines
ball.penup()
ball.goto(0, 0)
# change (d) along x, speed
ball.dx = 0.3
ball.dy = 0.3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
# start at center
pen.penup()
# hides pen
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Ocr A Std", 15, "normal"))


# function to move the paddles
def paddle_a_up():
    # ycor returns the y coordinate, part of the turtle module
    y = paddle_a.ycor()
    # set movement along y-axis
    y += 20
    # set paddle_a to that position
    paddle_a.sety(y)


def paddle_a_down():
    # ycor returns the y coordinate, part of the turtle module
    y = paddle_a.ycor()
    # set movement along y-axis
    y -= 20
    # set paddle_a to that position
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
# listen for keyboard input
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    # 290 based on height of frame/2
    if ball.ycor() > 290:
        winsound.PlaySound("pong_wall.wav", winsound.SND_ASYNC)
        ball.sety(290)
        # reset direction to opposite direction
        ball.dy *= -1

    if ball.ycor() < -280:
        winsound.PlaySound("pong_wall.wav", winsound.SND_ASYNC)
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        winsound.PlaySound("pong_score.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # clears previous score
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ocr A Std", 15, "normal"))

    if ball.xcor() < -390:
        winsound.PlaySound("pong_score.wav", winsound.SND_ASYNC)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ocr A Std", 15, "normal"))

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        winsound.PlaySound("pong_paddle.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() < -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        winsound.PlaySound("pong_paddle.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1
