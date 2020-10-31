##########DEPENDENCIES#############

from dronekit import connect, VehicleMode,LocationGlobalRelative,APIException
import time
import socket
import exceptions
import math
import argparse



########DataObject##############




#########FUNCTIONS#################

def connectMyCopter():

	parser = argparse.ArgumentParser(description='commands')
	parser.add_argument('--connect')
	args = parser.parse_args()

	connection_string = args.connect

	if not connection_string:
		import dronekit_sitl
		sitl = dronekit_sitl.start_default()
		connection_string = sitl.connection_string()

	vehicle = connect(connection_string,wait_ready=True)


	return vehicle


def arm_and_takeoff(targetHeight):


	while vehicle.is_armable!=True:
		print("Waiting for vehicle to become armable.")
		time.sleep(1)
	print("Vehicle is now armable")

	vehicle.mode = VehicleMode("GUIDED")

	while vehicle.mode!='GUIDED':
		print("Waiting for drone to enter GUIDED flight mode")
		time.sleep(1)
	print("Vehicle now in GUIDED MODE. Have fun!!")

	vehicle.armed = True
	while vehicle.armed==False:
		print("Waiting for vehicle to become armed.")
		time.sleep(1)
	print("Look out! Virtual props are spinning!!")

	vehicle.simple_takeoff(targetHeight) ##meters

	while True:
		print("Current Altitude: %d"%vehicle.location.global_relative_frame.alt)
		if vehicle.location.global_relative_frame.alt>=.95*targetHeight:
			break
		time.sleep(1)
	print("Target altitude reached!!")

	return None

def get_distance_meters(targetLocation,currentLocation):
	dLat=targetLocation.lat - currentLocation.lat
	dLon=targetLocation.lon - currentLocation.lon
	
	return math.sqrt((dLon*dLon)+(dLat*dLat))*1.113195e5

def goto(targetLocation):
	distanceToTargetLocation = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)

	vehicle.simple_goto(targetLocation)

	while vehicle.mode.name=="GUIDED":
		currentDistance = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)
		if currentDistance<distanceToTargetLocation*.07:
			print("Reached target waypoint.")
			time.sleep(2)
			break
		time.sleep(1)
	return None

##################DRONE MOVEMENT###################

def move_F_B(scalar):
	go_to_location = vehicle.location.global_relative_frame
	go_to_location.lat += scalar*.00007
	goto(go_to_location)

def move_L_R(scalar):
	go_to_location = vehicle.location.global_relative_frame
	go_to_location.lon += scalar*.00007
	goto(go_to_location)
	
################SIMULATION FUNCTIONS##################

def animal_location(home):
	pass

def calc_SS(currentLocation,animal_location,INITIAL_DISTANCE):
	current_distance = get_distance_meters(animal_location,currentLocation)
	return ((INITIAL_DISTANCE-current_distance)/INITIAL_DISTANCE)*100
	

def box_mission(animal_location,length_of_box,INITIAL_DISTANCE):
	pass


def find_animal(animal_location,length_of_box):
	pass


##########MAIN EXECUTABLE###########

vehicle = connectMyCopter()
arm_and_takeoff(10)

move_F_B(2)
move_L_R(2)
move_F_B(-2)
move_L_R(-2)

