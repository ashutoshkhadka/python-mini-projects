from turtle import Turtle

STARTING_COORS = [(360, 40), (360, 20), (360, 0), (360, -20), (360, -40)]


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xcor, 200)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
