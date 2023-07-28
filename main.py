from turtle import Turtle, Screen
from cars import Cars
from walker import Walker
import time
from random import randint
from scoreboard import ScoreBoard
SPEED = 20

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.listen()
walker = Walker()
screen.onkeypress(key="Up", fun=walker.move)
scoreboard = ScoreBoard()


moving = []

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    chance = randint(1, 4)
    if chance ==1:
        cars = Cars()
        moving.append(cars)
    if walker.ycor() > 280:
        walker.goto(0, -280)
        SPEED += 5
        scoreboard.increase()
    for j in moving:
        j.forward(SPEED)
        if j.distance(walker) < 25:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()


