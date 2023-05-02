from turtle import Turtle


class Scoresheet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.rewrite_score()

    def increment_score(self, player):
        if player == "r":
            self.r_score += 1
        else:
            self.l_score += 1
        self.rewrite_score()

    def rewrite_score(self):
        self.clear()
        self.goto(-120, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 80, "normal"))
        self.goto(120, 200)
        self.write(f"{self.l_score}", align="center", font=("Arial", 80, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))
        self.goto(0, -35)
        if self.r_score < self.l_score:
            self.color("red")
            self.write(f"Player Right wins !!!", align="center", font=("Arial", 28, "normal"))
        else:
            self.color("blue")
            self.write(f"Player Left wins !!!", align="center", font=("Arial", 28, "normal"))