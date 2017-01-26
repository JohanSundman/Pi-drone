#	Made by Johan Sundman
#
#
#

import time
import math
import os

from link import * # Link to the hardware
import drone
import imu # Gyro & accelerometer

VERSION = "1.4.5";


def main():
	# Init text
	startup()

	# Create the components
	drone_imu = imu.Imu()

	# The program loop
	while True:

		# Clear before print
		os.system('cls' if os.name == 'nt' else 'clear')

		# Update the values
		drone_imu.accel.update();
		drone_imu.gyro.update();


		# Print accel data
		print("Acc x: ", drone_imu.accel.x)
		print("Acc y: ", drone_imu.accel.y)
		print("Acc z: ", drone_imu.accel.z)
		print()
		print("Acc Ax: ", radToDeg(drone_imu.accel.Ax))
		print("Acc Ay: ", radToDeg(drone_imu.accel.Ay))
		print()

		# Print gyro data
		print("Gyro x:", radToDeg(drone_imu.gyro.x)) # Rad per second -> deg per second
		print("Gyro y:", radToDeg(drone_imu.gyro.y))
		print("Gyro z:", radToDeg(drone_imu.gyro.z))

		# Merged!
		drone.imu.merge()
		print()
		print("Merged x:", radToDeg(drone.imu.x))
		print()
		
		# End the cycle
		time.sleep(2)

	
def startup():
	print("----------------")
	print("Starting Pi-drone V.", VERSION)
	print("----------------")

def radToDeg(deg):
	return deg * 180 / math.pi

# Start the program
main()