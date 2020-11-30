
class Drone:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def location(self):
        return [self.x, self.y, self.z]

    def moveFr(self, x):
        self.x = float(self.x + x)

    def moveRi(self, y):
        self.y = float(self.y + y)

    def moveUp(self, z):
        self.z = float(self.z + z)
