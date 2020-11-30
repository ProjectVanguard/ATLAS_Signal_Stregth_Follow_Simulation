from Drone import Drone
from Simulation import Simulation
from Animal import Animal
# Several runs to test functionality.


def main():
    print("################## Simulation 1 ##########################")
    drone = Drone(98.0, 98.0, 0.0)
    sim = Simulation(drone, 3)
    sim.run()
    print("#########################################################")

    # print("\n\n################## Simulation 2 ##########################")
    # drone = Drone(40.0, 300.0, 100.0)
    # sim = Simulation(drone, 3)
    # sim.run()

    # print("\n\n################## Simulation 3 ##########################")
    # drone = Drone(0.0, 0.0, 100.0)
    # sim = Simulation(drone, 10)
    # sim.run()
    # print("#########################################################")

    # print("\n\n################## Simulation 4 ##########################")
    # drone = Drone(1111.0, 23234.0, 100.0)
    # sim = Simulation(drone, 3)
    # sim.run()
    # print("#########################################################")

    # print("\n\n################## Simulation 5 ##########################")
    # drone = Drone(0.0, 0.0, 100.0)
    # sim = Simulation(drone, 5)
    # sim.run()
    # print("#########################################################\n\n")


if __name__ == "__main__":
    main()
