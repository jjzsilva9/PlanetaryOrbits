import turtle
from scipy.constants import G
import math
t = turtle.Turtle()
t.hideturtle()

class Planet:
  
  def __init__(self, radius, mass, colour, postion):
    self.radius = radius
    self.mass = mass
    self.colour = colour
    self.position = postion
    self.Fx = 0
    self.Fy = 0

  def update(self, planets):
    for planet in planets:
      distanceX = self.postion[0] - planet.position[0]
      distanceY = self.postion[1] - planet.position[1]
      self.Fx+= (G*planet.mass*self.mass)/distanceX
      self.Fy+= (G*planet.mass*self.mass)/distanceY

  def draw(self):
    t.speed(100)
    t.penup()
    t.setpos(self.position)
    t.pendown()
    t.fillcolor(self.colour)
    t.begin_fill()
    t.circle(self.radius)
    t.end_fill()


earth = Planet(50, 10, "green", [0, 0])
earth.draw()