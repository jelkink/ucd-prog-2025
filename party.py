from location import Location

class Party:

  def __init__(self, name, strategy):
    self.name = name
    self.location = Location()    
    self.strategy = strategy

    self.resetVoters()

  def countVoters(self):
    return len(self.voters)

  def vote(self, voter):
    self.voters.append(voter)

  def resetVoters(self):
    self.voters = []

  def getLocation(self):
    return self.location
  
  def __str__(self):
    return "%10s (%s) at %s has %d voters" % (self.name, self.strategy, self.location, self.countVoters())