from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        # self.highscore = 0
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("courier", 24, "normal"))

    def increased_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("courier", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("courier", 24, "normal"))
    # def game_over(self):
    #     self.penup()
    #     self.goto(-80,0)
    #     self.write("GAME OVER", font=("courier", 24, "normal"))
