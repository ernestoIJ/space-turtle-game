from turtle import Turtle
import random


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -270)
        self.setheading(90)
        self.all_bullets = []
        self.all_first_powerups = []
        self.all_second_powerups = []
        self.num_second_powerups = 0
        self.all_powbullets = []

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_backwards(self):
        self.setheading(270)
        self.forward(10)

    def create_bullet(self):
        new_bullet = Turtle("square")
        new_bullet.penup()
        new_bullet.shapesize(stretch_wid=0.1, stretch_len=0.3)
        new_bullet.color("red")
        x_cord = self.xcor()
        y_cord = self.ycor()
        new_bullet.setheading(self.heading())
        new_bullet.goto(x_cord, y_cord)
        self.all_bullets.append(new_bullet)

    def move_bullet(self):
        if len(self.all_bullets) > 0:
            for i in range(len(self.all_bullets)):
                self.all_bullets[i].forward(10)

    def powerup(self):
        random_chance = random.randint(1, 100)
        if random_chance == 1:
            power = Turtle("circle")
            power.color("yellow")
            power.penup()
            power.shapesize(stretch_wid=0.5, stretch_len=0.5)
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            power.goto(random_x, random_y)
            self.all_first_powerups.append(power)

    def second_powerup(self):
        random_chance = random.randint(1, 100)
        if random_chance == 1:
            power = Turtle("classic")
            power.color("grey")
            power.penup()
            power.shapesize(stretch_wid=2, stretch_len=2)
            random_x = random.randint(-280, 280)
            random_y = random.randint(-280, 280)
            power.goto(random_x, random_y)
            self.all_second_powerups.append(power)

    def create_power_bullet(self):
        if self.num_second_powerups > 0:
            bull = Turtle("classic")
            bull.color("grey")
            bull.penup()
            bull.setheading(self.heading())
            bull.shapesize(stretch_wid=6, stretch_len=6)
            bull.speed("fastest")
            bull.goto(self.xcor(), self.ycor())
            self.all_powbullets.append(bull)
            self.num_second_powerups -= 1

    def move_second_powerup(self):
        for power in self.all_powbullets:
            power.forward(10)

