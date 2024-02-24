import turtle
from turtle import Turtle



class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.score = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score:{self.score}", False, "center", ("Courier", 20, "normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score:{self.score}", False, "center", ("Courier", 20, "normal"))


    def game_over(self):

        self.home()
        self.color("White")
        self.write(f"GAME OVER",False,"Center",("Courier",20,"normal"))




