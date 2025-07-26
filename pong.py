import turtle
import os

# Initialize the main window
wind = turtle.Screen()
wind.title("Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)
# Turns off the screen updates for better performance
wind.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle A
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# Ball's speed in x direction
ball.dx = 0.1 
# Ball's speed in y direction
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    # Get the current y-coordinate of paddle A and move it up
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Function to move paddle A up
def paddle_a_down():
    # Get the current y-coordinate of paddle A and move it up
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    # Function to move paddle B up
def paddle_b_up():
    # Get the current y-coordinate of paddle B and move it up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

# Function to move paddle A up
def paddle_b_down():
    # Get the current y-coordinate of paddle B and move it down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard bindings
wind.listen()
wind.onkeypress(paddle_a_up, "w")
wind.onkeypress(paddle_a_down, "s")
wind.onkeypress(paddle_b_up, "Up")
wind.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    # Update the screen
    wind.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("start /min wmplayer bounce.wav")
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("start /min wmplayer bounce.wav")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal")) 

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 60 < ball.ycor() < paddle_b.ycor() + 60):
        ball.setx(340)
        ball.dx *= -1
        os.system("start /min wmplayer bounce.wav")
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
        ball.setx(-340)
        ball.dx *= -1
        os.system("start /min wmplayer bounce.wav")
