from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(self.position)
        self.show_score(self.score)

    def left_score(self):
        self.score += 1
        self.goto(self.position)
        self.show_score(self.score)

    def right_score(self):
        self.score += 1
        self.goto(self.position)
        self.show_score(self.score)

    def show_score(self, score):
        self.clear()
        self.write(f"{score}", align="center", font=("Courier", 40, "normal"))
