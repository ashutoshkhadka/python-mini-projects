from turtle import Screen
from pingpong.paddle import Paddle
from ball import Ball
from scoresheet import Scoresheet

WALL_LIMIT = 280
MAX_ROUND = 2

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)  # turn off animation

paddle_r = Paddle(360)
paddle_l = Paddle(-360)
ball = Ball()
scoresheet = Scoresheet()

screen.listen()
screen.onkey(fun=paddle_r.go_up, key="Up")
screen.onkey(fun=paddle_r.go_down, key="Down")
screen.onkey(fun=paddle_l.go_up, key="w")
screen.onkey(fun=paddle_l.go_down, key="s")

is_game_over = False
while not is_game_over:
    screen.update()
    ball.move()
    # Detect collision against wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 345 \
            or ball.distance(paddle_l) < 50 and ball.xcor() < -345:
        ball.bounce_x()

    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            scoresheet.increment_score("r")
        else:
            scoresheet.increment_score("l")
        ball.reset()

    if scoresheet.r_score == MAX_ROUND or scoresheet.l_score == MAX_ROUND:
        scoresheet.game_over()
        is_game_over = True

screen.exitonclick()
