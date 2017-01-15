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
		print("Acc Ax: ", (drone_imu.accel.Ax * 180 / math.pi))
		print("Acc Ay: ", (drone_imu.accel.Ay * 180 / math.pi))
		print()

		# Print gyro data
		print("Gyro x:", drone_imu.gyro.x)
		print("Gyro y:", drone_imu.gyro.y)
		print("Gyro z:", drone_imu.gyro.z)

		# End the cycle
		time.sleep(2)

	
def startup():
	print("----------------")
	print("Starting Pi-drone V.", VERSION)
	print("----------------")


# Start the program
main()