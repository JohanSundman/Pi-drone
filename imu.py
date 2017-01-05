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
	
	# Get a variable
	def get(self, axis):
		temp = False
		if axis == "x":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		elif axis == "y":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_Y_ADR)
		elif axis == "z":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_Z_ADR)
		return temp


	def update(self):
		self.x = get("x")
		self.y = get("y")
		self.z = get("z")


	def accurate(self, times, delay):
		temp = [] # Temporary array of values
		# Measuring multiple values
		for i in range(times):
			x = self.get("x")
			y = self.get("x")
			z = self.get("x")
			temp.append(Axis(x,y,z))
			time.sleep(delay);

		# Get the avarage out of them
		avg = Axis(0,0,0)
		for obj in temp: # Add them all together
			avg.x += obj.x
			avg.y += obj.y
			avg.z += obj.z
		
		for instance in avg: # Divide them by the number of measurements
			instance /= times # 
		
		# Return the obj
		return avg



class Gyroscope:
	def update(self):
		pass


class Axis:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

