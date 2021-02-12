import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Score

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

score1 = Score((-200, 250))
score2 = Score((200, 250))

ball = Ball()

screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True
score1.sum_score1()
score2.sum_score2()


while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_right) < 60 and ball.xcor() > 320:

        ball.bounce_paddle()

    if ball.distance(paddle_left) < 60 and ball.xcor() < -320:

        ball.bounce_paddle()

    if ball.xcor() > 380:
        score1.sum_score1()
        ball.reset_ball()
        ball.move_ball()

    if ball.xcor() < -380:
        score2.sum_score2()
        ball.reset_ball()
        ball.move_ball_bd()

screen.exitonclick()