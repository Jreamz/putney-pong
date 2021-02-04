from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("Putney Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

score = Score()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() >= 323 or ball.distance(l_paddle) < 50 and ball.xcor() <= -323:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.l_point()
        score.update_score()
        ball.ball_reset()

    if ball.xcor() < -380:
        score.r_point()
        score.update_score()
        ball.ball_reset()

screen.exitonclick()
