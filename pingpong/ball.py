from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move *= 1.1
        self.y_move *= 1.1

    def reset(self):
        self.goto(0, 0)
        self.x_move = 3
        self.y_move = 3
