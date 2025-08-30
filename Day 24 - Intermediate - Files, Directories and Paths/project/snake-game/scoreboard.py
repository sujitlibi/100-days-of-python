from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.save_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))

    def read_highscore(self):
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
