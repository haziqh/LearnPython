import turtle

wn = turtle.Screen()
wn.title('Pong by Haziq')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write('Player 1: 0               Player 2: 0', align='center', font=('Courier', 20, 'normal'))



# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:       # Roughly half of the window height (300)
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:      # Roughly half of the window height (-300)
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:       # Roughly half of the window width (400)
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1            # Adds score to Player 1 when ball goes through right side
        pen.clear()             # Clears the score before updating new score
        pen.write('Player 1: {}               Player 2: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

    if ball.xcor() < -390:      # Roughly half of the window width (-400)
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1            # Adds score to Player 2 when ball goes through left side
        pen.clear()             # Clears the score before updating new score
        pen.write('Player 1: {}               Player 2: {}'.format(score_a, score_b), align='center', font=('Courier', 20, 'normal'))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1