from turtle import Turtle
from paddle import Paddle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.write(f"SCOREBOARD\n{self.l_score}\t       {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def r_won(self):
            self.r_score += 1
            self.clear()
            self.write(f"SCOREBOARD\n{self.l_score}\t     "
                       f"  {self.r_score}", align="center", font=("Arial", 20, "normal"))
    def l_won(self):
            self.l_score += 1
            self.clear()
            self.write(f"SCOREBOARD\n{self.l_score}\t       {self.r_score}", align="center",
                       font=("Arial", 20, "normal"))
