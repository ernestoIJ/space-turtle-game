from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        self.goto(190, -280)
        self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))
        self.goto(230, 270)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
