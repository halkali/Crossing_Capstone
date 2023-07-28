from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-350,250)
        self.speed("fastest")
        self.write(f"Level: {self.lvl}",align="CENTER", font=('Arial', 15, 'normal'))


    def increase(self):
        self.clear()
        self.lvl +=1
        self.write(f"Level: {self.lvl}", align="CENTER", font=('Arial', 15, 'normal'))

    def game_over(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.write("GAME OVER",align="CENTER", font=('Arial',30, 'normal'))



