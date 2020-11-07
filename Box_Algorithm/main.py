from Drone import Drone
from Simulation import Simulation
from Animal import Animal
#Several runs to test functionality.
def main():
    print("################## Simulation 1 ##########################")
    drone = Drone(0,0,100)
    lizard = Animal([4234,234,0])
    sim = Simulation(drone,lizard,3)
    sim.run()
    print("#########################################################")

    print("\n\n################## Simulation 2 ##########################")
    drone = Drone(40,300,100)
    lizard = Animal([0,0,0])
    sim = Simulation(drone,lizard,3)
    sim.run()

    print("\n\n################## Simulation 3 ##########################")
    drone = Drone(0,0,100)
    lizard = Animal([20,5,0])
    sim = Simulation(drone,lizard,10)
    sim.run()
    print("#########################################################")
 
    print("\n\n################## Simulation 4 ##########################")
    drone = Drone(1111,23234,100)
    lizard = Animal([0,0,0])
    sim = Simulation(drone,lizard,3)
    sim.run()
    print("#########################################################")

    print("\n\n################## Simulation 5 ##########################")
    drone = Drone(0,0,100)
    lizard = Animal([3333,9999,0])
    sim = Simulation(drone,lizard,5)
    sim.run()
    print("#########################################################\n\n")

   

if __name__ == "__main__":
    main()



