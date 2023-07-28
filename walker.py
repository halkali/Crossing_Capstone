from turtle import Turtle

class Walker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.shapesize(1)
        self.showturtle()

    def move(self):
        self.forward(10)

