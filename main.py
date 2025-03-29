from simulation import Simulation

def main():
  simulation = Simulation()
  simulation.setup()
  simulation.run()
  simulation.printResults()

if __name__ == "__main__":
  main()