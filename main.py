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

VERSION = "1.5.1";


def main():
	# Init text
	startup()

	# Create the components
	drone_imu = imu.Imu()

	# The program loop
	while True:

		# Clear before print
		os.system('cls' if os.name == 'nt' else 'clear')

		# Fetch data accel data
		data = drone_imu.accel.accurate(4, 0.1)
		# Print accel data
		print("X: ", data.x)
		print("Y: ", data.y)
		print("Z: ", data.z)
		print()
		print("x: ", drone_imu.accel.get("x"))
		print("y: ", drone_imu.accel.get("y"))
		print("z: ", drone_imu.accel.get("z"))
		print()

		# Get gyro data

		# Print gyro data
		print("x:", drone_imu.gyro.get("x"))
		print("y:", drone_imu.gyro.get("y"))
		print("z:", drone_imu.gyro.get("z"))

		# End the cycle
		time.sleep(2)

	
def startup():
	print("----------------")
	print("Starting Pi-drone V.", VERSION)
	print("----------------")


# Start the program
main()