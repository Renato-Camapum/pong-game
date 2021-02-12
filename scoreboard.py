from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score_1 = -1
        self.score_2 = -1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)

    def sum_score1(self):
        self.clear()
        self.score_1 += 1
        self.write(f"{self.score_1}", align="center", font=("Arial", 30, "normal"))

    def sum_score2(self):
        self.clear()
        self.score_2 += 1
        self.write(f"{self.score_2}", align="center", font=("Arial", 30, "normal"))

