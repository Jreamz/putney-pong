from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.inc_speed()
        self.x_move *= -1

    def ball_reset(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def inc_speed(self):
        self.ball_speed *= 0.9
