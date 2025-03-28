from party import Party
from voter import Voter

class Simulation:

  def __init__(self):
    self.parties = []
    self.voters = []

  def setup(self):
    for i in range(100):     # as an example, 100 voters - should be configured!
      voter = Voter()
      self.voters.append(voter)
    for i in range(5):       # as an example, 5 parties - should be configured!
      party = Party("Party " + str(i), 0, 0, "sticker")
      self.parties.append(party)

  def run(self):
    for i in range(10):      # as an example, 10 rounds - should be configured!
      for voter in self.voters:
        voter.vote(self.parties)

    for party in self.parties:
      print(party.name + ": " + str(party.countVoters()))