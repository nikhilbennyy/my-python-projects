from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
tim = Turtle()
scr = Screen()
snake = Snake()
food = Food()
score = ScoreBoard()
food.clear()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.listen()
scr.onkeypress(snake.up, "Up")
scr.onkeypress(snake.down, "Down")
scr.onkeypress(snake.right, "Right")
scr.onkeypress(snake.left, "Left")
game_on = True
while game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        food.new_food()
        snake.increase_length()
        score.increased_score()
        # print(food.xcor())
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        # game_on=False
        scr.tracer(0)
        score.reset()

        snake.reset()
        scr.update()

    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg)<15:
            # game_on=False
            scr.tracer(0)
            score.reset()
            snake.reset()
            scr.update()

#
#
# scr.exitonclick()