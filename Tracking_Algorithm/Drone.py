
class Drone:

    def __init__(self, x=0, y=0, z=0, pointing_direction='', flight_mode=''):
        self.x = x
        self.y = y
        self.z = z
        self.pointing_direction = pointing_direction
        self.flight_mode = flight_mode

    def location(self):
        return [self.x, self.y, self.z, self.flight_mode, self.pointing_direction]

    def moveFr(self, x):
        self.x = float(self.x + x)

    def moveRi(self, y):
        self.y = float(self.y + y)

    def moveUp(self, z):
        self.z = float(self.z + z)

    def point_towards(self, pointing_direction):
        self.pointing_direction = pointing_direction

    def get_mode(self):
        return self.flight_mode

    def set_mode(self, flight_mode):
        self.flight_mode = flight_mode
