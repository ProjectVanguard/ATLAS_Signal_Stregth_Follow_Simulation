# Object to store an ID, vector and Signal strength
class Data_Point(object):
    def __init__(self, _id, x, y, z, signal_strength):
        self.id = _id
        self.signal_strength = signal_strength
        self.x = x
        self.y = y
        self.z = z

    def get_Id(self):
        return self.id

    def get_Location(self):
        return [self.x, self.y, self.z]

    def get_Signal(self):
        return self.signal_strength
