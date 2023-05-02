from turtle import Turtle

STARTING_COORS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for coor in STARTING_COORS:
            self.add_segment(coor)

    def add_segment(self, pos):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(pos)
        self.segments.append(turtle)

    def extend(self):
        last_turtle = self.segments[-1]
        self.add_segment(last_turtle.pos())

    def reset(self):
        for seg in self.segments:
            seg.goto(1010,1010)
        self.segments.clear()
        self.create_snake()


    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.segments[0].forward(STEP_SIZE)

    def right(self):
        if self.segments[0] != LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
