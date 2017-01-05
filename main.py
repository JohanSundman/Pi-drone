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


def main():
	# Create the components
	imu = imu.Imu()

	# The program loop
	while True:
		# Fetch data
		imu.accel.update()

		# Clear before print
		os.system('cls' if os.name == 'nt' else 'clear')

		# Print
		print("x:", imu.accel.x)
		print("y:", imu.accel.y)
		print("z:", imu.accel.z)

		# End the cycle
		time.sleep(0.1)

	



# Start the program
main()