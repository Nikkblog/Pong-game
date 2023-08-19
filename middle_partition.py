from turtle import Turtle


class Partition(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("arrow")
        self.color("red")
        self.penup()
        self.goto(0, 300)
        while self.ycor() != -300:
            self.draw_line()

    def draw_line(self):
        self.pendown()
        self.setheading(270)
        self.forward(20)
        self.penup()
        self.forward(20)


