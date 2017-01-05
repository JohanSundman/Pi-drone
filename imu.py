# Accelerometer & gyroscope
import time
from link import * # Link to the hardware

# CONSTANTS
ACCEL_X_ADR = 0x3b
ACCEL_Y_ADR = 0x3d
ACCEL_Z_ADR = 0x3f
SMBUSS_ADR = 0x68
POWER_MGMT_1 = 0x6b
POWER_MGMT_2 = 0x6c


class Imu:
	def __init__(self):
		wake_up(SMBUSS_ADR, POWER_MGMT_1) # Activate the imu
		self.accel = Accelerometer() # Create an accelerometer instance
		self.gyro = Gyroscope() # Create a gyroscope instance



class Accelerometer:
	def update(self):
		self.x = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		self.y = read_word_2c(SMBUSS_ADR, ACCEL_Y_ADR)
		self.z = read_word_2c(SMBUSS_ADR, ACCEL_Z_ADR)


class Gyroscope:
	def update(self):
		pass