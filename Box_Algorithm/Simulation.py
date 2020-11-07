from Drone import Drone
from Data import Data
import math
#This is the logic of the simulation using all methods to move the drone until it finds the animal.
class Simulation:
    def __init__(self,drone,animal,length_of_box):
        self.drone = drone
        self.animal = animal
        self.length_of_box = length_of_box
    
#Method that takes Drone object the max data at the previews boxmition the location of the animal and moves the dorne in direction of the highest known SS.
#This method will need to be refactored since location of the animal will not be needed as well as the initial distance.
#This method uses them in order to use the Calc_SS method that wont be used in the future.
    def move(self,Data,INITIAL_DISTANCE):
        t0 = self.drone.location()
        maxV = Data.getV()
        maxS = Data.getS()
        direction_of_travel = [maxV[0] - t0[0], maxV[1] - t0[1], maxV[2] - t0[2]]
        print("\n\nDrone will move in %s --> %s direction and it is in %s location relative to its starting position"%(Data.id,direction_of_travel,self.drone.location()))
        self.drone.moveFr(direction_of_travel[0] * 2)
        self.drone.moveRi(direction_of_travel[1] * 2)
        self.drone.moveUp(direction_of_travel[2] * 2)
        while(self.Calc_SS(INITIAL_DISTANCE) > maxS):
            maxS = self.Calc_SS(INITIAL_DISTANCE)
            self.drone.moveFr(direction_of_travel[0])
            self.drone.moveRi(direction_of_travel[1])
            self.drone.moveUp(direction_of_travel[2])
        self.drone.moveFr(direction_of_travel[0]*-1)
        self.drone.moveRi(direction_of_travel[1]*-1)
        self.drone.moveUp(direction_of_travel[2]*-1)
    
#Drone makes a box collecting signal strength and storing them as Data objects and returning that collection.
    def Box_mission(self,INITIAL_DISTANCE):
        box_plots = []
        box_plots.append(Data("T0",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data("T1",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveRi((self.length_of_box/2) * -1)
        box_plots.append(Data("T2",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveFr((self.length_of_box/2) * -1)
        box_plots.append(Data("T3",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveFr((self.length_of_box/2) * -1)
        box_plots.append(Data("T4",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveRi(self.length_of_box/2)
        box_plots.append(Data("T5",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveRi(self.length_of_box/2)
        box_plots.append(Data("T6",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data("T7",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data("T8",self.drone.location()[0],self.drone.location()[1],self.drone.location()[2],self.Calc_SS(INITIAL_DISTANCE)))
        self.drone.moveRi((self.length_of_box/2) * -1)
        self.drone.moveFr((self.length_of_box/2) * -1)
        return box_plots
    #Calculate the simulated signal srenght by repliving this method with the actial signal sreght recived the algorithm will work as designed
    def Calc_SS (self,INITIAL_DISTANCE):
        destination = self.animal
        current_location = self.drone.location()

        current_distance = math.sqrt(((destination.x-current_location[0])**2) + 
        ((destination.y-current_location[1])**2) + 
        ((destination.z-current_location[2])**2))

        return ((INITIAL_DISTANCE-current_distance)/INITIAL_DISTANCE)*100


    def run(self):
        #Calculationg INITIAL_DISTANCE for future reference this will not be needed in the refactoring since it is only used for Calc_SS.
        INITIAL_DISTANCE = math.sqrt(((self.animal.x-self.drone.location()[0])**2) + ((self.animal.y-self.drone.location()[1])**2) + ((self.animal.z-self.drone.location()[2])**2))

        #Box_mission
        temp_plot = self.Box_mission(INITIAL_DISTANCE)

        #Check if the max point in the box mission was T0 if not move in the direction of the max mission if it was end the simulation because you are on top of the animal.
        max = temp_plot[0]         
        for i in temp_plot:
            if (max.getS() <= i.getS()):
                max = i
        if(max.getId() != "T0"):
            self.move(max,INITIAL_DISTANCE)
        else:
            print("\n\nThe animal is below the drone at location %s\n\n"%(self.drone.location()))

            

        #This repeats the previews logic but in a while loop I did it this way since it needed to be repeted until the animal was found but at the same time the first iteration
        #was needed outside of the loop in order to have a comparable max object to start he loop.
        while(max.getId != "T0"):
            temp_plot = self.Box_mission(INITIAL_DISTANCE)
            max = temp_plot[0]         
            for i in temp_plot:
                if (max.getS() <= i.getS()):
                    max = i

            if(max.getId() != "T0"):
                self.move(max,INITIAL_DISTANCE)
            else:
                print("\n\nThe animal is below the drone at location %s\n\n"%(self.drone.location()))
                break