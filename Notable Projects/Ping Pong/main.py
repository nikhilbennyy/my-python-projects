from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


score=Scoreboard()
ball=Ball()
tur = Turtle()
scr = Screen()
scr.setup(width=800, height = 600)
scr.bgcolor("black")
tur.color("white")
tur.hideturtle()
scr.tracer(0)
tur.penup()
tur.pensize(5)
tur.pencolor("white")
tur.goto(0,-300)
tur.left(90)

for n in range(0, 55):
    if n%2==0:
        tur.pendown()
        tur.forward(10)
    else:
        tur.penup()
        tur.forward(10)


r_paddle=Paddle(380)
l_paddle=Paddle(-380)


scr.listen()
scr.onkeypress(r_paddle.up, "Up")
scr.onkeypress(r_paddle.down, "Down")
scr.onkeypress(l_paddle.up, "w")
scr.onkeypress(l_paddle.down, "s")

game_on=True
while game_on:
    scr.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.change_y()
    if ball.distance(r_paddle) < 40 and ball.xcor()>350 or ball.distance(l_paddle) < 40 and ball.xcor() < -350:
        # ball.change_y()
        ball.change_x()
    elif ball.xcor()>380 or ball.xcor()<-380:
        pos=ball.xcor()
        if pos>0:
            score.l_won()
        else:
            score.r_won()
        ball.reset_ball()
    if score.r_score==10 or score.l_score==10:
        if score.r_score > score.l_score:
            tur.penup()
            tur.goto(200,0)
            tur.write("YOU WON", align="right", font=("Arial", 20, "normal"))
        else:
            tur.penup()
            tur.goto(-200, 0)
            tur.write("YOU WON", align="left", font=("Arial", 20, "normal"))
        time.sleep(3)
        exit()


scr.exitonclick()
