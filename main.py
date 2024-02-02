# 1. Create the screen

from turtle import Screen
from player import Player

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

player = Player()
computer = Player()
player.player_one()
computer.computer_player()
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()










screen.exitonclick()
