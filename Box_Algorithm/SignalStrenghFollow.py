import math


#Object to store an ID, vector and Signal strength
class Data(object):
    def __init__(self, id,x,y,z,signal_strength): self.id, self.signal_strength, self.x,self.y, self.z = id, signal_strength,x,y,z

    def getId(self): return self.id
    def getV(self): return [self.x,self.y,self.z]
    def getS(self): return self.signal_strength

#Drone Object
class Drone(object):
    def __init__(self,x=0, y=0, z=0): self.x, self.y, self.z = x, y, z
    def location(self):return [self.x,self.y,self.z]
    def moveFr(self, x): 
        self.x = float(self.x + x)
        
    def moveRi(self, y): 
        self.y = float(self.y + y) 
        
    def moveUp(self, z): 
        self.z = float(self.z + z) 
        
    


#Calculate the simulated signal srenght by repliving this method with the actial signal sreght recived the algorithm will work as designed
def Calc_SS (Drone,Vector,INITIAL_DISTANCE):
    destination = Vector
    current_location = Drone.location()
    current_distance = math.sqrt(((destination[0]-current_location[0])**2) + ((destination[1]-current_location[1])**2) + ((destination[2]-current_location[2])**2))
    return ((INITIAL_DISTANCE-current_distance)/INITIAL_DISTANCE)*100

#Drone makes a box collecting signal strength and storing them as Data objects and returning that collection.
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

#Method that takes Drone object the max data at the previews boxmition the location of the animal and moves the dorne in direction of the highest known SS.
#This method will need to be refactored since location of the animal will not be needed as well as the initial distance.
#This method uses them in order to use the Calc_SS method that wont be used in the future.
def move(Drone,Data,Vector,INITIAL_DISTANCE):
    t0 = Drone.location()
    maxV = Data.getV()
    maxS = Data.getS()
    direction_of_travel = [maxV[0] - t0[0], maxV[1] - t0[1], maxV[2] - t0[2]]
    print(" ")
    print(" ")
    print("Drone will move in %s --> %s direction and it is in %s direction relative to its starting position"%(Data.id,direction_of_travel,Drone.location()))
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
    
#This is the logic of the simulation using all methods to move the drone until it finds the animal.
def Simulation(Drone,Vector,length_of_box):
    #Calculationg INITIAL_DISTANCE for future reference this will not be needed in the refactoring since it is only used for Calc_SS.
    INITIAL_DISTANCE = math.sqrt(((Vector[0]-Drone.location()[0])**2) + ((Vector[1]-Drone.location()[1])**2) + ((Vector[2]-Drone.location()[2])**2))

    #Box_mission
    temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)

    #Check if the max point in the box mission was T0 if not move in the direction of the max mission if it was end the simulation because you are on top of the animal.
    max = temp_plot[0]         
    for i in temp_plot:
        if (max.getS() <= i.getS()):
            max = i
    if(max.getId() != "T0"):
        move(Drone,max,Vector,INITIAL_DISTANCE)
    else:
        print(" ")
        print(" ")
        print("The animal is below the drone at location %s"%(Drone.location()))
        print(" ")
        print(" ")
        

    #This repeats the previews logic but in a while loop I did it this way since it needed to be repeted until the animal was found but at the same time the first iteration
    #was needed outside of the loop in order to have a comparable max object to start he loop.
    while(max.getId != "T0"):
        temp_plot = Box_mission(Drone,Vector,length_of_box,INITIAL_DISTANCE)
        max = temp_plot[0]         
        for i in temp_plot:
            if (max.getS() <= i.getS()):
                max = i

        if(max.getId() != "T0"):
            move(Drone,max,Vector,INITIAL_DISTANCE)
        else:
            print(" ")
            print(" ")
            print("The animal is below the drone at location %s"%(Drone.location()))
            print(" ")
            print(" ")
            break




    
        
    
#Several runs to test functionality.
def main():
    print("################## Simulation 1 ##########################")
    drone = Drone(0,0,100)
    lizard = [4234,234,0]
    Simulation(drone,lizard,3)
    print("#########################################################")
    print(" ")
    print(" ")
    print("################## Simulation 2 ##########################")
    drone = Drone(40,300,100)
    lizard = [0,0,0]
    Simulation(drone,lizard,3)
    print("#########################################################")
    print(" ")
    print(" ")
    print("################## Simulation 3 ##########################")
    drone = Drone(0,0,100)
    lizard = [20,5,0]
    Simulation(drone,lizard,10)
    print("#########################################################")
    print(" ")
    print(" ")
    print("################## Simulation 4 ##########################")
    drone = Drone(1111,23234,100)
    lizard = [0,0,0]
    Simulation(drone,lizard,3)
    print("#########################################################")
    print(" ")
    print(" ")
    print("################## Simulation 5 ##########################")
    drone = Drone(0,0,100)
    lizard = [3333,9999,0]
    Simulation(drone,lizard,5)
    print("#########################################################")
    print(" ")
    print(" ")

   

if __name__ == "__main__":
    main()



