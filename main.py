import turtle
from scipy.constants import G
import math
import datetime
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
    for sphere in planets:
      if sphere != self:
        distanceX = self.postion[0] - sphere.position[0]
        distanceY = self.postion[1] - sphere.position[1]
        self.Fx+= (G*sphere.mass*self.mass)/distanceX
        self.Fy+= (G*sphere.mass*self.mass)/distanceY
        velocityX = self.Fx/self.mass
        velocityY = self.Fy/self.mass
        self.position[0] += velocityX * datetime.timedelta
        self.position[1] += velocityY * datetime.timedelta

  def draw(self):
    t.speed(100)
    t.penup()
    t.setpos(self.position)
    t.pendown()
    t.fillcolor(self.colour)
    t.begin_fill()
    t.circle(self.radius)
    t.end_fill()

planets = []
earth = Planet(5, 10, "green", [0, 0])
sun = Planet(20, 100, "yellow", [150, 50])
planets.append(earth)
planets.append(sun)


while True:
  for planet in planets:
    planet.update(planets)
    planet.draw()