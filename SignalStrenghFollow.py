import random
import math



class Vector(object):

    def __init__(self, x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    
    def getx(self): return self.x
    def gety(self): return self.y
    def getz(self): return self.y
    

    def pirntVector(self): print (self.x, " ", self.y, " ", self.z," ")

class Pair(object):
    def __init__(self, id, vector,signal_strength): self.id, self.vector, self.signal_strength = id, vector, signal_strength

    def getId(self): return self.id
    def getV(self): return self.vector
    def getS(self): return self.signal_strength

class Drone(object):
    def __init__(self,x=0, y=0, z=0): self.x, self.y, self.z = x, y, z

    def moveUp(self, x): self.x = float(self.x + x)
    def moveDo(self, x): self.x = float(self.x - x)   
    def moveRi(self, y): self.z = float(self.x + y) 
    def moveLe(self, y): self.d = float(self.x - y)
    def moveFr(self, z): self.d = float(self.x + z)
    def moveBa(self, z): self.d = float(self.x - z)

    def location(self):return Vector(self.x,self.y,self.z)

def Calc_SS (Drone,Vector,INITIAL_DISTANCE):
    destination = Vector
    current_location = Drone.location
    current_distance = math.sqrt(((destination.x-current_location.x)*(destination.x-current_location.x)) +
                     ((destination.y-current_location.y)*(destination.y-current_location.y)) + 
                     ((destination.z-current_location.z)*(destination.z-current_location.z)))
    return ((INITIAL_DISTANCE-current_distance)/INITIAL_DISTANCE)*100

def Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE):
    box_plots = []
    box_plots.append(Pair("T0",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Pair("T1",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveLe(length_of_box/2)
    box_plots.append(Pair("T2",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveBa(length_of_box/2)
    box_plots.append(Pair("T3",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveBa(length_of_box/2)
    box_plots.append(Pair("T4",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi(length_of_box/2)
    box_plots.append(Pair("T5",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi(length_of_box/2)
    box_plots.append(Pair("T6",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Pair("T7",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Pair("T8",Drone.location,Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveLe(length_of_box/2)
    Drone.moveBa(length_of_box/2)
    return box_plots

def move(Drone,Pair,meters):
    pass



def Simulation(Drone,Vector,length_of_box):
    INITIAL_DISTANCE = math.sqrt(((Vector.x-Drone.x)*(Vector.x-Drone.x)) +
                     ((Vector.y-Drone.y)*(Vector.y-Drone.y)) + 
                     ((Vector.z-Drone.z)*(Vector.z-Drone.z)))

    temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)
    max = temp_plot[0]         
    for i in temp_plot:
        if (max.getS() <= i.getS()):
            max = i

    if(max.getId() != "T0"):
        move(Drone,max,10)
    else:
        print("The animal is within a box of length " + length_of_box/2 + "on top of the animal")

    while(max.getId != "T0"):
        temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)
        max = temp_plot[0]         
        for i in temp_plot:
            if (max.getS() <= i.getS()):
                max = i

        if(max.getId() != "T0"):
            move(Drone,max,10)



    print("The animal is within a box of length " + length_of_box/2 + "on top of the animal")
        
    

def main():
   pass

    








if __name__ == "__main__":
    main()



