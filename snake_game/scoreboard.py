from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 250)
        self.color("white")
        self.rewrite_score()
        self.hideturtle()

    def increment_score(self):
        self.score += 1
        self.clear()
        self.rewrite_score()

    def rewrite_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over !!!", align="center", font=("Arial", 24, "normal"))

