# Accelerometer & gyroscope
import time
import math
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
		# Update the values
		self.accel.update()
		self.gyro.update()

		## Data variables
		# self.accel x, y z, Ax, Ay
		# self.gyro x, y, z

		# Here is what our algorithm will do:
		# - accelerometer tells us: "You are now at position Racc"
		# - we say "Thank you, but let me check",
		# - then correct this information with gyroscope data as well as with past Rest data and we output a new estimated vector Rest.
		# - we consider Rest to be our "best bet" as to the current position of the device.
		# Credit: http://www.instructables.com/id/Accelerometer-Gyro-Tutorial/step3/Combining-the-Accelerometer-and-Gyro/



# G forces at each axis
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
		# Update the regular values(scaled)
		self.x = self.get("x", True)
		self.y = self.get("y", True)
		self.z = self.get("z", True)

		# Get the rotational angles | http://www.hobbytronics.co.uk/accelerometer-info
		self.Ax = math.atan2(self.x, math.sqrt(math.pow(self.y, 2) + math.pow(self.z, 2)))
		self.Ay = math.atan2(self.y, math.sqrt(math.pow(self.x, 2) + math.pow(self.z, 2)))



# Rad per second in rotational speed
class Gyroscope:

	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	# Get a variable
	def get(self, axis, scale = True):
		temp = 0
		if axis == "x":
			temp = read_word_2c(SMBUSS_ADR, GYRO_X_ADR)
		elif axis == "y":
			temp = read_word_2c(SMBUSS_ADR, GYRO_Y_ADR)
		elif axis == "z":
			temp = read_word_2c(SMBUSS_ADR, GYRO_Z_ADR)

		# Scaling
		if scale:
			temp = temp / GYRO_TO_DEG

		# Return
		return temp

	def update(self):
		self.x += self.get("x")
		self.y += self.get("y")
		self.z += self.get("z")





# An axis class containing x y z values
class Axis:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
