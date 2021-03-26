import turtle
from scipy.constants import G
import math
t = turtle.Turtle()

class Planet:
  
  def __init__(self, radius, mass, colour, postion):
    self.radius = radius
    self.mass = mass
    self.colour = colour
    self.position = postion

  def update(self, planets):
    F = 0
    for planet in planets:
      distance = math.sqrt((self.postion[0] - planet.position[0])**2 + (self.position[1]-planet.position[1])**2)
      F+= (G*planet.mass*self.mass)/distance