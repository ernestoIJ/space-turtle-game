from turtle import Screen
import time
from player import Player
from background import Background
from scoreboard import Scoreboard
from enemy import Enemy

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Space Turtle")
screen.tracer(0)

turtle = Player()
asteroid = Background()
score = Scoreboard()
enemy = Enemy()


screen.listen()
screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_backwards, "Down")
screen.onkey(turtle.move_right, "Right")
screen.onkey(turtle.move_left, "Left")
screen.onkey(turtle.create_bullet, "s")
screen.onkey(turtle.create_power_bullet, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    asteroid.create_asteroid()
    asteroid.move_asteroid()

    turtle.move_bullet()

    turtle.move_second_powerup()

    enemy.move_forward()

    turtle.powerup()

    turtle.second_powerup()

    if score.lives == 0:
        score.game_over()
        game_is_on = False

    if enemy.ycor() < -300:
        enemy.reset_enemy()
        score.decrease_lives()

    for bullet in turtle.all_bullets:
        if enemy.distance(bullet) < 20:
            enemy.reset_enemy()
            enemy.increase_speed()
            score.increase_score()

    enemy.clear_explosions()

    for powerups in turtle.all_first_powerups:
        if powerups.distance(turtle) < 20:
            powerups.goto(-350, 350)
            enemy.instant_kill()
            enemy.reset_enemy()
            score.increase_score()
            enemy.increase_speed()

    for power in turtle.all_second_powerups:
        if power.distance(turtle) < 20:
            power.goto(-350, 350)
            turtle.num_second_powerups += 1

    for bull in turtle.all_powbullets:
        if enemy.distance(bull) < 30:
            enemy.reset_enemy()
            score.increase_score()
            enemy.increase_speed()

screen.exitonclick()
