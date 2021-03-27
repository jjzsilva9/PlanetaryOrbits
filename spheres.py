import turtle
from scipy.constants import G
import math
import datetime
import time
t = turtle.Turtle()
t.hideturtle()

class Planet:
  
  def __init__(self, radius, mass, colour, x, y, Ux, Uy):
    self.radius = radius
    self.mass = mass
    self.colour = colour
    self.x = x
    self.y = y
    self.Fx = 0
    self.Fy = 0
    self.Vx = 0
    self.Vy = 0
    self.Ux = Ux
    self.Uy = Uy

  def update(self, planets):
    for sphere in planets:
      if sphere != self:
        distanceX = self.x - sphere.x
        distanceY = self.y - sphere.y
        self.Fx = (G*sphere.mass*self.mass)/distanceX
        self.Fy = (G*sphere.mass*self.mass)/distanceY
        accelerationX = self.Fx/self.mass
        accelerationY = self.Fy/self.mass
        self.Vx = self.Ux + (accelerationX)
        self.Vy = self.Uy + (accelerationY)
        self.x += self.Vx
        self.y += self.Vy
        print(f"X: {self.x}, Y: {self.y}, Vx: {self.Vx},  Vy: {self.Vy}")
        print(f"DistanceX: {distanceX} DistanceY: {distanceY}")

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
earth = Planet(10, 10000, "green", 300, 300, -10, -10)
planets.append(earth)
sun = Planet(250, 100000000000000, "yellow", 0, 0, 0, 0)
planets.append(sun)

while True:
  time.sleep(0.1)
  earth.update(planets)
  earth.draw()
  sun.draw()