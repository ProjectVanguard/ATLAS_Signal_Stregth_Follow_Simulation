from Drone import Drone
from Simulation import Simulation
from Animal import Animal
# Several runs to test functionality.


def main():
    print("################## Simulation 1 ##########################")
    drone = Drone(150, 0, 0.0)
    sim = Simulation(drone, 3)
    sim.probe()
    print("#########################################################")

    print("\n\n################## Simulation 2 ##########################")
    drone = Drone(40.0, 30.0, 0)
    sim = Simulation(drone, 3)
    sim.probe()

    print("\n\n################## Simulation 3 ##########################")
    drone = Drone(0.0, 0.0, 0.0)
    sim = Simulation(drone, 2)
    sim.probe()
    print("#########################################################")

    print("\n\n################## Simulation 4 ##########################")
    drone = Drone(30.0, 30.0, 30.0)
    sim = Simulation(drone, 3)
    sim.probe()
    print("#########################################################")

    print("\n\n################## Simulation 5 ##########################")
    drone = Drone(0.0, 0.0, 10.0)
    sim = Simulation(drone, 5)
    sim.probe()
    print("#########################################################\n\n")


if __name__ == "__main__":
    main()
