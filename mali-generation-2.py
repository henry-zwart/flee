import flee
import handle_refugee_data
import numpy as np
import analysis as a

if __name__ == "__main__":
  print "Simulating Mali."

  end_time = 61
  e = flee.Ecosystem()

# Distances are estimated using Bing Maps.

# Mali
  
  o1 = e.addLocation("Kidal", movechance=0.3)
  o2 = e.addLocation("Gao", movechance=0.3)
  o3 = e.addLocation("Timbuktu", movechance=0.3)

  e.linkUp("Kidal","Gao","402.0") #354 in Google
  e.linkUp("Kidal","Timbuktu", "622.0") #964.0
  e.linkUp("Gao","Timbuktu","411.0") #612

# Mauritania

  m1 = e.addLocation("Mbera", movechance=0.0)
# GPS 15.639012, -5.751422

  e.linkUp("Kidal","Mbera","1049.0")
  e.linkUp("Gao","Mbera","839.0")
  e.linkUp("Timbuktu","Mbera","428.0")

# Burkina Faso

  b1 = e.addLocation("Mentao", movechance=0.0)
# GPS 13.999700, -1.680371
  b2 = e.addLocation("Bobo-Dioulasso", movechance=0.0)

  e.linkUp("Kidal","Mentao","1285.0")
  e.linkUp("Gao","Mentao","883.0")
  e.linkUp("Timbuktu","Mentao","733.0")

  e.linkUp("Kidal","Bobo-Dioulasso","1430.0")
  e.linkUp("Gao","Bobo-Dioulasso","1029.0")
  e.linkUp("Timbuktu","Bobo-Dioulasso","830.0")

# Niger
  n1 = e.addLocation("Abala", movechance=0.0)
  n2 = e.addLocation("Mangaize", movechance=0.0)

  e.linkUp("Kidal","Abala","1099.0")
  e.linkUp("Gao","Abala","696.0")
  e.linkUp("Timbuktu","Abala","1108.0")

  e.linkUp("Kidal","Mangaize","858.0")
  e.linkUp("Gao","Mangaize","455.0")
  e.linkUp("Timbuktu","Mangaize","867.0")

  d = handle_refugee_data.DataTable("mali2012/refugees.csv", csvformat="mali-portal")

  for t in xrange(0,end_time):
    new_refs = d.get_new_refugees(t)
    for i in xrange(0, new_refs):
      if(t<31): #Kidal has fallen, but Gao and Timbuktu are still controlled by Mali
        e.addAgent(location=o1)
      else: #All three cities have fallen
        # Population numbers source: UNHCR (2009 Mali census)
        pop_kidal_region = 68000
        pop_gao_region = 544000
        pop_timbuktu_region = 682000
        pop_total = pop_kidal_region + pop_gao_region + pop_timbuktu_region
        dice_roll = np.random.randint(pop_total)

        if dice_roll < pop_kidal_region:
          e.addAgent(location=o1) #Add refugee to Kidal
        elif dice_roll < pop_kidal_region + pop_gao_region:
          e.addAgent(location=o2) #Add refugee to Gao
        else:
          e.addAgent(location=o3) #Add refugee to Timbuktu

    e.evolve()

    # Basic output
    # e.printInfo()

    print t

    # Validation / data comparison

    m1_data = d.get_field("Mbera", t) - d.get_field("Mbera", 0)
    b1_data = d.get_field("Mentao", t) - d.get_field("Mentao", 0)
    b2_data = d.get_field("Bobo-Dioulasso", t) - d.get_field("Bobo-Dioulasso", 0)
    n1_data = d.get_field("Abala", t) - d.get_field("Abala", 0)
    n2_data = d.get_field("Mangaize", t) - d.get_field("Mangaize", 0)

    errors = [a.rel_error(m1.numAgents,m1_data), a.rel_error(b1.numAgents,b1_data), a.rel_error(b2.numAgents,b2_data), a.rel_error(n1.numAgents,n1_data), a.rel_error(n2.numAgents,n2_data)]
    abs_errors = [a.abs_error(m1.numAgents,m1_data), a.abs_error(b1.numAgents,b1_data), a.abs_error(b2.numAgents,b2_data), a.abs_error(n1.numAgents,n1_data), a.abs_error(n2.numAgents,n2_data)]

    print "Mbera: ", m1.numAgents, ", data: ", m1_data, ", error: ", errors[0]
    print "Mentao: ", b1.numAgents, ", data: ", b1_data, ", error: ", errors[1]
    print "Bobo-Dioulasso: ", b2.numAgents,", data: ", b2_data, ", error: ", errors[2]
    print "Abala: ", n1.numAgents,", data: ", n1_data, ", error: ", errors[3]
    print "Mengaize: ", n2.numAgents,", data: ", n2_data, ", error: ", errors[4]
    if e.numAgents()>0:
      print "Total error: ", float(np.sum(abs_errors))/float(e.numAgents())

  if np.abs(np.sum(errors) - 116.8) > 5.0:
    print "TEST FAILED."
  if np.sqrt(np.sum(np.power(errors,2))) > 90.6*1.1:
    print "TEST FAILED."
  else:
    print "TEST SUCCESSFUL."

