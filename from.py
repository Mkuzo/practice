from turtle import *
class FACE:
  def __init__(self,x,y):
    self.size = 90
    self.codinate = (x,y)
    self.nose = "small"
  def setsize(self,radius):
    self.size = radius
  def draw(self):
    self.goHome()
    pensize(3)
    speed(0)
    self.drawoutline()
    self.draweye(135)
    self.draweye(45)
    self.drawmouth()
    self.drawmouth()
    pensize(5)
  def goHome(self):
    penup()
    goto(self.codinate)
    setheading(0)
  def drawoutline(self):
    penup()
    forward(self.size)
    left(90)
    pendown()
    circle(self.size)
    