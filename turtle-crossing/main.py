import time
from turtle import Screen
from squirtle import Squirtle
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

squirtle = Squirtle()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=squirtle.go_up, key="Up")
sleep_speed = 0.1
is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(sleep_speed)
    cars.generate()
    cars.move()
    # Detect collision
    for car in cars.cars:
        if squirtle.distance(car) < 20:
            scoreboard.game_over()
            is_game_over = True

    if squirtle.ycor() >= 270:
        scoreboard.incr_score()
        squirtle.reset_turtle()
        cars.speed_up()
        sleep_speed -= 0.005

screen.exitonclick()
