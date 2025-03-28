from location import Location

class Party:

  def __init__(self, name, x, y, strategy):
    self.name = name
    self.location = Location()    
    self.strategy = strategy

    self.location.set(x, y)
    self.resetVoters()

  def countVoters(self):
    return len(self.voters)

  def vote(self, voter):
    self.voters.append(voter)

  def resetVoters(self):
    self.voters = []

  def.getLocation(self):
    return self.location