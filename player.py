from turtle import Turtle
import random
STARTING_POSITION = (350, 0)
COMPUTER_STARTING_POSITION = (-350, 0)

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.turtlesize(5, 1)
        self.game_over = False


    def set_starting_position(self, position):
        self.penup()
        self.goto(position)
    def player_one(self):
        self.penup()
        self.set_starting_position(STARTING_POSITION)


    def computer_player(self):
        self.penup()
        self.set_starting_position(COMPUTER_STARTING_POSITION)
        random_direction = random.choice(["up", "down"])


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



