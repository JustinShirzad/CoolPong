import turtle
import winsound

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
paddle_a_direction = 0

# Paddle A
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)
paddle_b_direction = 0

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
    global paddle_a_direction
    paddle_a_direction = 1

# Function to move paddle A up
def paddle_a_down():
    global paddle_a_direction
    paddle_a_direction = -1

# Function to move paddle B up
def paddle_b_up():
    global paddle_b_direction
    paddle_b_direction = 1

# Function to move paddle B down
def paddle_b_down():
    global paddle_b_direction
    paddle_b_direction = -1

# Function to stop paddle A
def paddle_a_stop():
    global paddle_a_direction
    paddle_a_direction = 0

# Function to stop paddle B
def paddle_b_stop():
    global paddle_b_direction
    paddle_b_direction = 0

# Keyboard bindings
wind.listen()
wind.onkeypress(paddle_a_up, "w")
wind.onkeyrelease(paddle_a_stop, "w")
wind.onkeypress(paddle_a_down, "s")
wind.onkeyrelease(paddle_a_stop, "s")
wind.onkeypress(paddle_b_up, "Up")
wind.onkeyrelease(paddle_b_stop, "Up")
wind.onkeypress(paddle_b_down, "Down")
wind.onkeyrelease(paddle_b_stop, "Down")

# Update ball speed
def ball_control():
    if ball.dx < 0.1:
        ball.dx -= 0.01
    if ball.dy < 0.1:
        ball.dy -= 0.01

def update_paddle_a():
    global paddle_a_direction
    new_y = paddle_a.ycor() + (paddle_a_direction * 0.2)
    if -240 <= new_y <= 240:
        paddle_a.sety(new_y)

def update_paddle_b():
    global paddle_b_direction
    new_y = paddle_b.ycor() + (paddle_b_direction * 0.2)
    if -240 <= new_y <= 240:
        paddle_b.sety(new_y)

# Main game loop
while True:
    # Update the screen
    wind.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    update_paddle_a()
    update_paddle_b()

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

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
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() - 60 < ball.ycor() < paddle_a.ycor() + 60):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
