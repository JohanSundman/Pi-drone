#	Made by Johan Sundman
#
#
#

import time
import math
#import smbus

from link import *
import drone
import imu # Gyro & accelerometer

def main():
	# Create the components
	drone_imu = imu.Imu()
	
	# The program loop
	while True:
		# som stuff
		drone_imu.sleep(1)
		# End the cycle
		time.sleep(0.1)
		print("..")
		link.testFunc()
	



# Start the program
main()