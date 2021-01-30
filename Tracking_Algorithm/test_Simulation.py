from Drone import Drone
from Simulation import Simulation
from Animal import Animal

import unittest
import random


class test_Simulation(unittest.TestCase):

    def test_search(self):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        stepts = random.uniform(0, 15)
        sim = Simulation(Drone(x, y, 0.0), stepts)
        sim.probe()


if __name__ == '__main__':
    unittest.main()
