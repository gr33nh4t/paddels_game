from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 
# set up
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(scoreboard.game_over_r, "e")
screen.onkey(scoreboard.game_over_l, "q")


default_time=0.1
gameon=True

while gameon:
  screen.update()
  time.sleep(default_time)

  # move ball
  ball.goto(ball.xcor()+ ball.x_move,ball.ycor()+ ball.y_move)


  # ball bounce off top and bottom
  if ball.ycor()>280 or ball.ycor()<-280:
    ball.y_move*=-1

  # ball bounce off paddle
  if ball.distance(r_paddle)<=50 or ball.distance(l_paddle)<=50:
    ball.x_move*=-1
    default_time*=0.9

  # ball out of bounds right
  if ball.xcor()==400:
    ball.goto(0,0)
    ball.x_move*=-1
    default_time=0.1
    scoreboard.lpoint()
    
  # ball out of bounds left
  if ball.xcor()==-400:
    ball.goto(0,0)
    ball.x_move*=-1
    default_time=0.1
    scoreboard.rpoint()


screen.exitonclick()