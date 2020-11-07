#Object to store an ID, vector and Signal strength
class Data(object):
    def __init__(self, _id,x,y,z,signal_strength): 
        self.id = _id
        self.signal_strength = signal_strength 
        self.x = x
        self.y = y 
        self.z = z

    def getId(self): 
        return self.id
    def getV(self): 
        return [self.x,self.y,self.z]
    def getS(self): 
        return self.signal_strength
