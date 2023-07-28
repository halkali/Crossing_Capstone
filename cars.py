import random
from turtle import Turtle
from random import randint

COLORS = ["red", "black", "yellow", "blue", "violet", "pink", "green"]



class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.setheading(180)
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.konum()
        self.showturtle()

    def konum(self):
        self.goto(randint(420,500),randint(-230,250))


