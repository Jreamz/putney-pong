from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.title("Putney Pong")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_over = False
while not game_over:
    screen.update()






screen.exitonclick()
