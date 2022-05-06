from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.move_speed=0.1
    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x,new_y)
    def change_y(self):
        self.y_direction *= -1
    def change_x(self):
        self.x_direction *= -1
        self.move_speed *= 0.9
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.change_x()