import flee.flee as flee
import datamanager.handle_refugee_data as handle_refugee_data
import numpy as np
import outputanalysis.analysis as a

"""
Generation 1 code. Incorporates only distance, travel always takes one day.
"""

if __name__ == "__main__":
  print("Testing basic data handling and simulation kernel.")

  flee.SimulationSettings.SimulationSettings.MinMoveSpeed=10.0
  flee.SimulationSettings.SimulationSettings.MaxMoveSpeed=10.0

  end_time = 100
  e = flee.Ecosystem()

  l1 = e.addLocation("A", movechance=1.0)
  l2 = e.addLocation("B", movechance=0.0)

  e.linkUp("A","B","50.0")


  for t in range(0,end_time):
    # Insert refugee agents
    e.addAgent(location=l1)

    # Propagate the model by one time step.
    e.evolve()

    if t==2:
      assert e.close_location("B")

    print(t, l1.numAgents, l2.numAgents)
    e.printComplete()

  assert t==99
  assert l2.numAgents==3 # Location is closed after 3 steps, refugees underway will still arrive but others are blocked.

  print("Test successful!")

  """
    l2_data = d.get_field("Mauritania", t) - d.get_field("Mauritania", 0)
    l3_data = d.get_field("Niger", t) - d.get_field("Niger", 0)
    l4_data = d.get_field("Burkina Faso", t) - d.get_field("Burkina Faso", 0)

    errors = [a.rel_error(l2.numAgents,l2_data), a.rel_error(l3.numAgents,l3_data), a.rel_error(l4.numAgents,l4_data)]

    print "Kiffa: ", l2.numAgents, ", data: ", l2_data, ", error: ", errors[0]
    print "Niamey: ", l3.numAgents, ", data: ", l3_data, ", error: ", errors[1]
    print "Bobo-Dioulasso: ", l4.numAgents,", data: ", l4_data, ", error: ", errors[2]
    print "Cumulative error: ", np.sum(errors), ", Squared error: ", np.sqrt(np.sum(np.power(errors,2)))

  if np.abs(np.sum(errors) - 0.495521376979) > 0.1:
    print "TEST FAILED."
  if np.sqrt(np.sum(np.power(errors,2))) > 0.33+0.03:
    print "TEST FAILED."
  else:
    print "TEST SUCCESSFUL."
  """
