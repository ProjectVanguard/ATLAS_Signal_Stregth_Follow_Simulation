from Animal import Animal

import unittest


class test_Animal(unittest.TestCase):

    def test_animal_in_range(self):
        animal = Animal()
        self.assertTrue(animal.get_Coordinates()['x'] < 100 and animal.get_Coordinates()[
                        'x'] > -100, "Animal not in range X")
        self.assertTrue(animal.get_Coordinates()['y'] < 100 and animal.get_Coordinates()[
                        'y'] > -100, "Animal not in range Y")
        self.assertTrue(animal.get_Coordinates()['z'] < 100 and animal.get_Coordinates()[
                        'z'] > -100, "Animal not in range Z")
    # ...

    def test_animal_movement(self):
        animal = Animal()
        location = animal.get_Coordinates().copy()
        animal.move_animal_location()
        self.assertNotEquals(location, animal.get_Coordinates())


if __name__ == '__main__':
    unittest.main()
