import random
from location import Location

class Voter:

  def __init__(self):
    self.location = Location()

  def vote(self, parties):
    closestDistance = 2 # any value above sqrt(2) will do

    for party in parties:
      distance = party.getLocation().distance(self.location)
      if distance < closestDistance:
        closestDistance = distance
        closestParty = party

    closestParty.vote(self)