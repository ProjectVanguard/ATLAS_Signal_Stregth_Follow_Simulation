from Drone import Drone
from Data_Point import Data_Point
from Animal import Animal
from Signal import Signal
import math
# This is the logic of the simulation using all methods to move the drone until it finds the animal.


class Simulation:
    def __init__(self, drone, length_of_box):
        self.drone = drone
        self.length_of_box = length_of_box

# Method that takes Drone object the max Data_Point at the previews boxmition the location of the animal and moves the dorne in direction of the highest known SS.
# This method will need to be refactored since location of the animal will not be needed as well as the initial distance.
# This method uses them in order to use the Calc_SS method that wont be used in the future.
    def move(self, Data_Point):
        t0 = self.drone.location()
        max_Location = Data_Point.get_Location()
        max_Signal = Data_Point.get_Signal()
        direction_of_travel = [max_Location[0] - t0[0],
                               max_Location[1] - t0[1], max_Location[2] - t0[2]]

        print("\n\nDrone will move in %s --> %s direction and it is in %s location relative to its starting position" %
              (Data_Point.id, direction_of_travel, self.drone.location()))

        self.drone.moveFr(direction_of_travel[0] * 2)
        self.drone.moveRi(direction_of_travel[1] * 2)
        self.drone.moveUp(direction_of_travel[2] * 2)

        while(Signal(self.drone).calcSS() > max_Signal):
            max_Signal = Signal(self.drone).calcSS()
            self.drone.moveFr(direction_of_travel[0])
            self.drone.moveRi(direction_of_travel[1])
            self.drone.moveUp(direction_of_travel[2])

        self.drone.moveFr(direction_of_travel[0]*-1)
        self.drone.moveRi(direction_of_travel[1]*-1)
        self.drone.moveUp(direction_of_travel[2]*-1)

# Drone makes a box collecting signal strength and storing them as Data_Point objects and returning that collection.
    def Box_mission(self):
        box_plots = []
        box_plots.append(Data_Point("T0", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data_Point("T1", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveRi((self.length_of_box/2) * -1)
        box_plots.append(Data_Point("T2", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveFr((self.length_of_box/2) * -1)
        box_plots.append(Data_Point("T3", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveFr((self.length_of_box/2) * -1)
        box_plots.append(Data_Point("T4", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveRi(self.length_of_box/2)
        box_plots.append(Data_Point("T5", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveRi(self.length_of_box/2)
        box_plots.append(Data_Point("T6", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data_Point("T7", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveFr(self.length_of_box/2)
        box_plots.append(Data_Point("T8", self.drone.x, self.drone.y,
                                    self.drone.z, Signal(self.drone).calcSS()))
        self.drone.moveRi((self.length_of_box/2) * -1)
        self.drone.moveFr((self.length_of_box/2) * -1)
        return box_plots

    def run(self):

        # Box_mission
        temp_plot = self.Box_mission()

        # Check if the max point in the box mission was T0 if not move in the direction of the max mission if it was end the simulation because you are on top of the animal.
        max = temp_plot[0]
        for i in temp_plot:
            if (max.get_Signal() <= i.get_Signal()):
                max = i
        if(max.get_Id() != "T0"):
            self.move(max)
        else:
            print("\n\nThe animal is below the drone at location %s\n\n" %
                  (self.drone.location()))

        # This repeats the previews logic but in a while loop I did it this way since it needed to be repeted until the animal was found but at the same time the first iteration
        # was needed outside of the loop in order to have a comparable max object to start he loop.
        while(max.get_Id != "T0"):
            temp_plot = self.Box_mission()
            max = temp_plot[0]
            for i in temp_plot:
                if (max.get_Signal() <= i.get_Signal()):
                    max = i

            if(max.get_Id() != "T0"):
                self.move(max)
            else:
                print("\n\nThe animal is below the drone at location %s\n\n" %
                      (self.drone.location()))
                break
