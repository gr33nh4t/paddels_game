from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score=0
    self.highscore_l = self.get_highscore_l()
    self.highscore_r = self.get_highscore_r()
    self.r_score=0
    self.update_scoreboard()

  # get highscore func
  def get_highscore_l(self):
    with open("highscore_l.txt", 'r') as file:
      return int(file.read())
    
  def get_highscore_r(self):
    with open("highscore_r.txt", 'r') as file:
      return int(file.read())
    
  # save highscore func
  def save_highscore_r(self):
    with open("highscore_r.txt", 'w') as file:
      file.write(str(self.highscore_r))

  def save_highscore_l(self):
    with open("highscore_l.txt", 'w') as file:
      file.write(str(self.highscore_l))

  def rpoint(self):
    self.r_score+=1
    self.update_scoreboard()

  def lpoint(self):
    self.l_score+=1
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-200,200)
    if self.l_score > self.highscore_l:
        self.highscore_l = self.l_score
        self.save_highscore_l()
    if self.r_score > self.highscore_r:
        self.highscore_r = self.r_score
        self.save_highscore_r()


    self.write(f"{self.l_score} \nHighScore:{self.highscore_l}",align="center",font=("Courier",22,"normal"))

    self.goto(200,200)
    self.write(f"{self.r_score} \nHighScore:{self.highscore_r}",align="center",font=("Courier",24,"normal"))

  # Game Over
  def game_over (self):
    self.clear()
    self.screen.clear()
    self.goto(0,0)
    self.screen.bgcolor('darkred')
    if self.l_score > self.highscore_l:
      self.highscore_l = self.l_score
      self.save_highscore_l()

    if self.r_score > self.highscore_r:
      self.highscore_r = self.r_score
      self.save_highscore_r()

    self.write(f"____________Game Over____________\n\nRight Paddle:\nFinal Score:{self.r_score} \nHigh Score:{self.highscore_r} \n\nLeft Paddle: \nFinal Score:{self.l_score} \nHigh Score: {self.highscore_l}", align="center", font= ('Arial', 24, 'normal'))
    self.screen.update()
    self.screen.ontimer(self.screen.bye, 2000) 

  def game_over_r(self):
    self.l_score += 3
    self.highscore_l += 3
    self.save_highscore_l()
    self.game_over()

  def game_over_l(self):
    self.r_score += 3
    self.highscore_r += 3
    self.save_highscore_r()
    self.game_over()


