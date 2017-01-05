#	Made by Johan Sundman
#
#
#

import time
import math
#import smbus

from link import * # Link to the hardware
import drone
import imu # Gyro & accelerometer

# CONSTANTS
ACCEL_X_ADR = 0x3b
ACCEL_Y_ADR = 0x3d
ACCEL_Z_ADR = 0x3f
SMBUSS_ADR = 0x68
POWER_MGMT_1 = 0x6b
POWER_MGMT_2 = 0x6c

def main():
	# Create the components
	drone_imu = imu.Imu()
	wake_up(SMBUSS_ADR, POWER_MGMT_1)

	# The program loop
	while True:
		# som stuff
		drone_imu.sleep(1)
		
		# Fetch data
		x = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		y = read_word_2c(SMBUSS_ADR, ACCEL_Y_ADR)
		z = read_word_2c(SMBUSS_ADR, ACCEL_Z_ADR)

		print("x:", x)
		print("y:", y)
		print("z:", z)

		# End the cycle
		time.sleep(0.1)

	



# Start the program
main()