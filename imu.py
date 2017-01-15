# Accelerometer & gyroscope
import time
from link import * # Link to the hardware

# CONSTANTS ADRESSES
ACCEL_X_ADR = 0x3b
ACCEL_Y_ADR = 0x3d
ACCEL_Z_ADR = 0x3f
GYRO_X_ADR = 0x43
GYRO_Y_ADR = 0x45
GYRO_Z_ADR = 0x47
SMBUSS_ADR = 0x68
POWER_MGMT_1 = 0x6b
POWER_MGMT_2 = 0x6c

# CONSTANT VALUES
ACCEL_TO_G = 16384
GYRO_TO_DEG = 131

class Imu:
	x = 0
	y = 0
	z = 0

	def __init__(self):
		wake_up(SMBUSS_ADR, POWER_MGMT_1) # Activate the imu
		self.accel = Accelerometer() # Create an accelerometer instance
		self.gyro = Gyroscope() # Create a gyroscope instance

	def merge(self):
		offsetX = self.accel.get("x", true) - self.x

		# Collect data and merge it with existing
		self.x += offsetX;
		self.y += offsetY;
		self.z += offsetZ;




class Accelerometer:
	
	# Get a variable
	def get(self, axis, scale = True):
		temp = 0
		if axis == "x":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_X_ADR)
		elif axis == "y":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_Y_ADR)
		elif axis == "z":
			temp = read_word_2c(SMBUSS_ADR, ACCEL_Z_ADR)

		# Scale it
		if scale:
			temp = temp / ACCEL_TO_G

		# Send it back
		return temp


	def update(self):
		self.x = self.get("x")
		self.y = self.get("y")
		self.z = self.get("z")


	def accurate(self, times, delay):
		temp = [] # Temporary array of values
		# Measuring multiple values
		for i in range(times):
			x = self.get("x")
			y = self.get("y")
			z = self.get("z")
			temp.append(Axis(x,y,z))
			#time.sleep(delay);

		# Get the avarage out of them
		avg = Axis(0,0,0)
		for obj in temp: # Add them all together
			avg.x += obj.x
			avg.y += obj.y
			avg.z += obj.z
		avg.x /= times # Divide them by their amount
		avg.y /= times
		avg.z /= times
		
		# Return the obj
		return avg



class Gyroscope:

	# Get a variable
	def get(self, axis, scale = True):
		temp = False
		if axis == "x":
			temp = read_word_2c(SMBUSS_ADR, GYRO_X_ADR)
		elif axis == "y":
			temp = read_word_2c(SMBUSS_ADR, GYRO_Y_ADR)
		elif axis == "z":
			temp = read_word_2c(SMBUSS_ADR, GYRO_Y_ADR)
		
		# Scaling
		if scale:
			temp = temp / GYRO_TO_DEG

		# Return
		return temp


	def update(self):
		self.x = self.get("x")
		self.y = self.get("y")
		self.z = self.get("z")


# An axis class containing x y z values
class Axis:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

