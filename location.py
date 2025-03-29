import random
import math

class Location:

  def __init__(self):
    self.x = random.random()
    self.y = random.random()

  def set(self, x, y):
    self.x = x
    self.y = y

  def distance(self, other):
    return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
  
  def __str__(self):
    return "(%.3f, %.3f)" % (self.x, self.y)