from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WALL_LIMIT = 280

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
scoreboard = Scoreboard()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

is_game_over = False
while not is_game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision
    if food.distance(snake.segments[0]) < 15:
        food.generate()
        scoreboard.increment_score()
        snake.extend()

    # Detect wall
    if snake.segments[0].xcor() > WALL_LIMIT or snake.segments[0].xcor() < -WALL_LIMIT or \
            snake.segments[0].ycor() > WALL_LIMIT or snake.segments[0].ycor() < -WALL_LIMIT:
        is_game_over = True
        scoreboard.game_over()

    # Detect Tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 6:
            is_game_over = True
            scoreboard.game_over()
screen.exitonclick()
