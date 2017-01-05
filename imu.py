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
	buss # The bus to get info from
	accel # The accelerometer object
	gyro # The gyroscope object

	def __init__(self):
		wake_up(SMBUSS_ADR, POWER_MGMT_1) # Activate the imu
		self.accel = Accelerometer() # Create an accelerometer instance
		self.gyro = Gyroscope() # Create a gyroscope instance



class Accelerometer(Imu):
	x, y, z # Axises

	def update():
		self.x = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		self.x = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		self.x = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)


class Gyroscope(Imu):
	def update():
		pass