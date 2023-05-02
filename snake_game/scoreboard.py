from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.goto(0, 250)
        self.color("white")
        self.rewrite_score()
        self.hideturtle()

    def increment_score(self):
        self.score += 1
        self.rewrite_score()

    def rewrite_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.rewrite_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write("Game Over !!!", align="center", font=("Arial", 24, "normal"))
