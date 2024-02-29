from turtle import Turtle
import random


class Enemy(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        random_x = random.randint(-280, 280)
        self.goto(random_x, 300)
        self.setheading(270)
        self.move_speed = 5
        self.explosion = []

    def move_forward(self):
        self.forward(self.move_speed)

    def reset_enemy(self):
        random_x = random.randint(-280, 280)
        self.goto(random_x, 300)

    def increase_speed(self):
        self.move_speed += 1

    def instant_kill(self):
        first_circle = Turtle("circle")
        first_circle.color("red")
        first_circle.penup()
        first_circle.shapesize(stretch_wid=2.5, stretch_len=2.5)
        first_circle.goto(self.xcor(), self.ycor())
        self.explosion.append(first_circle)

        second_circle = Turtle("circle")
        second_circle.color("orange")
        second_circle.penup()
        second_circle.shapesize(stretch_wid=1.75, stretch_len=1.75)
        second_circle.goto(self.xcor(), self.ycor())
        self.explosion.append(second_circle)

        third_circle = Turtle("circle")
        third_circle.color("yellow")
        third_circle.penup()
        third_circle.shapesize(stretch_wid=1, stretch_len=1)
        third_circle.goto(self.xcor(), self.ycor())
        self.explosion.append(third_circle)

    def clear_explosions(self):
        if len(self.explosion) > 0:
            for circle in self.explosion:
                circle.hideturtle()
