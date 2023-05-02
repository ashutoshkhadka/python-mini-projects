from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("black")
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def incr_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
