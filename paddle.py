from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(5, 1, 0)
        self.setpos(x_pos, y_pos)

    def up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
