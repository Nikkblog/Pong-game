from turtle import Turtle


# CORD = [(-380, 0), (370, 0)]


class Paddle(Turtle):
    def __init__(self, cord):
        super().__init__()
        self.y = 0
        self.cord = cord
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=0.70, stretch_wid=4)
        self.penup()
        self.goto(self.cord)

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor() + 30

        self.setpos(x_cor, y_cor)

    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor() - 30

        self.setpos(x_cor, y_cor)
