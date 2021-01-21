import time
import json
import math
from Drone import Drone


class Signal():
    def __init__(self, drone):
        self.drone = drone

    def get_data_from_json(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        return data

    def calcSS(self):
        data = self.get_data_from_json()

        distance = (
            ((self.drone.x - data['x'])*(self.drone.x - data['x'])) +
            ((self.drone.y - data['y'])*(self.drone.y - data['y'])) +
            ((self.drone.z - data['z'])*(self.drone.z - data['z'])))

        distance = math.sqrt(distance)
        if(distance >= 100):
            return 0
        else:
            return 100*(1-(distance/100))
