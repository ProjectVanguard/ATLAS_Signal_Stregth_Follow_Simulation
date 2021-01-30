import random
import time
import json


class Animal():
    def __init__(self, x=0, y=0, z=0, grid=[-100, 100]):
        self.coordinates = {
            'x': x,
            'y': y,
            'z': z
        }

        self.grid = grid

        self.generate_fake_cordinates()

    def generate_fake_cordinates(self):
        self.coordinates['x'], self.coordinates['y'] = random.uniform(
            self.grid[0], self.grid[1]), random.uniform(self.grid[0], self.grid[1])

    def move_animal_location(self):
        _randomX = random.uniform(-5, 5)
        _randomY = random.uniform(-5, 5)

        self.coordinates['x'] += _randomX

        if(self.coordinates['x'] < -100):
            self.coordinates['x'] += 10

        elif(self.coordinates['x'] > 100):
            self.coordinates['x'] -= 10

        self.coordinates['y'] += _randomY

        if(self.coordinates['y'] < -100):
            self.coordinates['y'] += 10

        elif(self.coordinates['y'] > 100):
            self.coordinates['y'] -= 10

        self.save_data_to_json()

    def get_Coordinates(self):
        return self.coordinates

    def save_data_to_json(self):
        with open('Tracking_Algorithm/data.json', 'w') as file:
            json.dump(self.coordinates, file)


def main():
    data = Animal()
    while True:

        print('X: {} Y:{} Z:{}'.format(
            data.coordinates['x'], data.coordinates['y'], data.coordinates['z']))
        time.sleep(2)
        data.move_animal_location()


if __name__ == "__main__":
    main()
