from Drone import Drone

import unittest


class Drone_test(unittest.TestCase):
    def test_drone_movement_X(self):
        drone = Drone(0.0, 0.0, 0.0)
        drone.moveFr(5)
        self.assertEqual(drone.location(), [5.0, 0.0, 0.0])
        drone.moveFr(-5)
        self.assertEqual(drone.location(), [0.0, 0.0, 0.0])

    # ...

    def test_drone_movement_Y(self):

        drone = Drone(0.0, 0.0, 0.0)
        drone.moveRi(5)
        self.assertEqual(drone.location(), [0.0, 5.0, 0.0])
        drone.moveRi(-5)
        self.assertEqual(drone.location(), [0.0, 0.0, 0.0])

    # ...

    def test_drone_movement_Z(self):

        drone = Drone(0.0, 0.0, 0.0)
        drone.moveUp(5)
        self.assertEqual(drone.location(), [0.0, 0.0, 5.0])
        drone.moveUp(-5)
        self.assertEqual(drone.location(), [0.0, 0.0, 0.0])

    # ...


if __name__ == '__main__':
    unittest.main()
