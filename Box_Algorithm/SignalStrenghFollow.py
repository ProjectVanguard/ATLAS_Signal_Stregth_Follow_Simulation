import random
import math



class Vector(object):

    def __init__(self, x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    def getx(self): return self.x
    def gety(self): return self.y
    def getz(self): return self.y
    def pirntVector(self): print (self.x, " ", self.y, " ", self.z," ")



class Pair(object):
    def __init__(self, id, Vector:Vector,signal_strength): self.id, self.Vector, self.signal_strength = id, Vector, signal_strength

    def getId(self): return self.id
    def getV(self): return self.Vector
    def getS(self): return self.signal_strength
    def getfucked(self): return self.getV()

class Drone(object):
    def __init__(self,x=0, y=0, z=0): self.x, self.y, self.z = x, y, z

    def moveUp(self, z): self.x = float(self.z + z)
    def moveDo(self, z): self.x = float(self.z - z)   
    def moveRi(self, y): self.z = float(self.y + y) 
    def moveLe(self, y): self.d = float(self.y - y)
    def moveFr(self, x): self.d = float(self.x + x)
    def moveBa(self, x): self.d = float(self.x - x)

    def location(self):return Vector(self.x,self.y,self.z)

def Calc_SS (Drone,Vector,INITIAL_DISTANCE):
    destination = Vector
    current_location = Drone.location()
    current_distance = math.sqrt(((destination.getx()-current_location.getx())*(destination.getx()-current_location.getx())) +
                     ((destination.gety()-current_location.gety())*(destination.gety()-current_location.gety())) + 
                     ((destination.getz()-current_location.getz())*(destination.getz()-current_location.getz())))
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

def move(Drone,Pair,Vector,INITIAL_DISTANCE):
    t0 = Drone.location()
    maxV = Pair.getV()
    maxS = Pair.getS()
    direction_of_travel = Vector(maxV.getx() - t0.getx(), maxV.gety() - t0.gety(), maxV.getz() - t0.getz())
    Drone.moveFr(direction_of_travel.getx() * 2)
    Drone.moveRi(direction_of_travel.gety() * 2)
    Drone.moveUp(direction_of_travel.getz() * 2)
    while(Calc_SS(Drone,Vector,INITIAL_DISTANCE) > maxS):
        maxS = Calc_SS(Drone,Vector,INITIAL_DISTANCE)
        Drone.moveFr(direction_of_travel.getx())
        Drone.moveRi(direction_of_travel.gety())
        Drone.moveUp(direction_of_travel.getz())
    Drone.moveBa(direction_of_travel.getx())
    Drone.moveLe(direction_of_travel.gety())
    Drone.moveDo(direction_of_travel.getz())
    


    


def Simulation(Drone,Vector,length_of_box):
    INITIAL_DISTANCE = math.sqrt(((Vector.getx()-Drone.location().getx()*(Vector.getx()-Drone.location().getx())) +
                     ((Vector.gety()-Drone.location().gety())*(Vector.gety()-Drone.location().gety())) + 
                     ((Vector.getz()-Drone.location().getz())*(Vector.getz()-Drone.location().getz())))

    temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)
    max = temp_plot[0]         
    for i in temp_plot:
        if (max.getS() <= i.getS()):
            max = i

    if(max.getId() != "T0"):
        move(Drone,max,Vector,INITIAL_DISTANCE)
    else:
        print("The animal is within a box of length " + length_of_box/2 + "on top of the animal")

    while(max.getId != "T0"):
        temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)
        max = temp_plot[0]         
        for i in temp_plot:
            if (max.getS() <= i.getS()):
                max = i

        if(max.getId() != "T0"):
            move(Drone,max,Vector,INITIAL_DISTANCE)



    print("The animal is within a box of length " + length_of_box/2 + "on top of the animal")
        
    

def main():
    drone = Drone(50,50,300)
    lizard = Vector(300,-800,300)
    Simulation(drone,lizard,50)
    
   

if __name__ == "__main__":
    main()



