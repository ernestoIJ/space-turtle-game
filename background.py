from turtle import Turtle
import random


class Background:

    def __init__(self):
        self.all_asteroids = []

    def create_asteroid(self):
        num = random.randint(1, 3)
        if num == 1:
            new_asteroid = Turtle("circle")
            new_asteroid.color("grey")
            new_asteroid.penup()
            new_asteroid.shapesize(stretch_wid=0.1, stretch_len=0.1)
            random_x = random.randint(-300, 300)
            new_asteroid.goto(random_x, 300)
            new_asteroid.setheading(270)
            self.all_asteroids.append(new_asteroid)

    def move_asteroid(self):
        for asteroid in self.all_asteroids:
            asteroid.forward(10)
