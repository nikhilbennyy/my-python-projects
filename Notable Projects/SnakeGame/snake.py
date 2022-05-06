from turtle import Turtle,Screen
from food import Food


tim = Turtle()
food = Food()
scr = Screen()


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        pos = 0
        for n in range(0, 3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos, 0)
            self.segment.append(new_segment)
            pos -= 20

    def seg(self, pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(pos)
        self.segment.append(new_segment)

    def increase_length(self):
        self.seg(self.segment[-1].position())

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].forward(20)

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]
