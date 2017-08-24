import sys
import csv

class SimulationSettings:
  Softening = 0.0
  #TurnBackAllowed = True # feature disabled for now.
  AgentLogLevel = 0 # set to 1 for basic agent information.
  CampLogLevel = 0  # set to 1 to obtain average times for agents to reach camps at any time step (aggregate info).
  InitLogLevel  = 0 # set to 1 for basic information on locations added and conflict zones assigned.
  TakeRefugeesFromPopulation = True

  CampWeight = 2.0 # attraction factor for camps.
  ConflictWeight = 0.25 # reduction factor for refugees entering conflict zones.
  MinMoveSpeed = 200 # least number of km that we expect refugees to traverse per time step.
  MaxMoveSpeed = 200 # most number of km that we expect refugees to traverse per time step.
  #UseDynamicCampWeights = True # overrides CampWeight depending on characteristics of the ecosystem.
  CapacityBuffer = 1.0

  AwarenessLevel = 1 #-1, no weighting at all, 0 = road only, 1 = location, 2 = neighbours, 3 = region.
  UseDynamicAwareness = False # Refugees become smarter over time.
  UseIDPMode = False

  def ReadFromCSV(csv_name):
    """
    Reads simulation settings from CSV
    """
    number_of_steps = -1

    with open(csv_name, newline='') as csvfile:
      values = csv.reader(csvfile)

      for row in values:
        if row[0][0] == "#":
          pass
        elif row[0] == "AgentLogLevel":
          AgentLogLevel = int(row[1])
        elif row[0] == "CampLogLevel":
          CampLogLevel = int(row[1])
        elif row[0] == "InitLogLevel":
          InitLogLevel = int(row[1])
        elif row[0] == "MinMoveSpeed":
          MinMoveSpeed = int(row[1])
        elif row[0] == "MaxMoveSpeed":
          MaxMoveSpeed = int(row[1])
        elif row[0] == "NumberOfSteps":
          number_of_steps = int(row[1])
        elif row[0] == "CampWeight":
          CampWeight = float(row[1])
        elif row[0] == "ConflictWeight":
          ConflictWeight = float(row[1])
        elif row[0] == "AwarenessLevel":
          AwarenessLevel = int(row[1])
        else:
          print("FLEE Initialization Error: unrecognized simulation parameter:",row[0])
          sys.exit()

    return number_of_steps

