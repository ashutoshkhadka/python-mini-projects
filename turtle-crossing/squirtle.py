from turtle import Turtle

STEP_SIZE = 10


class Squirtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, 250)

    def go_up(self):
        self.forward(STEP_SIZE)

    def reset_turtle(self):
        self.goto(0, 250)
