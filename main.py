import turtle
from scipy.constants import G
import math
import datetime
import time
t = turtle.Turtle()
t.hideturtle()

class Planet:
  
  def __init__(self, radius, mass, colour, x, y):
    self.radius = radius
    self.mass = mass
    self.colour = colour
    self.x = x
    self.y = y
    self.Fx = 0
    self.Fy = 0

  def update(self, planets):
    for sphere in planets:
      if sphere != self:
        distanceX = self.x - sphere.x
        distanceY = self.y - sphere.y
        self.Fx+= (G*sphere.mass*self.mass)/distanceX
        self.Fy+= (G*sphere.mass*self.mass)/distanceY
        velocityX = self.Fx/self.mass
        velocityY = self.Fy/self.mass
        self.x += velocityX
        self.y += velocityY

  def draw(self):
    t.speed(100)
    t.penup()
    t.setpos(self.x, self.y)
    t.pendown()
    t.fillcolor(self.colour)
    t.begin_fill()
    t.circle(self.radius)
    t.end_fill()

planets = []


while True:
  time.sleep(0.1)
  for planet in planets:
    planet.update(planets)
    planet.draw()