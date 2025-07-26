import turtle

# Initialize the main window
wind = turtle.Screen()
wind.title("Pong Game")
wind.bgcolor("black")
wind.setup(width=800, height=600)

# Turns off the screen updates for better performance
wind.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Function to move paddle A up
def paddle_a_up():
    # Get the current y-coordinate of paddle A and move it up
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

# Main game loop
while True:
    # Update the screen
    wind.update()
    
    print("Game is running...") 