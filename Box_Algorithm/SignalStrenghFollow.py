import math

class Data(object):
    def __init__(self, id,x,y,z,signal_strength): self.id, self.signal_strength, self.x,self.y, self.z = id, signal_strength,x,y,z

    def getId(self): return self.id
    def getV(self): return [self.x,self.y,self.z]
    def getS(self): return self.signal_strength

class Drone(object):
    def __init__(self,x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    def moveFr(self, x): self.x = float(self.x + x)
    def moveRi(self, y): self.y = float(self.y + y) 
    def moveUp(self, z): self.z = float(self.z + z) 
    
    
    

    def location(self):return [self.x,self.y,self.z]

def Calc_SS (Drone,Vector,INITIAL_DISTANCE):
    destination = Vector
    current_location = Drone.location()
    current_distance = math.sqrt(((destination[0]-current_location[0])*(destination[0]-current_location[0])) +
                     ((destination[1]-current_location[1])*(destination[1]-current_location[1])) + 
                     ((destination[2]-current_location[2])*(destination[2]-current_location[2])))
    return ((INITIAL_DISTANCE-current_distance)/INITIAL_DISTANCE)*100

def Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE):
    box_plots = []
    box_plots.append(Data("T0",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Data("T1",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi((length_of_box/2) * -1)
    box_plots.append(Data("T2",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr((length_of_box/2) * -1)
    box_plots.append(Data("T3",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr((length_of_box/2) * -1)
    box_plots.append(Data("T4",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi(length_of_box/2)
    box_plots.append(Data("T5",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi(length_of_box/2)
    box_plots.append(Data("T6",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Data("T7",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveFr(length_of_box/2)
    box_plots.append(Data("T8",Drone.location()[0],Drone.location()[1],Drone.location()[2],Calc_SS(Drone,Vector,INITIAL_DISTANCE)))
    Drone.moveRi((length_of_box/2) * -1)
    Drone.moveFr((length_of_box/2) * -1)
    return box_plots

def move(Drone,Data,Vector,INITIAL_DISTANCE):
    t0 = Drone.location()
    maxV = Data.getV()
    maxS = Data.getS()
    direction_of_travel = [maxV[0] - t0[0], maxV[1] - t0[1], maxV[2] - t0[2]]
    Drone.moveFr(direction_of_travel[0] * 2)
    Drone.moveRi(direction_of_travel[1] * 2)
    Drone.moveUp(direction_of_travel[2] * 2)
    while(Calc_SS(Drone,Vector,INITIAL_DISTANCE) > maxS):
        maxS = Calc_SS(Drone,Vector,INITIAL_DISTANCE)
        Drone.moveFr(direction_of_travel[0])
        Drone.moveRi(direction_of_travel[1])
        Drone.moveUp(direction_of_travel[2])
    Drone.moveFr(direction_of_travel[0]*-1)
    Drone.moveRi(direction_of_travel[1]*-1)
    Drone.moveUp(direction_of_travel[2]*-1)
    


    


def Simulation(Drone,Vector,length_of_box):
    INITIAL_DISTANCE = math.sqrt(((Vector[0]-Drone.location()[0]*(Vector[0]-Drone.location()[0])) +
                     ((Vector[1]-Drone.location()[1])*(Vector[1]-Drone.location()[1])) + 
                     ((Vector[2]-Drone.location()[2])*(Vector[2]-Drone.location()[2]))))

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
    drone = Drone(0,0,100)
    lizard = [1000,-500,100]
    Simulation(drone,lizard,10)
   

if __name__ == "__main__":
    main()



