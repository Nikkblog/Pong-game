from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.70)
        self.color("blue")
        self.penup()
        self.speed("slowest")
        self.x = 10
        self.y = 10
        self.ball_speed = 0.1

    def move_ball(self):
        x_cor = self.xcor() + self.x
        y_cor = self.ycor() + self.y

        self.goto(x_cor, y_cor)

    def ball_bounce(self):
        self.y *= -1

    def paddle_bounce(self):
        self.x *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.paddle_bounce()
