
from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, "center", ("courier", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f'Game is Over. Your score is: {self.score}', False, "center", ("courier", 12, "normal"))

    def scoring(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()

