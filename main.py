import time
from turtle import Screen, Turtle
from paddle import Paddle
from middle_partition import Partition
from ball import Ball
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("Black")
screen.tracer(0)

t = Turtle()

ball = Ball()
left_score = Score((-50, 240))
right_score = Score((50, 240))

left = Paddle((-380, 0))
right = Paddle((370, 0))
partition = Partition()

screen.listen()
screen.onkey(left.move_up, "a")
screen.onkey(left.move_down, "s")

screen.onkey(right.move_up, "k")
screen.onkey(right.move_down, "l")

timer = 0.10
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move_ball()

    # Detecting wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.ball_bounce()

    # Detect Paddle and bounce
    if ball.distance(right) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()

        # right_score.right_score()
    elif ball.distance(left) < 50 and ball.xcor() < -355:
        ball.paddle_bounce()

        # left_score.left_score()

    if ball.xcor() > 380:
        ball.reset_position()
        left_score.left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        right_score.right_score()

screen.exitonclick()
